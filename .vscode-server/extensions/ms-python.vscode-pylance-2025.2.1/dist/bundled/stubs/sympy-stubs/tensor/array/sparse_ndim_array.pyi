from typing import Any
from typing_extensions import Self

from sympy import Indexed
from sympy.matrices import SparseMatrix
from sympy.tensor.array.mutable_ndim_array import MutableNDimArray
from sympy.tensor.array.ndim_array import ImmutableNDimArray, NDimArray

class SparseNDimArray(NDimArray):
    def __new__(self, *args, **kwargs) -> ImmutableSparseNDimArray: ...
    def __getitem__(self, index) -> Indexed | Self: ...
    @classmethod
    def zeros(cls, *shape) -> Self: ...
    def tomatrix(self) -> SparseMatrix: ...
    def reshape(self, *newshape) -> Self: ...

class ImmutableSparseNDimArray(SparseNDimArray, ImmutableNDimArray):
    def __new__(cls, iterable=..., shape=..., **kwargs) -> Self: ...
    def __setitem__(self, index, value): ...
    def as_mutable(self) -> MutableSparseNDimArray: ...

class MutableSparseNDimArray(MutableNDimArray, SparseNDimArray):
    def __new__(cls, iterable=..., shape=..., **kwargs) -> Self: ...
    def __setitem__(self, index, value) -> None: ...
    def as_immutable(self) -> ImmutableSparseNDimArray: ...
    @property
    def free_symbols(self) -> set[Any]: ...
