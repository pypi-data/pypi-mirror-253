from pathlib import Path
from unittest import TestCase

import numpy as np

from rtctools.util import run_optimization_problem

from utils_tests import demand_matching_test, energy_conservation_test, heat_to_discharge_test


class TestVaryingTemperature(TestCase):
    def test_1a_temperature_variation(self):
        """
        This test is to check if the varying network temperature works as expected on a simple
        network. We give it temperature options such that it should select a minimum delta T to be
        able to meet the heat demands. It is known which network temperatures should be selected
        based on the specified input values.

        Checks:
        - Standard checks for demand matching, heat to discharge and energy conservation
        - Check expected supply temperature
        - Check expected return temperature

        Missing:
        - Check on integer variable for selected temperature.

        """
        import models.unit_cases.case_1a.src.run_1a as run_1a
        from models.unit_cases.case_1a.src.run_1a import HeatProblemTvar

        base_folder = Path(run_1a.__file__).resolve().parent.parent

        heat_problem = run_optimization_problem(HeatProblemTvar, base_folder=base_folder)

        # This optimization problem is to see whether the correct minimum delta temperaute is
        # chose by the optimization, minimum of 21 deg is needed, only the 85/60 option is
        # feasible, note that a maximum velocity is set low to achieve this.
        results = heat_problem.extract_results()

        test = TestCase()
        test.assertTrue(heat_problem.solver_stats["success"], msg="Optimisation did not succeed")
        # Check that the highest supply temperature is selected
        np.testing.assert_allclose(results[f"{3625334968694477359}_temperature"], 85.0)

        # Check that the lowest return temperature is selected
        np.testing.assert_allclose(results[f"{3625334968694477359000}_temperature"], 60.0)

        demand_matching_test(heat_problem, results)
        energy_conservation_test(heat_problem, results)
        heat_to_discharge_test(heat_problem, results)

    def test_3a_temperature_variation_supply(self):
        """
        Check varying temperature behoviour for network with storage (tank). In this case we
        Minimise the produced heat and thus we expect the lowest temperature to be selected.

        Checks:
        - Standard checks for demand matching, heat to discharge and energy conservation.
        - Check if the expected temperature is selected and if temperature variable is set
        correctly.

        """
        import models.unit_cases.case_3a.src.run_3a as run_3a
        from models.unit_cases.case_3a.src.run_3a import HeatProblemTvarsup

        base_folder = Path(run_3a.__file__).resolve().parent.parent

        heat_problem = run_optimization_problem(HeatProblemTvarsup, base_folder=base_folder)

        test = TestCase()
        test.assertTrue(heat_problem.solver_stats["success"], msg="Optimisation did not succeed")

        # optimization with two choices in supply temp 80 and 120 deg
        # lowest temperature should be selected because of lower heat losses and
        # heat production minimization goal
        results = heat_problem.extract_results()

        # Check whehter the heat demand is matched
        for d in heat_problem.heat_network_components.get("demand", []):
            target = heat_problem.get_timeseries(f"{d}.target_heat_demand").values[
                : len(heat_problem.times())
            ]
            np.testing.assert_allclose(target, results[f"{d}.Heat_demand"])

        # Check that the lowest temperature (80.0) is the outputted temperature
        np.testing.assert_allclose(results[f"{4195016129475469474608}_temperature"], 80.0)
        # Verify that also the integer is correctly set
        np.testing.assert_allclose(results[f"{4195016129475469474608}_80.0"], 1.0)
        np.testing.assert_allclose(results[f"{4195016129475469474608}_120.0"], 0.0)

        demand_matching_test(heat_problem, results)
        energy_conservation_test(heat_problem, results)
        heat_to_discharge_test(heat_problem, results)

    def test_3a_temperature_variation_return(self):
        """
        Check varying temperature behoviour for network with storage (tank). In this case we
        Minimise the flow at the producer, and thus we expect the lowest temperature to be selected
        to maximise the detla T.

        Checks:
        - Standard checks for demand matching, heat to discharge and energy conservation.
        - Check if the expected temperature is selected and if temperature variable is set
        correctly.

        Missing:
        - I think there is a double demand mathcing check now...

        """
        import models.unit_cases.case_3a.src.run_3a as run_3a
        from models.unit_cases.case_3a.src.run_3a import HeatProblemTvarret

        base_folder = Path(run_3a.__file__).resolve().parent.parent

        heat_problem = run_optimization_problem(HeatProblemTvarret, base_folder=base_folder)

        test = TestCase()
        test.assertTrue(heat_problem.solver_stats["success"], msg="Optimisation did not succeed")

        # optimization with two choices in return temp 30 and 40 deg
        # lowest temperature should be selected because of larger dT causing lowest flow rates
        # and we apply source Q minimization goal
        results = heat_problem.extract_results()

        # Check whehter the heat demand is matched
        for d in heat_problem.heat_network_components.get("demand", []):
            target = heat_problem.get_timeseries(f"{d}.target_heat_demand").values[
                : len(heat_problem.times())
            ]
            np.testing.assert_allclose(target, results[f"{d}.Heat_demand"])

        # Check that the lowest temperature (30.0) is the outputted temperature
        np.testing.assert_allclose(results[f"{4195016129475469474608000}_temperature"], 30.0)
        # Verify that also the integer is correctly set
        np.testing.assert_allclose(results[f"{4195016129475469474608000}_30.0"], 1.0)
        np.testing.assert_allclose(results[f"{4195016129475469474608000}_40.0"], 0.0)

        demand_matching_test(heat_problem, results)
        energy_conservation_test(heat_problem, results)
        heat_to_discharge_test(heat_problem, results)

    def test_hex_temperature_variation(self):
        """
        This test is to check whether the heat exchanger behaves as expected when optimized under
        varying network temperature. This is of special interest as we want to ensure the
        temperatures stay physically feasible, therefore we create a problem where the lowest
        available supply T is infeasible.

        Checks:
        - Standard checks for demand matching, heat to discharge and energy conservation.
        - Check that the infeasible temperature is not selected.

        """
        import models.heat_exchange.src.run_heat_exchanger as run_heat_exchanger
        from models.heat_exchange.src.run_heat_exchanger import HeatProblemTvar

        base_folder = Path(run_heat_exchanger.__file__).resolve().parent.parent

        heat_problem = run_optimization_problem(HeatProblemTvar, base_folder=base_folder)

        test = TestCase()
        test.assertTrue(heat_problem.solver_stats["success"], msg="Optimisation did not succeed")

        # optimization with three choices of primary supply temperature of which the lowest is
        # infeasible. Therefore optimization should select second lowest option of 80.
        # lowest feasible temperature should be selected due to heatlosses and the minimization
        # goal of the sources
        results = heat_problem.extract_results()

        # Check that the lowest feasible temperature (80.0) is the outputted temperature and not
        # the 69 which is below the secondary side supply temperature
        np.testing.assert_allclose(results[f"{33638164429859421}_temperature"], 80.0)
        # Verify that also the integer is correctly set
        np.testing.assert_allclose(results[f"{33638164429859421}_69.0"], 0.0)
        np.testing.assert_allclose(results[f"{33638164429859421}_80.0"], 1.0)
        np.testing.assert_allclose(results[f"{33638164429859421}_90.0"], 0.0)

        demand_matching_test(heat_problem, results)
        energy_conservation_test(heat_problem, results)
        heat_to_discharge_test(heat_problem, results)

    def test_hex_temperature_variation_disablehex(self):
        """
        This test is to check if the optimizer disables the heat exchanger when only infeasible
        temperature option are provided to it.

        Checks:
        - Standard checks for demand matching, heat to discharge and energy conservation.
        - Infeasible T for heat exchanger is selected.
        - Heat exchanger is disabled.

        """
        import models.heat_exchange.src.run_heat_exchanger as run_heat_exchanger
        from models.heat_exchange.src.run_heat_exchanger import HeatProblemTvarDisableHEX

        base_folder = Path(run_heat_exchanger.__file__).resolve().parent.parent

        heat_problem = run_optimization_problem(HeatProblemTvarDisableHEX, base_folder=base_folder)
        # FIXME: apparantly there is a conflict in the constraints for the is_disabled_hex
        test = TestCase()
        test.assertTrue(heat_problem.solver_stats["success"], msg="Optimisation did not succeed")

        # optimization with only one option in temperature which is infeasible for the hex.
        # therefore optimization should disable the heat exchanger
        results = heat_problem.extract_results()

        # Check that the problem has an infeasible temperature for the hex
        np.testing.assert_allclose(results[f"{33638164429859421}_temperature"], 69.0)
        # Verify that the hex is disabled
        np.testing.assert_allclose(results["HeatExchange_39ed__disabled"], 1.0)
        np.testing.assert_allclose(results["HeatExchange_39ed.Primary_heat"], 0.0)

        demand_matching_test(heat_problem, results)
        energy_conservation_test(heat_problem, results)
        heat_to_discharge_test(heat_problem, results)

    def test_hex_temperature_variation_secondary(self):
        """
        Check to see the functioning of the varying network temperature with a heat exchanger where
        all options are feasible and we expect it to take the most advantageous one, which in this
        case is the lowest one.

        Checks:
        - Standard checks for demand matching, heat to discharge and energy conservation.
        - Check that lowest temperature is selected and set correctly.

        """
        import models.heat_exchange.src.run_heat_exchanger as run_heat_exchanger
        from models.heat_exchange.src.run_heat_exchanger import HeatProblemTvarSecondary

        base_folder = Path(run_heat_exchanger.__file__).resolve().parent.parent

        heat_problem = run_optimization_problem(HeatProblemTvarSecondary, base_folder=base_folder)

        test = TestCase()
        test.assertTrue(heat_problem.solver_stats["success"], msg="Optimisation did not succeed")

        # optimization with two choices in secondary supply temp 70 and 90 deg
        # lowest temperature should be selected because of heat minimization and lower T has
        # lower heat loss.
        results = heat_problem.extract_results()

        # Check that the lowest temperature (70.0) is the outputted temperature
        np.testing.assert_allclose(results[f"{7212673879469902607010}_temperature"], 70.0)
        # Verify that also the integer is correctly set
        np.testing.assert_allclose(results[f"{7212673879469902607010}_70.0"], 1.0)
        np.testing.assert_allclose(results[f"{7212673879469902607010}_90.0"], 0.0)

        demand_matching_test(heat_problem, results)
        energy_conservation_test(heat_problem, results)
        heat_to_discharge_test(heat_problem, results)

    # Note that CBC struggles heavily and tends to crash, therefore excluded from pipeline
    # def test_varying_temperature_with_pipe_sizing(self):
    #     root_folder = str(Path(__file__).resolve().parent.parent)
    #     import sys
    #     sys.path.insert(1, root_folder)
    #
    #     import examples.pipe_diameter_sizing.src.example  # noqa: E402, I100
    #     from examples.pipe_diameter_sizing.src.example import (
    #         PipeDiameterSizingProblemTvar,
    #     )  # noqa: E402, I100
    #
    #     base_folder = (
    #         Path(examples.pipe_diameter_sizing.src.example.__file__).resolve().parent.parent
    #     )
    #
    #     del root_folder
    #     sys.path.pop(1)
    #
    #     # The optimization should select the highest delta-temperature as
    #     # this minimizes the length
    #     # times diameter cost function
    #
    #     # problem = run_optimization_problem(
    #     PipeDiameterSizingProblemTvar, base_folder=base_folder)
    #     # results = problem.extract_results()
    #
    #
    #     # # Check that the highest supply temperature is selected
    #     # np.testing.assert_allclose(
    #     results[f"{761602374459208051248}__supply_temperature"], 90.0)
    #     #
    #     # # Check that the lowest return temperature is selected
    #     # np.testing.assert_allclose(
    #     results[f"{761602374459208051248000}__return_temperature"], 30.0)
