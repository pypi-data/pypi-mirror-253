import unittest
from functools import partial
from unittest.mock import MagicMock

from cloudshell.shell.standards.pdu.driver_interface import PDUResourceDriverInterface


class TestDriverInterface(unittest.TestCase):
    def test_interface_is_abstract(self):
        with self.assertRaisesRegex(TypeError, "abstract"):
            PDUResourceDriverInterface()

    def test_interface_have_all_methods(self):
        intr_has_attr = partial(hasattr, PDUResourceDriverInterface)
        self.assertTrue(intr_has_attr("get_inventory"))
        self.assertTrue(intr_has_attr("PowerOn"))
        self.assertTrue(intr_has_attr("PowerOff"))
        self.assertTrue(intr_has_attr("PowerCycle"))

    def test_abstract_methods_return_none(self):
        class TestedClass(PDUResourceDriverInterface):
            def get_inventory(self, context):
                return super().get_inventory(context)

            def PowerOn(self, context, ports):
                return super().PowerOn(context, ports)

            def PowerOff(self, context, ports):
                return super().PowerOff(context, ports)

            def PowerCycle(self, context, ports, delay):
                return super().PowerCycle(context, ports, delay)

        inst = TestedClass()
        arg = MagicMock()
        self.assertIsNone(inst.get_inventory(arg))
        self.assertIsNone(inst.PowerOn(arg, arg))
        self.assertIsNone(inst.PowerOff(arg, arg))
        self.assertIsNone(inst.PowerCycle(arg, arg, arg))
