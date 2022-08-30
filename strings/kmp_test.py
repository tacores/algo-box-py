
from kmp import find_pattern
from kmp import compute_prefix_function
import unittest

class kmp_test(unittest.TestCase):

    def test_sample1(self):
        pattern = 'TACG'
        text = 'GT'
        expected = []
        self.assertEqual(find_pattern(pattern, text), expected)

    def test_sample2(self):
        pattern = 'ATA'
        text = 'ATATA'
        expected = [0, 2]
        self.assertEqual(find_pattern(pattern, text), expected)

    def test_sample3(self):
        pattern = 'ATAT'
        text = 'GATATATGCATATACTT'
        expected = [1, 3, 9]
        self.assertEqual(find_pattern(pattern, text), expected)
    
    def test_compute_prefix_function1(self):
        param = 'abababcaab'
        expected = [0, 0, 1, 2, 3, 4, 0, 1, 1, 2]
        self.assertEqual(compute_prefix_function(param), expected)

if __name__ == '__main__':
    unittest.main()
