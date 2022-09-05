
from evacuation import max_flow
from evacuation import FlowGraph
import unittest

def add_edge(graph, s, t, capa):
    graph.add_edge(s - 1, t - 1, capa)

class kmp_test(unittest.TestCase):

    def test_sample1(self):
        graph = FlowGraph(5)
        add_edge(graph, 1, 2, 2)
        add_edge(graph, 2, 5, 5)
        add_edge(graph, 1, 3, 6)
        add_edge(graph, 3, 4, 2)
        add_edge(graph, 4, 5, 1)
        add_edge(graph, 3, 2, 3)
        add_edge(graph, 2, 4, 1)

        expected = 6
        self.assertEqual(max_flow(graph, 0, 4), expected)

    def test_sample2(self):
        graph = FlowGraph(4)
        add_edge(graph, 1, 2, 10000)
        add_edge(graph, 1, 3, 10000)
        add_edge(graph, 2, 3, 1)
        add_edge(graph, 3, 4, 10000)
        add_edge(graph, 2, 4, 10000)

        expected = 20000
        self.assertEqual(max_flow(graph, 0, 3), expected)

if __name__ == '__main__':
    unittest.main()
