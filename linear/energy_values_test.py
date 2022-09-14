
from energy_values import SolveEquation
import unittest
import math
import numpy as np

class energy_values_test(unittest.TestCase):

    def test_SolveEquation_sample1(self):
        param = []
        expected = []
        self.assertTrue(np.allclose(SolveEquation(param), expected))

    def test_SolveEquation_sample2(self):
        param = [[1, 0, 0, 0, 1],
                 [0, 1, 0, 0, 5],
                 [0, 0, 1, 0, 4],
                 [0, 0, 0, 1, 3]]
        expected = [1.000000, 5.000000, 4.000000, 3.000000]
        self.assertTrue(np.allclose(SolveEquation(param), expected))

    def test_SolveEquation_sample3(self):
        param = [[1, 1, 3],
                 [2, 3, 7]]
        expected = [2.000000, 1.000000]
        self.assertTrue(np.allclose(SolveEquation(param), expected))

    def test_SolveEquation_sample4(self):
        param = [[5, -5, -1],
                 [-1, -2, -1]]
        expected = [0.200000, 0.40000]
        self.assertTrue(np.allclose(SolveEquation(param), expected))




if __name__ == '__main__':
    unittest.main()
