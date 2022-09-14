
from diet import solve_diet_problem
import unittest
import math
import numpy as np

class diet_test(unittest.TestCase):

    def test_solve_diet_problem_sample1(self):
        n = 3
        m = 2
        A = [[-1, -1], [1, 0], [0, 1]]
        b = [-1, 2, 2]
        c = [-1, 2]
        expected = [0.000000000000000, 2.000000000000000]

        anst, ansx = solve_diet_problem(n, m, A, b, c)
        self.assertEqual(anst, 0)   # Bounded solution
        self.assertTrue(np.allclose(ansx, expected))

    def test_solve_diet_problem_sample2(self):
        n = 2
        m = 2
        A = [[1, 1], [-1, -1]]
        b = [1, -2]
        c = [1, 1]
        expected = -1   # No solution

        anst, _ = solve_diet_problem(n, m, A, b, c)
        self.assertEqual(anst, expected)   

    def test_solve_diet_problem_sample3(self):
        n = 1
        m = 3
        A = [[0, 0, 1]]
        b = [3]
        c = [1, 1, 1]
        expected = 1    # Infinity

        anst, _ = solve_diet_problem(n, m, A, b, c)
        self.assertEqual(anst, expected)

    def test_solve_diet_problem_exam_failed1(self):
        n = 1
        m = 2
        A = [[21, -37]]
        b = [3632]
        c = [76, 18]
        expected = 1    # Infinity

        anst, _ = solve_diet_problem(n, m, A, b, c)
        self.assertEqual(anst, expected)

    def test_solve_diet_problem_exam_failed2(self):
        n = 1
        m = 2
        A = [[33, 7]]
        b = [1393]
        c = [-33, 17]
        expected = [-0.000000000000002248, 199.000000000000000000]

        anst, ansx = solve_diet_problem(n, m, A, b, c)
        self.assertEqual(anst, 0)   # Bounded solution
        self.assertTrue(np.allclose(ansx, expected))

    def test_solve_diet_problem_exam_failed3(self):
        n = 2
        m = 1
        A = [[-1], [1]]
        b = [-39, 86]
        c = [-20]
        expected = [39.000000000000000000]

        anst, ansx = solve_diet_problem(n, m, A, b, c)
        self.assertEqual(anst, 0)   # Bounded solution
        self.assertTrue(np.allclose(ansx, expected)) 

if __name__ == '__main__':
    unittest.main()
