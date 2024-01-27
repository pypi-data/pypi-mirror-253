from pathlib import Path
from unittest import TestCase

import numpy as np

from rtctools.util import run_optimization_problem

from rtctools_heat_network.head_loss_class import HeadLossOption


class TestHeadLossCalculation(TestCase):
    def test_scalar_return_type(self):
        """
        Check whether the _hn_pipe_head_loss() method of head loss mixin
        behaves like expected. Meaning that it is checked whether it returns the expected types
        given the variations of input types, namely float and numpy array.

        Missing:
        Model should be replaced with esdl model.
        Check whether the returned scalar had the expected value.
        """
        import models.basic_source_and_demand.src.heat_comparison as heat_comparison
        from models.basic_source_and_demand.src.heat_comparison import HeatPython

        class Model(HeatPython):
            def __init__(self, head_loss_option, *args, **kwargs):
                self.__head_loss_option = head_loss_option
                super().__init__(*args, **kwargs)

            def _hn_get_pipe_head_loss_option(self, *args, **kwargs):
                return self.__head_loss_option

            def optimize(self):
                # Just pre, we don't care about anything else
                self.pre()

        base_folder = Path(heat_comparison.__file__).resolve().parent.parent

        for h in [
            HeadLossOption.LINEAR,
            HeadLossOption.CQ2_INEQUALITY,
            HeadLossOption.LINEARIZED_DW,
        ]:
            m = run_optimization_problem(Model, head_loss_option=h, base_folder=base_folder)

            options = m.heat_network_options()
            parameters = m.parameters(0)

            ret = m._head_loss_class._hn_pipe_head_loss("pipe_hot", m, options, parameters, 0.1)
            self.assertIsInstance(ret, float)

            ret = m._head_loss_class._hn_pipe_head_loss(
                "pipe_hot", m, options, parameters, np.array([0.1])
            )
            self.assertIsInstance(ret, np.ndarray)
            self.assertEqual(len(ret), 1)

            ret = m._head_loss_class._hn_pipe_head_loss(
                "pipe_hot", m, options, parameters, np.array([0.05, 0.1, 0.2])
            )
            self.assertIsInstance(ret, np.ndarray)
            self.assertEqual(len(ret), 3)


# TODO: testing of head loss should be relooked
# class TestHeadLossOptions(TestCase):
#     def test_no_head_loss_mixing_options(self):
#         """
#         This test is to check whether the optimization fails as expected when a conflicting
#         configuration is provided for head loss options. This is achieved by overriding the
#         _hn_get_pipe_head_loss_option() method.

#         Missing:
#         Model should be replaced with esdl model.
#         Not sure if this test is the most effective... Seems to me like we might want remove the
#         _hn_get_pipe_head_loss_option() method all together as we are never using it and it is
#         adding quite some code complexity and not good for transparency.

#         """
#         import models.basic_source_and_demand.src.heat_comparison as heat_comparison
#         from models.basic_source_and_demand.src.heat_comparison import HeatPython

#         base_folder = Path(heat_comparison.__file__).resolve().parent.parent

#         class Model(HeatPython):
#             def heat_network_options(self):
#                 options = super().heat_network_options()
#                 options["head_loss_option"] = HeadLossOption.LINEAR
#                 return options

#             def _hn_get_pipe_head_loss_option(self, *args, **kwargs):
#                 return HeadLossOption.NO_HEADLOSS

#         with self.assertRaisesRegex(
#             Exception, "Mixing .NO_HEADLOSS with other head loss options is not allowed"
#         ):
#             run_optimization_problem(Model, base_folder=base_folder)
