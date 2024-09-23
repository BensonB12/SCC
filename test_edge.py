import unittest
from edge import Edge

class TestEdge(unittest.TestCase):

    def test_edge_initialization(self):
        edge = Edge(node=1, neighbor=2, weight=5)
        self.assertEqual(edge.node, 1)
        self.assertEqual(edge.neighbor, 2)
        self.assertEqual(edge.weight, 5)

    def test_edge_default_weight(self):
        edge = Edge(node=1, neighbor=2)
        self.assertEqual(edge.weight, 1)

    def test_edge_invalid_initialization(self):
        with self.assertRaises(ValueError):
            Edge(node="invalid", neighbor=2)  # Node should be int

if __name__ == '__main__':
    unittest.main()
