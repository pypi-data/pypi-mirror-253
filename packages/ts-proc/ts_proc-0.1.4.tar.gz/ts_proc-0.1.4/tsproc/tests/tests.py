import unittest

from tsproc.tests.test_process import TestProcess, TestContext, TestModule, TestSubProcess


class TestProcesses(unittest.TestCase):

    def test_process(self):
        modules = (
            TestModule(),
            TestSubProcess(modules=(TestModule(), TestModule())),
            TestModule(),
        )
        context = TestContext()
        p = TestProcess(modules=modules)
        p.run(context=context)
        self.assertEqual(context.number, 4)
        self.assertEqual(context.number, len(p))
