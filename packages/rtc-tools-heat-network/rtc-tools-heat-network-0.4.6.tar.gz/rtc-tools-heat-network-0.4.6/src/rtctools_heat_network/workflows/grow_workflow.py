import json
import locale
import logging
import os
import time
import xml.etree.ElementTree as ET  # noqa: N817
from pathlib import Path

from influxdb import InfluxDBClient

import numpy as np

from rtctools._internal.alias_tools import AliasDict
from rtctools.optimization.collocated_integrated_optimization_problem import (
    CollocatedIntegratedOptimizationProblem,
)
from rtctools.optimization.goal_programming_mixin_base import Goal
from rtctools.optimization.linearized_order_goal_programming_mixin import (
    LinearizedOrderGoalProgrammingMixin,
)
from rtctools.optimization.single_pass_goal_programming_mixin import (
    CachingQPSol,
    SinglePassGoalProgrammingMixin,
)
from rtctools.util import run_optimization_problem

from rtctools_heat_network.esdl.esdl_mixin import ESDLMixin
from rtctools_heat_network.head_loss_class import HeadLossOption
from rtctools_heat_network.techno_economic_mixin import TechnoEconomicMixin
from rtctools_heat_network.workflows.goals.minimize_discounted_tco import MinimizeDiscountedTCO
from rtctools_heat_network.workflows.goals.minimize_tco_goal import MinimizeTCO
from rtctools_heat_network.workflows.io.write_output import ScenarioOutput
from rtctools_heat_network.workflows.utils.adapt_profiles import (
    adapt_hourly_year_profile_to_day_averaged_with_hourly_peak_day,
)
from rtctools_heat_network.workflows.utils.helpers import main_decorator


DB_HOST = "172.17.0.2"
DB_PORT = 8086
DB_NAME = "Warmtenetten"
DB_USER = "admin"
DB_PASSWORD = "admin"

logger = logging.getLogger("WarmingUP-MPC")
logger.setLevel(logging.INFO)

locale.setlocale(locale.LC_ALL, "")

ns = {"fews": "http://www.wldelft.nl/fews", "pi": "http://www.wldelft.nl/fews/PI"}

WATT_TO_MEGA_WATT = 1.0e6
WATT_TO_KILO_WATT = 1.0e3


class TargetHeatGoal(Goal):
    priority = 1

    order = 2

    def __init__(self, state, target):
        self.state = state

        self.target_min = target
        self.target_max = target
        try:
            self.function_range = (-1.0e6, max(2.0 * max(target.values), 1.0e6))
            self.function_nominal = max(np.median(target.values), 1.0e6)
        except Exception:
            self.function_range = (-1.0e6, max(2.0 * target, 1.0e6))
            self.function_nominal = max(target, 1.0e6)

    def function(self, optimization_problem, ensemble_member):
        return optimization_problem.state(self.state)


