import abc


class Context(abc.ABC):

    def __repr__(self):
        class_name = self.__class__.__name__
        properties = ", ".join(f"{key}={value}" for key, value in vars(self).items())
        return f"{class_name}({properties})"
