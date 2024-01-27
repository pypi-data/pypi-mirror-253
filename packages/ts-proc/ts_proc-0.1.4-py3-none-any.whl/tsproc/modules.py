import abc
import typing

from tsproc.context import Context


class Module(abc.ABC):

    def __init__(self):
        pass

    @abc.abstractmethod
    def run(self, context: Context):
        pass

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"{class_name}"

    def __len__(self):
        return 1


class Process(Module):

    def __init__(self, modules: typing.Tuple[Module, ...]):
        super().__init__()
        self._modules = modules

    @property
    def modules(self):
        return self._modules

    # TODO python 3.8 add @final
    def run(self, context: Context):
        for module in self:
            module.run(context=context)

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"{class_name}({[m for m in self]})"

    def __len__(self):
        return sum(len(m) for m in self)

    def __getitem__(self, index):
        return self._modules[index]
