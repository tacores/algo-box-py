# python3

import unittest
from eulerian_cycle import hierholzer

class eulerian_cycle_test(unittest.TestCase):

    def test_hierholzer_sample1(self):
        edges = [
            (1, 2),
            (1, 1),
            (0, 1),
            (2, 0)
        ]
        expected = [0, 1, 1, 2]
        self.assertEqual(hierholzer(3, len(edges), edges), expected)

    def test_hierholzer_sample2(self):
        edges = [
            (0, 2),
            (1, 2),
            (0, 1),
            (2, 0)
        ]
        expected = None
        self.assertEqual(hierholzer(3, len(edges), edges), expected)

    def test_hierholzer_sample3(self):
        edges = [
            (0, 1),
            (1, 0),
            (0, 3),
            (3, 0),
            (1, 3),
            (2, 1),
            (3, 2)
        ]
        expected = [0, 1, 0, 3, 2, 1, 3]
        self.assertEqual(hierholzer(4, len(edges), edges), expected)

    def test_hierholzer_sample4(self):
        edges = [
            (1, 2),
            (2, 3),
            (0, 3),
            (2, 0),
            (3, 1),
            (1, 2),
            (3, 1)
        ]
        expected = [1, 2, 3, 1, 2, 0, 3]
        self.assertEqual(hierholzer(4, len(edges), edges), expected)


if __name__ == '__main__':
    unittest.main()