class EndScenarioSizingDiscounted(
    ScenarioOutput,
    TechnoEconomicMixin,
    LinearizedOrderGoalProgrammingMixin,
    SinglePassGoalProgrammingMixin,
    ESDLMixin,
    CollocatedIntegratedOptimizationProblem,
):
    """
    Goal priorities are:
    1. Match heat demand with target
    2. minimize TCO = Capex + Opex*lifetime
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._override_hn_options = {}

        self._number_of_years = 30.0

        self.__indx_max_peak = None
        self.__day_steps = 5

        # self._override_pipe_classes = {}

        # variables for solver settings
        self._qpsol = None

        self._hot_start = False

        # Store (time taken, success, objective values, solver stats) per priority
        self._priorities_output = []
        self.__priority = None
        self.__priority_timer = None

        self.__heat_demand_bounds = dict()
        self.__heat_demand_nominal = dict()

    def _get_runinfo_path_root(self):
        runinfo_path = Path(self.esdl_run_info_path).resolve()
        tree = ET.parse(runinfo_path)
        return tree.getroot()

    def parameters(self, ensemble_member):
        parameters = super().parameters(ensemble_member)
        parameters["peak_day_index"] = self.__indx_max_peak
        parameters["time_step_days"] = self.__day_steps
        parameters["number_of_years"] = self._number_of_years
        return parameters

    def pipe_classes(self, p):
        return self._override_pipe_classes.get(p, [])

    def pre(self):
        self._qpsol = CachingQPSol()

        super().pre()

        # parameters = self.parameters(0)
        # bounds = self.bounds()

        # TODO: these constraints do no longer work as we now have varying size timesteps
        # for s in self._setpoint_constraints_sources:
        #     # Here we enforce that over the full time horizon no setpoint changes can be done
        #     self._timed_setpoints[s] = (len(self.times()), 0)
        #
        # # Mixed-interger formulation of component setpoint
        # for component_name in self._timed_setpoints.keys():
        #     # Make 1 variable per component (so not per control
        #     # variable) which represents if the setpoint of the component
        #     # is changed (1) is not changed (0) in a timestep
        #     change_setpoint_var = f"{component_name}._change_setpoint_var"
        #     self._component_to_change_setpoint_map[component_name] = change_setpoint_var
        #     self._change_setpoint_var[change_setpoint_var] = ca.MX.sym(change_setpoint_var)
        #     self._change_setpoint_bounds[change_setpoint_var] = (0, 1.0)

    def read(self):
        """
        Reads the yearly profile with hourly time steps and adapt to a daily averaged profile
        except for the day with the peak demand.
        """
        super().read()

        (
            self.__indx_max_peak,
            self.__heat_demand_nominal,
        ) = adapt_hourly_year_profile_to_day_averaged_with_hourly_peak_day(self, self.__day_steps)

        logger.info("HeatProblem read")

    def bounds(self):
        bounds = super().bounds()
        bounds.update(self.__heat_demand_bounds)
        return bounds

    def variable_nominal(self, variable):
        try:
            return self.__heat_demand_nominal[variable]
        except KeyError:
            return super().variable_nominal(variable)

    def heat_network_options(self):
        # TODO: make empty placeholder in HeatProblem we don't know yet how to put the global
        #  constraints in the ESDL e.g. min max pressure
        options = super().heat_network_options()
        options["minimum_velocity"] = 0.001
        options["maximum_velocity"] = 3.0
        options["maximum_temperature_der"] = np.inf
        options["neglect_pipe_heat_losses"] = True
        options["heat_loss_disconnected_pipe"] = True
        options["head_loss_option"] = HeadLossOption.NO_HEADLOSS
        # options.update(self._override_hn_options)
        return options

    def esdl_heat_model_options(self):
        """Overwrites the fraction of the minimum tank volume"""
        options = super().esdl_heat_model_options()
        options["min_fraction_tank_volume"] = 0.0
        return options

    def path_goals(self):
        goals = super().path_goals().copy()
        bounds = self.bounds()

        for demand in self.heat_network_components["demand"]:
            # target = self.get_timeseries(f"{demand}.target_heat_demand_peak")
            target = self.get_timeseries(f"{demand}.target_heat_demand")
            if bounds[f"{demand}.HeatIn.Heat"][1] < max(target.values):
                logger.warning(
                    f"{demand} has a flow limit, {bounds[f'{demand}.HeatIn.Heat'][1]}, "
                    f"lower that wat is required for the maximum demand {max(target.values)}"
                )
            state = f"{demand}.Heat_demand"

            goals.append(TargetHeatGoal(state, target))
        return goals

    def goals(self):
        goals = super().goals().copy()
        # We do a minization of TCO consisting of CAPEX and OPEX
        # CAPEX is based upon the boolean placement variables and the optimized maximum sizes
        # Note that CAPEX for geothermal and ATES is also dependent on the amount of doublets
        # In practice this means that the CAPEX is mainly driven by the peak day problem
        # The OPEX is based on the Source strategy which is computed on the __daily_avg variables
        # The OPEX thus is based on an avg strategy and discrepancies due to fluctuations intra-day
        # are possible.
        # The idea behind the two timelines is that the optimizer can make the OPEX vs CAPEX
        # trade-offs

        goals.append(MinimizeDiscountedTCO(priority=2))

        return goals

    def constraints(self, ensemble_member):
        constraints = super().constraints(ensemble_member)

        for a in self.heat_network_components.get("ates", []):
            stored_heat = self.state_vector(f"{a}.Stored_heat")
            constraints.append(((stored_heat[-1] - stored_heat[0]), 0.0, np.inf))

        for b in self.heat_network_components.get("buffer", {}):
            vars = self.state_vector(f"{b}.Heat_buffer")
            symbol_stored_heat = self.state_vector(f"{b}.Stored_heat")
            constraints.append((symbol_stored_heat[self.__indx_max_peak], 0.0, 0.0))
            for i in range(len(self.times())):
                if i < self.__indx_max_peak or i > (self.__indx_max_peak + 23):
                    constraints.append((vars[i], 0.0, 0.0))

        return constraints

    def history(self, ensemble_member):
        return AliasDict(self.alias_relation)

    def __state_vector_scaled(self, variable, ensemble_member):
        canonical, sign = self.alias_relation.canonical_signed(variable)
        return (
            self.state_vector(canonical, ensemble_member) * self.variable_nominal(canonical) * sign
        )

    def solver_options(self):
        options = super().solver_options()
        options["casadi_solver"] = self._qpsol
        options["solver"] = "gurobi"
        gurobi_options = options["gurobi"] = {}
        gurobi_options["MIPgap"] = 0.02
        gurobi_options["threads"] = 4
        gurobi_options["LPWarmStart"] = 2

        return options

    def solver_success(self, solver_stats, log_solver_failure_as_error):
        success, log_level = super().solver_success(solver_stats, log_solver_failure_as_error)

        # Allow time-outs for CPLEX and CBC
        if (
            solver_stats["return_status"] == "time limit exceeded"
            or solver_stats["return_status"] == "stopped - on maxnodes, maxsols, maxtime"
        ):
            if self.objective_value > 1e10:
                # Quick check on the objective value. If no solution was
                # found, this is typically something like 1E50.
                return success, log_level

            return True, logging.INFO
        else:
            return success, log_level

    def priority_started(self, priority):
        self.__priority = priority
        self.__priority_timer = time.time()

        super().priority_started(priority)

    def priority_completed(self, priority):
        super().priority_completed(priority)

        self._hot_start = True

        time_taken = time.time() - self.__priority_timer
        self._priorities_output.append(
            (
                priority,
                time_taken,
                True,
                self.objective_value,
                self.solver_stats,
            )
        )

    def post(self):
        # In case the solver fails, we do not get in priority_completed(). We
        # append this last priority's statistics here in post().
        # TODO: check if we still need this small part of code below
        success, _ = self.solver_success(self.solver_stats, False)
        if not success:
            time_taken = time.time() - self.__priority_timer
            self._priorities_output.append(
                (
                    self.__priority,
                    time_taken,
                    False,
                    self.objective_value,
                    self.solver_stats,
                )
            )

        super().post()
        results = self.extract_results()
        parameters = self.parameters(0)
        # bounds = self.bounds()
        # Optimized ESDL
        self._write_updated_esdl()

        for d in self.heat_network_components.get("demand", []):
            realized_demand = results[f"{d}.Heat_demand"]
            target = self.get_timeseries(f"{d}.target_heat_demand").values
            timesteps = np.diff(self.get_timeseries(f"{d}.target_heat_demand").times)
            parameters[f"{d}.target_heat_demand"] = target.tolist()
            delta_energy = np.sum((realized_demand - target)[1:] * timesteps / 1.0e9)
            if delta_energy >= 1.0:
                logger.warning(f"For demand {d} the target is not matched by {delta_energy} GJ")

        if self.esdl_run_info_path is None:
            logger.warning(
                "Not writing results since no esdl path to write the files to is specified"
            )
            return

        root = self._get_runinfo_path_root()
        parameters_dict = dict()
        workdir = root.findtext("pi:outputResultsFile", namespaces=ns)
        if workdir is None:
            logger.error("No workdir specified, skipping writing results")
            return

        parameter_path = os.path.join(workdir, "parameters.json")
        for key, value in parameters.items():
            new_value = value  # [x for x in value]
            parameters_dict[key] = new_value
        if parameter_path is None:
            workdir = root.findtext("pi:workDir", namespaces=ns)
            parameter_path = os.path.join(workdir, "parameters.json")
            if not Path(workdir).is_absolute():
                parameter_path = Path(workdir).resolve().parent
                parameter_path = os.path.join(parameter_path.__str__() + "parameters.json")
        with open(parameter_path, "w") as file:
            json.dump(parameters_dict, fp=file)

        # root = self._get_runinfo_path_root()
        # bounds_dict = dict()
        # bounds_path = root.findtext("pi:outputResultsFile", namespaces=ns)
        # bounds_path = os.path.join(workdir, "bounds.json")
        # for key, value in bounds.items():
        #     if "Stored_heat" not in key:
        #         new_value = value  # [x for x in value]
        #         # if len(new_value) == 1:
        #         #     new_value = new_value[0]
        #         bounds_dict[key] = new_value
        # if bounds_path is None:
        #     workdir = root.findtext("pi:workDir", namespaces=ns)
        #     bounds_path = os.path.join(workdir, "bounds.json")
        #     if not Path(workdir).is_absolute():
        #         bounds_path = Path(workdir).resolve().parent
        #         bounds_path = os.path.join(bounds_path.__str__() + "bounds.json")
        # with open(bounds_path, "w") as file:
        #     json.dump(bounds_dict, fp=file)

        root = self._get_runinfo_path_root()
        results_path = root.findtext("pi:outputResultsFile", namespaces=ns)
        results_dict = dict()

        for key, values in results.items():
            new_value = values.tolist()
            if len(new_value) == 1:
                new_value = new_value[0]
            results_dict[key] = new_value

        results_path = os.path.join(workdir, "results.json")
        if results_path is None:
            workdir = root.findtext("pi:workDir", namespaces=ns)
            results_path = os.path.join(workdir, "results.json")
            if not Path(workdir).is_absolute():
                results_path = Path(workdir).resolve().parent
                results_path = os.path.join(results_path.__str__() + "results.json")
        with open(results_path, "w") as file:
            json.dump(results_dict, fp=file)


class EndScenarioSizingDiscountedHIGHS(EndScenarioSizingDiscounted):
    def solver_options(self):
        options = super().solver_options()
        options["casadi_solver"] = self._qpsol
        options["solver"] = "highs"
        highs_options = options["highs"] = {}
        highs_options["mip_rel_gap"] = 0.02

        options["gurobi"] = None

        return options


class EndScenarioSizing(
    ScenarioOutput,
    TechnoEconomicMixin,
    LinearizedOrderGoalProgrammingMixin,
    SinglePassGoalProgrammingMixin,
    ESDLMixin,
    CollocatedIntegratedOptimizationProblem,
):
    """
    Goal priorities are:
    1. minimize TCO = Capex + Opex*lifetime
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._override_hn_options = {}

        self._number_of_years = 30.0

        self.__indx_max_peak = None
        self.__day_steps = 5

        # self._override_pipe_classes = {}

        # variables for solver settings
        self._qpsol = None

        self._hot_start = False

        # Store (time taken, success, objective values, solver stats) per priority
        self._priorities_output = []
        self.__priority = None
        self.__priority_timer = None

        self.__heat_demand_bounds = dict()
        self.__heat_demand_nominal = dict()

    def _get_runinfo_path_root(self):
        runinfo_path = Path(self.esdl_run_info_path).resolve()
        tree = ET.parse(runinfo_path)
        return tree.getroot()

    def parameters(self, ensemble_member):
        parameters = super().parameters(ensemble_member)
        parameters["peak_day_index"] = self.__indx_max_peak
        parameters["time_step_days"] = self.__day_steps
        parameters["number_of_years"] = self._number_of_years
        return parameters

    def pipe_classes(self, p):
        return self._override_pipe_classes.get(p, [])

    def pre(self):
        self._qpsol = CachingQPSol()

        super().pre()

        # parameters = self.parameters(0)
        # bounds = self.bounds()

        # TODO: these constraints do no longer work as we now have varying size timesteps
        # for s in self._setpoint_constraints_sources:
        #     # Here we enforce that over the full time horizon no setpoint changes can be done
        #     self._timed_setpoints[s] = (len(self.times()), 0)
        #
        # # Mixed-interger formulation of component setpoint
        # for component_name in self._timed_setpoints.keys():
        #     # Make 1 variable per component (so not per control
        #     # variable) which represents if the setpoint of the component
        #     # is changed (1) is not changed (0) in a timestep
        #     change_setpoint_var = f"{component_name}._change_setpoint_var"
        #     self._component_to_change_setpoint_map[component_name] = change_setpoint_var
        #     self._change_setpoint_var[change_setpoint_var] = ca.MX.sym(change_setpoint_var)
        #     self._change_setpoint_bounds[change_setpoint_var] = (0, 1.0)

    def read(self):
        """
        Reads the yearly profile with hourly time steps and adapt to a daily averaged profile
        except for the day with the peak demand.
        """
        super().read()

        (
            self.__indx_max_peak,
            self.__heat_demand_nominal,
        ) = adapt_hourly_year_profile_to_day_averaged_with_hourly_peak_day(self, self.__day_steps)

        logger.info("HeatProblem read")

    def bounds(self):
        bounds = super().bounds()
        bounds.update(self.__heat_demand_bounds)
        return bounds

    def variable_nominal(self, variable):
        try:
            return self.__heat_demand_nominal[variable]
        except KeyError:
            return super().variable_nominal(variable)

    def heat_network_options(self):
        # TODO: make empty placeholder in HeatProblem we don't know yet how to put the global
        #  constraints in the ESDL e.g. min max pressure
        options = super().heat_network_options()
        options["minimum_velocity"] = 0.001
        options["maximum_velocity"] = 3.0
        options["maximum_temperature_der"] = np.inf
        # options["neglect_pipe_heat_losses"] = True
        options["heat_loss_disconnected_pipe"] = True
        options["head_loss_option"] = HeadLossOption.NO_HEADLOSS
        # options.update(self._override_hn_options)
        return options

    def esdl_heat_model_options(self):
        """Overwrites the fraction of the minimum tank volume"""
        options = super().esdl_heat_model_options()
        options["min_fraction_tank_volume"] = 0.0
        return options

    def path_goals(self):
        goals = super().path_goals().copy()
        bounds = self.bounds()

        for demand in self.heat_network_components["demand"]:
            # target = self.get_timeseries(f"{demand}.target_heat_demand_peak")
            target = self.get_timeseries(f"{demand}.target_heat_demand")
            if bounds[f"{demand}.HeatIn.Heat"][1] < max(target.values):
                logger.warning(
                    f"{demand} has a flow limit, {bounds[f'{demand}.HeatIn.Heat'][1]}, "
                    f"lower that wat is required for the maximum demand {max(target.values)}"
                )
            state = f"{demand}.Heat_demand"

            goals.append(TargetHeatGoal(state, target))
        return goals

    def goals(self):
        goals = super().goals().copy()
        # We do a minization of TCO consisting of CAPEX and OPEX over 25 years
        # CAPEX is based upon the boolean placement variables and the optimized maximum sizes
        # Note that CAPEX for geothermal and ATES is also dependent on the amount of doublets
        # In practice this means that the CAPEX is mainly driven by the peak day problem
        # The OPEX is based on the Source strategy which is computed on the __daily_avg variables
        # The OPEX thus is based on an avg strategy and discrepancies due to fluctuations intra-day
        # are possible.
        # The idea behind the two timelines is that the optimizer can make the OPEX vs CAPEX
        # trade-offs

        goals.append(MinimizeTCO(priority=2, number_of_years=self._number_of_years))

        return goals

    def constraints(self, ensemble_member):
        constraints = super().constraints(ensemble_member)

        for a in self.heat_network_components.get("ates", []):
            stored_heat = self.state_vector(f"{a}.Stored_heat")
            constraints.append(((stored_heat[-1] - stored_heat[0]), 0.0, np.inf))

        for b in self.heat_network_components.get("buffer", {}):
            vars = self.state_vector(f"{b}.Heat_buffer")
            symbol_stored_heat = self.state_vector(f"{b}.Stored_heat")
            constraints.append((symbol_stored_heat[self.__indx_max_peak], 0.0, 0.0))
            for i in range(len(self.times())):
                if i < self.__indx_max_peak or i > (self.__indx_max_peak + 23):
                    constraints.append((vars[i], 0.0, 0.0))

        return constraints

    def history(self, ensemble_member):
        return AliasDict(self.alias_relation)

    def __state_vector_scaled(self, variable, ensemble_member):
        canonical, sign = self.alias_relation.canonical_signed(variable)
        return (
            self.state_vector(canonical, ensemble_member) * self.variable_nominal(canonical) * sign
        )

    def solver_options(self):
        options = super().solver_options()
        options["casadi_solver"] = self._qpsol
        options["solver"] = "gurobi"
        gurobi_options = options["gurobi"] = {}
        gurobi_options["MIPgap"] = 0.02
        gurobi_options["threads"] = 4
        gurobi_options["LPWarmStart"] = 2

        return options

    def solver_success(self, solver_stats, log_solver_failure_as_error):
        success, log_level = super().solver_success(solver_stats, log_solver_failure_as_error)

        # Allow time-outs for CPLEX and CBC
        if (
            solver_stats["return_status"] == "time limit exceeded"
            or solver_stats["return_status"] == "stopped - on maxnodes, maxsols, maxtime"
        ):
            if self.objective_value > 1e10:
                # Quick check on the objective value. If no solution was
                # found, this is typically something like 1E50.
                return success, log_level

            return True, logging.INFO
        else:
            return success, log_level

    def priority_started(self, priority):
        self.__priority = priority
        self.__priority_timer = time.time()

        super().priority_started(priority)

    def priority_completed(self, priority):
        super().priority_completed(priority)

        self._hot_start = True

        time_taken = time.time() - self.__priority_timer
        self._priorities_output.append(
            (
                priority,
                time_taken,
                True,
                self.objective_value,
                self.solver_stats,
            )
        )

    def post(self):
        # In case the solver fails, we do not get in priority_completed(). We
        # append this last priority's statistics here in post().
        # TODO: check if we still need this small part of code below
        success, _ = self.solver_success(self.solver_stats, False)
        if not success:
            time_taken = time.time() - self.__priority_timer
            self._priorities_output.append(
                (
                    self.__priority,
                    time_taken,
                    False,
                    self.objective_value,
                    self.solver_stats,
                )
            )

        super().post()
        results = self.extract_results()
        parameters = self.parameters(0)
        # bounds = self.bounds()
        # Optimized ESDL
        self._write_updated_esdl()

        for d in self.heat_network_components.get("demand", []):
            realized_demand = results[f"{d}.Heat_demand"]
            target = self.get_timeseries(f"{d}.target_heat_demand").values
            timesteps = np.diff(self.get_timeseries(f"{d}.target_heat_demand").times)
            parameters[f"{d}.target_heat_demand"] = target.tolist()
            delta_energy = np.sum((realized_demand - target)[1:] * timesteps / 1.0e9)
            if delta_energy >= 1.0:
                logger.warning(f"For demand {d} the target is not matched by {delta_energy} GJ")

        if self.esdl_run_info_path is None:
            logger.warning(
                "Not writing results since no esdl path to write the files to is specified"
            )
            return

        root = self._get_runinfo_path_root()
        parameters_dict = dict()
        workdir = root.findtext("pi:outputResultsFile", namespaces=ns)
        if workdir is None:
            logger.error("No workdir specified, skipping writing results")
            return

        parameter_path = os.path.join(workdir, "parameters.json")
        for key, value in parameters.items():
            new_value = value  # [x for x in value]
            parameters_dict[key] = new_value
        if parameter_path is None:
            workdir = root.findtext("pi:workDir", namespaces=ns)
            parameter_path = os.path.join(workdir, "parameters.json")
            if not Path(workdir).is_absolute():
                parameter_path = Path(workdir).resolve().parent
                parameter_path = os.path.join(parameter_path.__str__() + "parameters.json")
        with open(parameter_path, "w") as file:
            json.dump(parameters_dict, fp=file)

        # root = self._get_runinfo_path_root()
        # bounds_dict = dict()
        # bounds_path = root.findtext("pi:outputResultsFile", namespaces=ns)
        # bounds_path = os.path.join(workdir, "bounds.json")
        # for key, value in bounds.items():
        #     if "Stored_heat" not in key:
        #         new_value = value  # [x for x in value]
        #         # if len(new_value) == 1:
        #         #     new_value = new_value[0]
        #         bounds_dict[key] = new_value
        # if bounds_path is None:
        #     workdir = root.findtext("pi:workDir", namespaces=ns)
        #     bounds_path = os.path.join(workdir, "bounds.json")
        #     if not Path(workdir).is_absolute():
        #         bounds_path = Path(workdir).resolve().parent
        #         bounds_path = os.path.join(bounds_path.__str__() + "bounds.json")
        # with open(bounds_path, "w") as file:
        #     json.dump(bounds_dict, fp=file)

        root = self._get_runinfo_path_root()
        results_path = root.findtext("pi:outputResultsFile", namespaces=ns)
        results_dict = dict()

        for key, values in results.items():
            new_value = values.tolist()
            if len(new_value) == 1:
                new_value = new_value[0]
            results_dict[key] = new_value

        results_path = os.path.join(workdir, "results.json")
        if results_path is None:
            workdir = root.findtext("pi:workDir", namespaces=ns)
            results_path = os.path.join(workdir, "results.json")
            if not Path(workdir).is_absolute():
                results_path = Path(workdir).resolve().parent
                results_path = os.path.join(results_path.__str__() + "results.json")
        with open(results_path, "w") as file:
            json.dump(results_dict, fp=file)


