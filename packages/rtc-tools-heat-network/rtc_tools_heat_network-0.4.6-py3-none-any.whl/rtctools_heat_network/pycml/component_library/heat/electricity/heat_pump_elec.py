from rtctools_heat_network.pycml.component_library.heat.electricity.electricity_base import (
    ElectricityPort,
)
from rtctools_heat_network.pycml.component_library.heat.heat_pump import HeatPump


# TODO: for now in the electricity folder, but maybe we can make a multicommodity folder,
# where this is then placed.
class HeatPumpElec(HeatPump):
    """
    The heat pump elec is to model a water-water heatpump where we explicitly model its connection
    to the electricity grid. This allows to potentially optimize for electricity network constraints
    in the optimization of the heat network and vice-versa.
    """

    def __init__(self, name, **modifiers):
        super().__init__(
            name,
            **self.merge_modifiers(
                dict(),
                modifiers,
            ),
        )

        # TODO: potentially we can keep the component type as heat_pump and set subcomponent to
        # heat_pump_elec, first need to check if there wouldn't be anything conflicting then.
        self.component_type = "heat_pump_elec"
        self.min_voltage = 1.0e4

        self.add_variable(ElectricityPort, "ElectricityIn")
        self.add_equation(((self.ElectricityIn.Power - self.Power_elec) / self.elec_power_nominal))
