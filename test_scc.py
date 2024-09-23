import unittest
from graph import Graph
from scc import find_strongly_connected_components, build_meta_graph

class TestSCCMethods(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()
        self.graph.add_node(1)
        self.graph.add_node(2)
        self.graph.add_node(3)
        self.graph.add_node(4)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(2, 3)
        self.graph.add_edge(3, 1)
        self.graph.add_edge(3, 4)

    def test_find_strongly_connected_components(self):
        sccs = find_strongly_connected_components(self.graph)
        expected_sccs = [frozenset({1, 2, 3}), frozenset({4})]
        self.assertCountEqual(sccs, expected_sccs)

    def test_build_meta_graph(self):
        meta_graph = build_meta_graph(self.graph)
        nodes = list(meta_graph.all_nodes())
        edges = list(meta_graph.all_edges())
        self.assertIn(frozenset({1, 2, 3}), nodes)
        self.assertIn(frozenset({4}), nodes)
        self.assertIn((frozenset({1, 2, 3}), frozenset({4})), edges)

if __name__ == '__main__':
    unittest.main()