def connect_database():
    client = InfluxDBClient(
        host=DB_HOST, port=DB_PORT, username=DB_USER, password=DB_PASSWORD, database=DB_NAME
    )
    if DB_NAME not in client.get_list_database():
        client.create_database(DB_NAME)
    return client


def format_datetime(dt):
    date, time = dt.split(" ")
    day, month, year = date.split("-")
    ndate = year + "-" + month + "-" + day
    ntime = time + ":00+0000"
    return ndate + "T" + ntime


class EndScenarioSizingHIGHS(EndScenarioSizing):
    def post(self):
        super().post()

        self._write_updated_esdl()

    def solver_options(self):
        options = super().solver_options()
        options["casadi_solver"] = self._qpsol
        options["solver"] = "highs"
        highs_options = options["highs"] = {}
        highs_options["mip_rel_gap"] = 0.02

        options["gurobi"] = None

        return options


class EndScenarioSizingStaged(EndScenarioSizing):
    _stage = 0

    def __init__(self, stage=None, boolean_bounds=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._stage = stage
        self.__boolean_bounds = boolean_bounds

    def heat_network_options(self):
        options = super().heat_network_options()
        if self._stage == 1:
            options["neglect_pipe_heat_losses"] = True
            options["minimum_velocity"] = 0.0

        return options

    def solver_options(self):
        options = super().solver_options()
        options["solver"] = "gurobi"
        gurobi_options = options["gurobi"] = {}
        if self._stage == 1:
            gurobi_options["MIPgap"] = 0.005
        else:
            gurobi_options["MIPgap"] = 0.02
        gurobi_options["threads"] = 4
        gurobi_options["LPWarmStart"] = 2

        return options

    def bounds(self):
        bounds = super().bounds()

        if self._stage == 2:
            bounds.update(self.__boolean_bounds)

        return bounds


class EndScenarioSizingStagedHIGHS(EndScenarioSizingStaged):
    def solver_options(self):
        options = super().solver_options()
        options["casadi_solver"] = self._qpsol
        options["solver"] = "highs"
        highs_options = options["highs"] = {}
        if self._stage == 1:
            highs_options["mip_rel_gap"] = 0.005
        else:
            highs_options["mip_rel_gap"] = 0.02

        options["gurobi"] = None

        return options


class EndScenarioSizingCBC(EndScenarioSizing):
    def post(self):
        super().post()

        self._write_updated_esdl()

    def solver_options(self):
        options = super().solver_options()
        # options["casadi_solver"] = self._qpsol
        options["solver"] = "cbc"
        options["gurobi"] = None

        if options["solver"] == "cbc":
            options["hot_start"] = self._hot_start
            cbc_options = options["cbc"] = {}
            cbc_options["seconds"] = 300000.0

        return options


def run_end_scenario_sizing_no_heat_losses(
    end_scenario_problem_class,
    **kwargs,
):
    """
    This function is used to run end_scenario_sizing problem without heat losses. This is a
    simplification from the fully staged approach allowing users to more quickly iterate over
    results.

    Parameters
    ----------
    end_scenario_problem_class : The end scenario problem class.
    staged_pipe_optimization : Boolean to toggle between the staged or non-staged approach

    Returns
    -------

    """
    import time

    start_time = time.time()
    solution = run_optimization_problem(
        end_scenario_problem_class,
        stage=1,
        **kwargs,
    )

    print("Execution time: " + time.strftime("%M:%S", time.gmtime(time.time() - start_time)))

    return solution


def run_end_scenario_sizing(
    end_scenario_problem_class,
    staged_pipe_optimization=True,
    **kwargs,
):
    """
    This function is used to run end_scenario_sizing problem. There are a few variations of the
    same basic class. The main functionality this function adds is the staged approach, where
    we first solve without heat_losses, to then solve the same problem with heat losses but
    constraining the problem to only allow for the earlier found pipe classes and one size up.

    This staged approach is done to speed up the problem, as the problem without heat losses is
    much faster as it avoids inequality big_m constraints for the heat to discharge on pipes. The
    one size up possibility is to avoid infeasibilities in compensating for the heat losses.

    Parameters
    ----------
    end_scenario_problem_class : The end scenario problem class.
    staged_pipe_optimization : Boolean to toggle between the staged or non-staged approach

    Returns
    -------

    """
    import time

    boolean_bounds = {}

    start_time = time.time()
    if staged_pipe_optimization:
        solution = run_optimization_problem(
            end_scenario_problem_class,
            stage=1,
            **kwargs,
        )
        results = solution.extract_results()
        parameters = solution.parameters(0)

        # We give bounds for stage 2 by allowing one DN sizes larger than what was found in the
        # stage 1 optimization.
        pc_map = solution.get_pipe_class_map()
        for pipe_classes in pc_map.values():
            v_prev = 0.0
            first_pipe_class = True
            for var_name in pipe_classes.values():
                v = results[var_name][0]
                if first_pipe_class and abs(v) == 1.0:
                    boolean_bounds[var_name] = (abs(v), abs(v))
                elif abs(v) == 1.0:
                    boolean_bounds[var_name] = (0.0, abs(v))
                elif v_prev == 1.0:
                    boolean_bounds[var_name] = (0.0, 1.0)
                else:
                    boolean_bounds[var_name] = (abs(v), abs(v))
                v_prev = v
                first_pipe_class = False

        for asset in [
            *solution.heat_network_components.get("source", []),
            *solution.heat_network_components.get("buffer", []),
        ]:
            var_name = f"{asset}_aggregation_count"
            lb = results[var_name][0]
            ub = solution.bounds()[var_name][1]
            if round(lb) >= 1:
                boolean_bounds[var_name] = (lb, ub)

        t = solution.times()
        from rtctools.optimization.timeseries import Timeseries

        for p in solution.heat_network_components.get("pipe", []):
            if p in solution.hot_pipes and parameters[f"{p}.area"] > 0.0:
                lb = []
                ub = []
                for i in range(len(t)):
                    r = results[f"{p}__flow_direct_var"][i]
                    # bound to roughly represent 4km of heat losses in pipes
                    lb.append(
                        r if abs(results[f"{p}.Q"][i] / parameters[f"{p}.area"]) > 2.5e-2 else 0
                    )
                    ub.append(
                        r if abs(results[f"{p}.Q"][i] / parameters[f"{p}.area"]) > 2.5e-2 else 1
                    )

                boolean_bounds[f"{p}__flow_direct_var"] = (Timeseries(t, lb), Timeseries(t, ub))
                try:
                    r = results[f"{p}__is_disconnected"]
                    boolean_bounds[f"{p}__is_disconnected"] = (Timeseries(t, r), Timeseries(t, r))
                except KeyError:
                    pass

    solution = run_optimization_problem(
        end_scenario_problem_class,
        stage=2,
        boolean_bounds=boolean_bounds,
        **kwargs,
    )

    print("Execution time: " + time.strftime("%M:%S", time.gmtime(time.time() - start_time)))

    return solution


@main_decorator
def main(runinfo_path, log_level):
    logger.info("Run Scenario Sizing")

    kwargs = {
        "write_result_db_profiles": False,
        "influxdb_host": "localhost",
        "influxdb_port": 8086,
        "influxdb_username": None,
        "influxdb_password": None,
        "influxdb_ssl": False,
        "influxdb_verify_ssl": False,
    }
    # Temp comment for now
    # omotes-poc-test.hesi.energy
    # port 8086
    # user write-user
    # password nwn_write_test

    _ = run_optimization_problem(
        EndScenarioSizingHIGHS,
        esdl_run_info_path=runinfo_path,
        log_level=log_level,
        **kwargs,
    )
    # results = solution.extract_results()


if __name__ == "__main__":
    main()
