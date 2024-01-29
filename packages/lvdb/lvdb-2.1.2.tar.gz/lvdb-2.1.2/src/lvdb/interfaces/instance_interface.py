import abc
from typing import Optional

import numpy.typing as npt


class InstanceInterface(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'add') and
                callable(subclass.add) and
                hasattr(subclass, 'delete') and
                callable(subclass.delete) and
                hasattr(subclass, 'query_norm_range') and
                callable(subclass.query_norm_range) or
                NotImplemented)

    @abc.abstractmethod
    def add(self, vector) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, vector, first: Optional[bool] = True) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def query_vector_range(self, left_bound: npt.NDArray, right_bound: npt.NDArray):
        raise NotImplementedError

    @abc.abstractmethod
    def query_norm_range(self, lower_norm: float, upper_norm: float):
        raise NotImplementedError