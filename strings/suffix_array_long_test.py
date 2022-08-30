
from suffix_array_long import build_suffix_array
from suffix_array_long import sort_characters
from suffix_array_long import compute_char_classes
import unittest

class suffix_array_long_test(unittest.TestCase):

    def test_sample1(self):
        param = 'AAA$'
        expected = [3, 2, 1, 0]
        self.assertEqual(build_suffix_array(param), expected)

    def test_sample2(self):
        param = 'GAC$'
        expected = [3, 1, 2, 0]
        self.assertEqual(build_suffix_array(param), expected)

    def test_sample3(self):
        param = 'GAGAGAGA$'
        expected = [8, 7, 5, 3, 1, 6, 4, 2, 0]
        self.assertEqual(build_suffix_array(param), expected)

    def test_sample4(self):
        param = 'AACGATAGCGGTAGA$'
        expected = [15, 14, 0, 1, 12, 6, 4, 2, 8, 13, 3, 7, 9, 10, 11, 5]
        self.assertEqual(build_suffix_array(param), expected)

    def test_sample5(self):
        param = 'AACA$'
        expected = [4, 3, 0, 1, 2]
        self.assertEqual(build_suffix_array(param), expected)

    def test_sort_characters(self):
        param = 'ACGT$'
        expected = [4, 0, 1, 2, 3]
        self.assertEqual(sort_characters(param), expected)

    def test_compute_char_classes(self):
        S = 'AGTA$'
        order = [4, 0, 3, 1, 2]
        expected = [1, 2, 3, 1, 0]
        self.assertEqual(compute_char_classes(S, order), expected)

    def test_exam_failed_case(self):
        param = 'AACGATAGCGGTAGA$'
        expected = [15, 14, 0, 1, 12, 6, 4, 2, 8, 13, 3, 7, 9, 10, 11, 5]
        self.assertEqual(build_suffix_array(param), expected)


if __name__ == '__main__':
    unittest.main()
