import math

import numpy as np
from numpy.typing import ArrayLike, NDArray

from ...gloo import IndexBuffer, Texture2D, VertexBuffer
from .array_list import ArrayList
from .collection import Collection
from .util import dtype_reduce

# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2014, Nicolas P. Rougier
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------

def next_power_of_2(n): ...

class Item(object):
    def __init__(
        self,
        parent: Collection,
        key: int,
        vertices: ArrayLike,
        indices: ArrayLike,
        uniforms: ArrayLike,
    ): ...
    @property
    def vertices(self): ...
    @vertices.setter
    def vertices(self, data): ...
    @property
    def indices(self): ...
    @indices.setter
    def indices(self, data): ...
    @property
    def uniforms(self): ...
    @uniforms.setter
    def uniforms(self, data): ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, value): ...
    def __str__(self): ...

class BaseCollection(object):
    def __init__(self, vtype, utype=None, itype=None): ...
    def __len__(self): ...
    @property
    def vtype(self): ...
    @property
    def itype(self): ...
    @property
    def utype(self): ...
    def append(
        self,
        vertices: NDArray,
        uniforms: NDArray | None = None,
        indices: NDArray | None = None,
        itemsize: int | tuple | ArrayLike | None = None,
    ): ...
    def __delitem__(self, index): ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, data): ...
    def _compute_texture_shape(self, size=1): ...
    def _update(self): ...
