from typing import List
from .node import FkNode
from collections import deque


class FkGraph(FkNode):
    def __init__(self, unqn=None, allow_str_io=True) -> None:
        if unqn is None:
            unqn = self.get_default_unqn("graph")

        super().__init__(unqn=unqn, isolation=True, allow_str_io=allow_str_io)

        self._nodes: List[FkNode] = []

    @property
    def nodes(self):
        return self._nodes[:]

    def add_node(self, node):
        assert isinstance(node, FkNode)
        self._nodes.append(node)
        return node

    def remove_node(self, node):
        assert isinstance(node, FkNode)
        node.inputs = []
        node.outputs = []
        self._nodes.remove(node)
        return node

    def merge_var_by(self, key, keep_all_attr=True):
        var_map = {}

        def deal_io(obj, attr):
            io_list = []
            for i in getattr(obj, attr):
                assert hasattr(i, key)
                attr_v = getattr(i, key)
                if attr_v not in var_map:
                    var_map[attr_v] = i
                    io_list.append(i)
                else:
                    v = var_map[attr_v]
                    if keep_all_attr:
                        v._attr.update(i._attr)
                    io_list.append(v)
            if io_list != getattr(obj, attr):
                setattr(obj, attr, io_list)

        for n in self.nodes:
            deal_io(n, "inputs")
            deal_io(n, "outputs")

    @property
    def roots(self):
        root = []
        for node in self.nodes:
            prenode_nb = sum([len(i.srcs) for i in node.inputs])
            if prenode_nb == 0:
                root.append(node)
        return root

    def to_networkx(self):
        import networkx as nx

        G = nx.DiGraph()
        for node in self.nodes:
            G.add_node(node.unqn, obj=node, label=node.vis_label())
            # print(node.unqn, node._attr)
            for i in node.inputs:
                for src in i.srcs:
                    # print(src.unqn, '->', node.unqn)
                    G.add_edge(src.unqn, node.unqn, obj=i)
        return G

    def to_img(self, path):
        import networkx as nx

        g = self.to_networkx()
        gv = nx.nx_agraph.to_agraph(g)
        for n in gv.nodes():
            n.attr["label"] = g.nodes[n.name]["label"]
        gv.draw(path, prog="dot")

    @staticmethod
    def subgraph_inputs(nodes):
        inputs = []
        for n in nodes:
            for i in n.inputs:
                assert len(i.srcs) <= 1
                for src in i.srcs:
                    if src not in nodes:
                        inputs.append(i)
        return inputs

    @staticmethod
    def subgraph_outputs(nodes):
        outputs = []
        for n in nodes:
            for o in n.outputs:
                for on in o.dsts:
                    if on not in nodes:
                        outputs.append(o)
                        break
        return outputs

    @staticmethod
    def graph_inputs(nodes):
        inputs = []
        for node in nodes:
            for i in node.inputs:
                if len(i.srcs) == 0:
                    inputs.append(i)
        return inputs

    @staticmethod
    def graph_outputs(nodes):
        outputs = []
        for node in nodes:
            for o in node.outputs:
                if len(o.dsts) == 0:
                    outputs.append(o)
        return outputs

    def replace(self, src_nodes, dst_nodes):
        # src_subgraph_inputs = self.subgraph_inputs(src_nodes)
        src_subgraph_outputs = self.subgraph_outputs(src_nodes)
        # dst_subgraph_inputs = self.subgraph_inputs(dst_nodes)
        dst_subgraph_outputs = self.subgraph_outputs(dst_nodes)
        for o in src_subgraph_outputs:
            assert o in dst_subgraph_outputs, f""
        for n in dst_nodes:
            self.add_node(n)
        for n in src_nodes:
            self.remove_node(n)

    def topo_sort(self, networkx=True):
        if networkx:
            import networkx as nx

            g = self.to_networkx()
            self._nodes = [g.nodes[n]["obj"] for n in nx.topological_sort(g)]
        else:
            in_degree = {
                node: len([i for i in node.inputs if len(i.srcs) > 0])
                for node in self._nodes
            }
            queue = deque([node for node in self._nodes if in_degree[node] == 0])
            top_order = []
            while queue:
                node = queue.popleft()
                top_order.append(node)
                for edge in node.outputs:
                    for successor in edge.dsts:
                        for o in successor.inputs:
                            if edge == o:
                                in_degree[successor] -= 1
                        if in_degree[successor] == 0:
                            queue.append(successor)

            if len(top_order) != len(self.nodes):
                raise ValueError(
                    "Graph has at least one cycle, topological sort is not possible"
                )

            self._nodes = top_order
