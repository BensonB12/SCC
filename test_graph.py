import unittest
from graph import Graph

class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()

    def test_add_node(self):
        self.graph.add_node(1)
        self.assertIn(1, self.graph.all_nodes())

    def test_add_edge(self):
        self.graph.add_node(1)
        self.graph.add_node(2)
        self.graph.add_edge(1, 2, 10)
        self.assertIn((1, 2), self.graph.all_edges())
        self.assertEqual(self.graph.edge_weight(1, 2), 10)

    def test_neighbors_of(self):
        self.graph.add_node(1)
        self.graph.add_node(2)
        self.graph.add_edge(1, 2)
        self.assertEqual(self.graph.neighbors_of(1), [2])

    def test_no_neighbors(self):
        self.graph.add_node(3)
        self.assertEqual(self.graph.neighbors_of(3), [])

    def test_edge_weight_default(self):
        self.graph.add_node(1)
        self.graph.add_node(2)
        self.graph.add_edge(1, 2)
        self.assertEqual(self.graph.edge_weight(1, 2), 1)

if __name__ == '__main__':
    unittest.main()
