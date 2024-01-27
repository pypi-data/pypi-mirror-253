from pathlib import Path
from unittest import TestCase

import numpy as np


from rtctools.util import run_optimization_problem


class TestMILPGasSourceSink(TestCase):
    def test_source_sink(self):
        """
        Test case for a network consisting out of a source, pipes and a sink

        Checks:
        - That flow is maintained.
        - That the head drops over the pipe.

        """
        import models.unit_cases_gas.source_sink.src.run_source_sink as example
        from models.unit_cases_gas.source_sink.src.run_source_sink import GasProblem

        base_folder = Path(example.__file__).resolve().parent.parent

        results = run_optimization_problem(GasProblem, base_folder=base_folder).extract_results()

        # Test if mass conserved
        np.testing.assert_allclose(
            results["GasProducer_0876.GasOut.Q"], results["GasDemand_a2d8.GasIn.Q"]
        )

        # Test if head is going down
        np.testing.assert_array_less(results["Pipe_4abc.GasOut.H"], results["Pipe_4abc.GasIn.H"])
