from tsproc.context import Context
from tsproc.modules import Process, Module


class TestProcess(Process):
    pass


class TestSubProcess(Process):
    pass


class TestContext(Context):
    def __init__(self):
        super().__init__()
        self.number = 0


class TestModule(Module):

    def run(self, context: TestContext):
        context.number += 1
