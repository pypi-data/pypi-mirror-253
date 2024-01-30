from typing import Any, List
from ..ir import FkNode, FkGraph, FkVar
import re


class FkAnyPatternNode(FkNode):
    def vis_label(self):
        name = ""
        for k, v in self.attr_eq.items():
            name = f"{name}|{k}={v}"
        for k in self.attr_has:
            name = f"{name}|{k}"
        for k in self.attr_nhas:
            name = f"{name}|!{k}"
        if name.startswith("|"):
            name = name[1:]
        if len(name) == 0:
            name = "*"
        return name

    def __init__(self, attr_eq=dict(), attr_has=tuple(), attr_nhas=tuple()) -> None:
        super().__init__()
        self.attr_eq = attr_eq.copy()
        self.attr_has = attr_has.copy()
        self.attr_nhas = attr_nhas.copy()

    def eq(self, obj: FkNode) -> bool:
        for k in self.attr_has:
            if k not in obj._attr:
                return False
        for k, v in obj._attr.items():
            if k in self.attr_nhas:
                return False
            if k in self.attr_eq:
                if v != self.attr_eq[k]:
                    return False
        return True


class FkPatternBuilder:
    def __init__(self) -> None:
        self._inputs = []
        self._attr_eq = {}
        self._attr_has = []
        self._attr_nhas = []
        self._node = None

    def attr_has(self, k):
        self._attr_has.append(k)
        return self

    def attr_nhas(self, k):
        self._attr_nhas.append(k)
        return self

    def attr_eq(self, k, v):
        self._attr_eq[k] = v
        return self

    def __call__(self, *args: Any) -> Any:
        for arg in args:
            assert isinstance(arg, FkPatternBuilder)
        self._inputs = args
        return self

    def gen_pattern_node(self):
        if self._node is None:
            self._node = FkAnyPatternNode(
                self._attr_eq,
                self._attr_has,
                self._attr_nhas,
            )
        return self._node


class FkPatternRet(FkGraph):
    def __init__(self, map, graph) -> None:
        super().__init__()
        self._map = map
        for v in map.values():
            self.add_node(v)
        self.inputs = self.subgraph_inputs(list(map.values()))
        self.outputs = self.subgraph_outputs(list(map.values()))
        self._src_graph = graph

    @property
    def base_graph(self):
        return self._src_graph

    def corresponding(self, obj):
        if isinstance(obj, FkPatternBuilder):
            obj = obj._node
        assert obj is not None
        return self._map.get(obj, None)

    def sync_add_node(self, node):
        assert isinstance(node, FkNode)
        self._src_graph.add_node(node)
        self.add_node(node)
        return node

    def sync_remove_node(self, node):
        assert isinstance(node, FkNode)
        self._src_graph.remove_node(node)
        self.remove_node(node)
        return node


class FkPattern:
    def __init__(self, patterns: List[FkPatternBuilder]) -> None:
        self._graph = FkGraph()

        var_map_to_node = {}
        this_rank = [patterns] if isinstance(patterns, FkPatternBuilder) else patterns
        next_rank = []
        while len(this_rank) != 0:
            for pattern in this_rank:
                node = pattern.gen_pattern_node()
                self._graph.add_node(node)
                for i in pattern._inputs:
                    assert isinstance(i, FkPatternBuilder)
                    if i in var_map_to_node:
                        iv = var_map_to_node[i]
                    else:
                        iv = FkVar(i)
                        var_map_to_node[i] = iv
                    node.add_input(iv)
                    next_rank.append(i)
                if pattern in var_map_to_node:
                    ov = var_map_to_node[pattern]
                    node.add_output(ov)
            this_rank = next_rank
            next_rank = []
        self._graph.inputs = self._graph.subgraph_inputs(self._graph.nodes)
        self._graph.outputs = self._graph.subgraph_outputs(self._graph.nodes)

    @property
    def graph(self):
        return self._graph

    def extract(self, graph: FkGraph):
        from networkx.algorithms import isomorphism

        def node_match(n1, n2):
            return n2["obj"].eq(n1["obj"])

        g1 = graph.to_networkx()
        g2 = self._graph.to_networkx()
        GM = isomorphism.GraphMatcher(g1, g2, node_match=node_match)
        subgraphs = []
        for subgraph in GM.subgraph_isomorphisms_iter():
            subgraphs.append(
                FkPatternRet(
                    {
                        g2.nodes[v]["obj"]: g1.nodes[k]["obj"]
                        for k, v in subgraph.items()
                    },
                    graph,
                )
            )
        return subgraphs
