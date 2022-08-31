
from suffix_array_matching import suffix_array_builder
from suffix_array_matching import find_occurrences

import unittest

class suffix_array_long_test(unittest.TestCase):

    def test_sample1(self):
        text = 'AAA'
        patterns = ['A']
        expected = {0, 1, 2}
        self.assertEqual(find_occurrences(text, patterns), expected)

    def test_sample2(self):
        text = 'ATA'
        patterns = ['C', 'G', 'C']
        expected = set()  # empty
        self.assertEqual(find_occurrences(text, patterns), expected)

    def test_sample3(self):
        text = 'ATATATA'
        patterns = ['ATA', 'C', 'TATAT']
        expected = {0, 1, 2, 4}
        self.assertEqual(find_occurrences(text, patterns), expected)

    def test_exam_fail1(self):
        text = 'TCCTCTATGAGATCCTATTCTATGAAACCTTCAGACCAAAATTCTCCGGC'
        patterns = ['CCT', 'CAC', 'GAG', 'CAG', 'ATC']
        expected = {1, 8, 11, 13, 27, 31}
        self.assertEqual(find_occurrences(text, patterns), expected)

    def test_exam_fail2(self):
        text = 'G'
        patterns = ['G', 'T']
        expected = {0}
        self.assertEqual(find_occurrences(text, patterns), expected)

    def test_build_suffix_array1(self):
        param = 'AAA$'
        expected = [3, 2, 1, 0]
        self.assertEqual(suffix_array_builder().build_suffix_array(param), expected)

    def test_build_suffix_array2(self):
        param = 'GAC$'
        expected = [3, 1, 2, 0]
        self.assertEqual(suffix_array_builder().build_suffix_array(param), expected)

    def test_build_suffix_array3(self):
        param = 'GAGAGAGA$'
        expected = [8, 7, 5, 3, 1, 6, 4, 2, 0]
        self.assertEqual(suffix_array_builder().build_suffix_array(param), expected)

    def test_build_suffix_array4(self):
        param = 'AACGATAGCGGTAGA$'
        expected = [15, 14, 0, 1, 12, 6, 4, 2, 8, 13, 3, 7, 9, 10, 11, 5]
        self.assertEqual(suffix_array_builder().build_suffix_array(param), expected)

    def test_build_suffix_array5(self):
        param = 'AACA$'
        expected = [4, 3, 0, 1, 2]
        self.assertEqual(suffix_array_builder().build_suffix_array(param), expected)

    def test_build_suffix_sort_characters(self):
        param = 'ACGT$'
        expected = [4, 0, 1, 2, 3]
        self.assertEqual(suffix_array_builder().build_suffix_array(param), expected)

    def test_build_suffix_compute_char_classes(self):
        S = 'AGTA$'
        order = [4, 0, 3, 1, 2]
        expected = [1, 2, 3, 1, 0]
        self.assertEqual(suffix_array_builder().compute_char_classes(S, order), expected)


if __name__ == '__main__':
    unittest.main()
