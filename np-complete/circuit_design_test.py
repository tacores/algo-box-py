
from circuit_design import isSatisfiable
from circuit_design import add_edge
import unittest

def add_edge_wrapper(N, m, clauses):
    G = [[] for i in range(2*N)]
    RG = [[] for i in range(2*N)]
    for i in range(m):
        a, b = clauses[i][0], clauses[i][1]
        a_negate = 0 if a > 0 else 1
        b_negate = 0 if b > 0 else 1
        if a < 0:
            a = -a
        if b < 0:
            b = -b
        add_edge(a - 1, a_negate, b - 1, b_negate, N, G, RG)
    return G, RG

class circuit_design_test(unittest.TestCase):

    def test_isSatisfiable_sample1(self):
        N = 3
        m = 3
        clauses = [[1, -3], [-1, 2], [-2, -3]]
        expected = [1, 2, -3]

        G, RG = add_edge_wrapper(N, m, clauses)
        result = isSatisfiable(N, G, RG)
        b = [True] * 3
        for i in range(3):
            if result[i] < 0:
                b[i] = False
        self.assertTrue( (b[0] or not b[2]) and (not b[0] or b[1]) and (not b[1] or not b[2]) )

    def test_isSatisfiable_sample2(self):
        N = 1
        m = 2
        clauses = [[1, 1], [-1, -1]]
        expected = None

        G, RG = add_edge_wrapper(N, m, clauses)
        result = isSatisfiable(N, G, RG)
        self.assertEqual(result, expected)

    def test_isSatisfiable_circle(self):
        N = 2
        m = 3
        clauses = [[-1, 2], [-2, -2], [1, 1]]
        expected = None

        G, RG = add_edge_wrapper(N, m, clauses)
        result = isSatisfiable(N, G, RG)
        self.assertEqual(result, expected)

    def test_isSatisfiable_textexample1(self):
        N = 3
        m = 4
        clauses = [[-1, 2], [-2, 3], [1, -3], [3, 2]]
        expected = [1, 2, 3]

        G, RG = add_edge_wrapper(N, m, clauses)
        result = isSatisfiable(N, G, RG)
        self.assertEqual(result, expected)

    def test_isSatisfiable_textexample2(self):
        N = 3
        m = 4
        clauses = [[1, 2], [-3, -3], [3, -1], [-2, -2]]
        expected = None

        G, RG = add_edge_wrapper(N, m, clauses)
        result = isSatisfiable(N, G, RG)
        self.assertEqual(result, expected)

    def test_isSatisfiable_textexample3(self):
        N = 3
        m = 4
        clauses = [[1, 2], [1, -2], [-1, 2], [-1, -2]]
        expected = None

        G, RG = add_edge_wrapper(N, m, clauses)
        result = isSatisfiable(N, G, RG)
        self.assertEqual(result, expected)
    
    def test_isSatisfiable_textexample4(self):
        N = 3
        m = 3
        clauses = [[1, 2], [-3, -3], [3, -1]]

        G, RG = add_edge_wrapper(N, m, clauses)
        result = isSatisfiable(N, G, RG)
        b = [True] * 3
        for i in range(3):
            if result[i] < 0:
                b[i] = False
        self.assertTrue( (b[0] or b[1]) and (not b[2]) and (b[2] or not b[0]) )


if __name__ == '__main__':
    unittest.main()
