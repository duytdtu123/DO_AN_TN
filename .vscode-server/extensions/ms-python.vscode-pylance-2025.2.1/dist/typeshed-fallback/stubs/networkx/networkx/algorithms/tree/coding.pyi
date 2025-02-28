from networkx.exception import NetworkXException
from networkx.utils.backends import _dispatchable

class NotATree(NetworkXException): ...

@_dispatchable
def to_nested_tuple(T, root, canonical_form: bool = False): ...
@_dispatchable
def from_nested_tuple(sequence, sensible_relabeling: bool = False): ...
@_dispatchable
def to_prufer_sequence(T): ...
@_dispatchable
def from_prufer_sequence(sequence): ...
