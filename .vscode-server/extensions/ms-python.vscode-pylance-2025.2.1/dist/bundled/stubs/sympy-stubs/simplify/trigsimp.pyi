from typing import Any

from sympy.core.basic import Basic
from sympy.series.order import Order

def trigsimp_groebner(expr, hints=..., quick=..., order=..., polynomial=...) -> Order | Any: ...

_trigs = ...

def trigsimp(expr, inverse=..., **opts) -> Any: ...
def exptrigsimp(expr) -> Order: ...
def trigsimp_old(expr, *, first=..., **opts): ...

_trigpat = ...
_idn = ...
_midn = ...
_one = ...

def futrig(e, *, hyper=..., **kwargs) -> Basic | Order: ...
