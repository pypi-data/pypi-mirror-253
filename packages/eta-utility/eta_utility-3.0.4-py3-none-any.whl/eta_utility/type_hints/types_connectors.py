from __future__ import annotations

from typing import AbstractSet, Sequence, Set, Union

from eta_utility.connectors.node import (
    Node,
    NodeCumulocity,
    NodeEnEffCo,
    NodeEntsoE,
    NodeLocal,
    NodeModbus,
    NodeOpcUa,
)

AnyNode = Union[Node, NodeLocal, NodeModbus, NodeOpcUa, NodeEnEffCo, NodeEntsoE, NodeCumulocity]
Nodes = Union[Sequence[AnyNode], Set[AnyNode], AbstractSet[AnyNode], AnyNode]
