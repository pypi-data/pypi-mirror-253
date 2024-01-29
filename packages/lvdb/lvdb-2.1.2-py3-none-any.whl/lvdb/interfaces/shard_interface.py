import abc

import numpy.typing as npt


class ShardInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'insert') and
                callable(subclass.insert) and
                hasattr(subclass, 'delete') and
                callable(subclass.delete) and
                hasattr(subclass, 'get_data') and
                callable(subclass.get_data) or
                NotImplemented)

    @abc.abstractmethod
    def insert(self, vector: npt.NDArray):
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, vector: npt.NDArray, first: bool):
        raise NotImplementedError

    @abc.abstractmethod
    def get_data(self, partial: bool, lo: float, hi: float):
        raise NotImplementedError