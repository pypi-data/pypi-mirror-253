import sys
from pathlib import Path
from unittest import TestCase

from rtctools.util import run_optimization_problem

from utils_tests import demand_matching_test, energy_conservation_test, heat_to_discharge_test


class TestPipeDiameterSizingExample(TestCase):
    def test_half_network_gone(self):
        """
        This test is to check if the optimization behaves as expected under pipe class optimization.
        The test uses a symmetrical network with three demands in the middle that can be provided
        from a source both left and right. The optimal solution is that the optimizer only uses
        the left source and the associated left pipes.

        Checks:
        - Standard checks for demand matching, heat to discharge and energy conservation
        - That expected pipes are removed

        Missing:
        - Use the optional as state for the pipes in the esdl.
        - Check that the Q is under the max.
        - Check that head losses are as expected for the selected diameter
        - Check that head loss equals zero for removed pipes
        - Same for hydraulic power, no idea why it is outcommented

        """
        root_folder = str(Path(__file__).resolve().parent.parent)
        sys.path.insert(1, root_folder)

        import examples.pipe_diameter_sizing.src.example  # noqa: E402, I100
        from examples.pipe_diameter_sizing.src.example import (
            PipeDiameterSizingProblem,
        )  # noqa: E402, I100

        base_folder = (
            Path(examples.pipe_diameter_sizing.src.example.__file__).resolve().parent.parent
        )

        del root_folder
        sys.path.pop(1)

        problem = run_optimization_problem(PipeDiameterSizingProblem, base_folder=base_folder)

        parameters = problem.parameters(0)
        diameters = {p: parameters[f"{p}.diameter"] for p in problem.hot_pipes}
        results = problem.extract_results()

        # Check that half the network is removed, i.e. 4 pipes. Note that it
        # is equally possible for the left or right side of the network to be
        # removed.
        self.assertEqual(
            len([d for d in diameters.values() if d == 0.0]),
            4,
            "More/less than 4 pipes have been removed",
        )
        # Check that the correct/specific 4 pipes on the left or 4 on the right have been removed
        pipes_removed = ["Pipe_8592", "Pipe_2927", "Pipe_9a6f", "Pipe_a718"]
        pipes_remained = ["Pipe_96bc", "Pipe_51e4", "Pipe_6b39", "Pipe_f9b0"]
        self.assertTrue(
            all(
                (elem in [k for k, d in diameters.items() if (d == 0.0)] for elem in pipes_remained)
            )
            or all(
                elem in [k for k, d in diameters.items() if (d == 0.0)] for elem in pipes_removed
            ),
            "The incorrect 4 pipes have been removed",
        )
        # Ensure that the removed pipes do not have predicted hydraulic power values
        hydraulic_power_sum = 0.0
        for pipe in diameters.keys():
            if pipe in pipes_removed:
                hydraulic_power_sum += sum(abs(results[f"{pipe}.Hydraulic_power"]))
        # self.assertEqual(hydraulic_power_sum, 0.0, "Hydraulic power exists for a removed pipe")

        # Hydraulic power = delta pressure * Q = f(Q^3), where delta pressure = f(Q^2)
        # The linear approximation of the 3rd order function should overestimate the hydraulic
        # power when compared to the product of Q and the linear approximation of 2nd order
        # function (delta pressure).
        hydraulic_power_sum = 0.0
        hydraulic_power_post_process = 0.0
        for pipe in diameters.keys():
            if pipe in pipes_remained:
                hydraulic_power_sum += sum(abs(results[f"{pipe}.Hydraulic_power"]))
                hydraulic_power_post_process += sum(
                    abs(
                        results[f"{pipe}.dH"]
                        * parameters[f"{pipe}.rho"]
                        * 9.81
                        * results[f"{pipe}.HeatOut.Q"]
                    )
                )

        # self.assertGreater(hydraulic_power_sum, hydraulic_power_post_process)
        demand_matching_test(problem, results)
        energy_conservation_test(problem, results)
        heat_to_discharge_test(problem, results)


if __name__ == "__main__":
    import time

    start_time = time.time()
    a = TestPipeDiameterSizingExample()
    a.test_half_network_gone()
    print("Execution time: " + time.strftime("%M:%S", time.gmtime(time.time() - start_time)))
