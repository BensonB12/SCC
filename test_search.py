import unittest
from graph import Graph
from search import whatever_first_search, reverse_graph, topological_sort_of_dag, stack

class TestSearchMethods(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()
        self.graph.add_node(1)
        self.graph.add_node(2)
        self.graph.add_node(3)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(2, 3)

    def test_whatever_first_search(self):
        result = whatever_first_search(self.graph, 1, 3, stack())
        self.assertEqual(result, [(None, 1), (1, 2), (2, 3)])

    def test_topological_sort_of_dag(self):
        order = topological_sort_of_dag(self.graph, [1, 2, 3])
        self.assertEqual(order, [1, 2, 3])

    def test_reverse_graph(self):
        reversed_graph = reverse_graph(self.graph)
        self.assertIn((2, 1), reversed_graph.all_edges())
        self.assertIn((3, 2), reversed_graph.all_edges())

if __name__ == '__main__':
    unittest.main()
