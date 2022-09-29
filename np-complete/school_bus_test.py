
from school_bus import optimal_path
from school_bus import INF
import unittest

def buildGraph(n, m, edges):
    graph = [[INF] * n for _ in range(n)]
    for [u, v, w] in edges:
        u -= 1
        v -= 1
        graph[u][v] = graph[v][u] = w
    return graph

class school_bus_test(unittest.TestCase):

    def test_optimal_path_sample1(self):
        n = 4
        m = 6
        edges = [[1, 2, 20],[1, 3, 42],[1, 4, 35],[2, 3, 30],[2, 4, 34],[3, 4, 12]]
        expectedVal = 97
        expectedPath = [1, 4, 3, 2]

        graph = buildGraph(n, m, edges)
        (ans, path) = optimal_path(graph)
        self.assertEqual(ans, expectedVal)
        self.assertEqual(path, expectedPath)

    def test_optimal_path_sample2(self):
        n = 4
        m = 4
        edges = [[1, 2, 1],[2, 3, 4],[3, 4, 5],[4, 2, 1]]
        expectedVal = -1
        expectedPath = []

        graph = buildGraph(n, m, edges)
        (ans, path) = optimal_path(graph)
        self.assertEqual(ans, expectedVal)
        self.assertEqual(path, expectedPath)

    def test_optimal_path_two(self):
        n = 2
        m = 1
        edges = [[1, 2, 100]]
        expectedVal = 200
        expectedPath = [1, 2]

        graph = buildGraph(n, m, edges)
        (ans, path) = optimal_path(graph)
        self.assertEqual(ans, expectedVal)
        self.assertEqual(path, expectedPath)

    def test_optimal_path_three(self):
        n = 3
        m = 3
        edges = [[1, 2, 10],[2, 3, 20],[3, 1, 30]]
        expectedVal = 60
        expectedPath = [1, 3, 2]

        graph = buildGraph(n, m, edges)
        (ans, path) = optimal_path(graph)
        self.assertEqual(ans, expectedVal)
        self.assertEqual(path, expectedPath)

    def test_optimal_path_three_noloop(self):
        n = 3
        m = 2
        edges = [[1, 2, 10],[2, 3, 20]]
        expectedVal = -1
        expectedPath = []

        graph = buildGraph(n, m, edges)
        (ans, path) = optimal_path(graph)
        self.assertEqual(ans, expectedVal)
        self.assertEqual(path, expectedPath)

    def test_optimal_path_17(self):
        n = 17
        m = 17
        edges = [[1,2,1],[2,3,1],[3,4,1],[4,5,1],[5,6,1],[6,7,1],[7,8,1],[8,9,1],[9,10,1],[10,11,1],[11,12,1],[12,13,1],[13,14,1],[14,15,1],[15,16,1],[16,17,1],[17,1,1]]
        expectedVal = 17

        graph = buildGraph(n, m, edges)
        (ans, path) = optimal_path(graph)
        self.assertEqual(ans, expectedVal)

if __name__ == '__main__':
    unittest.main()
