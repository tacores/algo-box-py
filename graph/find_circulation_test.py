# python3

import unittest
from find_circulation import construct_graph
from find_circulation import solve

class find_circulation_test(unittest.TestCase):

    def test_max_flow_sample1(self):
        N = 3
        E = 2
        edges = [
            (1, 2, 0, 3),
            (2, 3, 0, 3)
        ]
        graph = construct_graph(N, E, edges)
        expected = ["YES", 0, 0]
        self.assertEqual(solve(graph, N, E), expected)

    def test_max_flow_sample2(self):
        N = 3
        E = 3
        edges = [
            (1, 2, 1, 3),
            (2, 3, 2, 4),
            (3, 1, 1, 2)
        ]
        graph = construct_graph(N, E, edges)
        expected = ["YES", 2, 2, 2]
        self.assertEqual(solve(graph, N, E), expected)

    def test_max_flow_sample3(self):
        N = 3
        E = 3
        edges = [
            (1, 2, 1, 3),
            (2, 3, 2, 4),
            (1, 3, 1, 2)
        ]
        graph = construct_graph(N, E, edges)
        expected = ["NO"]
        self.assertEqual(solve(graph, N, E), expected)

    def test_max_flow_sample4(self):
        N = 4
        E = 5
        edges = [
            (1, 2, 2, 4),
            (2, 3, 1, 2),
            (3, 1, 1, 4),
            (2, 4, 1, 2),
            (4, 1, 1, 4)
        ]
        graph = construct_graph(N, E, edges)
        expected = ["YES", 2, 1, 1, 1, 1]
        self.assertEqual(solve(graph, N, E), expected)

if __name__ == '__main__':
    unittest.main()


