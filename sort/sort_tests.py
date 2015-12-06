import unittest

import insert_sort
import bubble_sort
import select_sort

class SortTest(unittest.TestCase):

    def setUp(self):
        self.desc_arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.desc_expect = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        self.asc_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.asc_expect = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        self.random_arr = [8, 4, 2, 1, 10, 6, 3, 9, 5, 7]
        self.random_expect = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        self.two_kinds_arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
        self.two_kinds_expect = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]

    def test_insert_sort_descending(self):
        arr = self.desc_arr
        insert_sort.InsertSort.sort(arr)

        self.assertEqual(self.desc_expect, arr)

    def test_insert_sort_ascending(self):
        arr = self.asc_arr
        insert_sort.InsertSort.sort(arr)

        self.assertEqual(self.asc_expect, arr)

    def test_insert_sort_2kinds(self):
        arr = self.two_kinds_arr
        insert_sort.InsertSort.sort(arr)

        self.assertEqual(self.two_kinds_expect, arr)

    def test_insert_sort_random(self):
        arr = self.random_arr
        insert_sort.InsertSort.sort(arr)

        self.assertEqual(self.random_expect, arr)

    def test_bubble_sort_descending(self):
        arr = self.desc_arr
        bubble_sort.BubbleSort.sort(arr)

        self.assertEqual(self.desc_expect, arr)

    def test_bubble_sort_ascending(self):
        arr = self.asc_arr
        bubble_sort.BubbleSort.sort(arr)

        self.assertEqual(self.asc_expect, arr)

    def test_bubble_sort_2kinds(self):
        arr = self.two_kinds_arr
        bubble_sort.BubbleSort.sort(arr)

        self.assertEqual(self.two_kinds_expect, arr)

    def test_bubble_sort_random(self):
        arr = self.random_arr
        bubble_sort.BubbleSort.sort(arr)

        self.assertEqual(self.random_expect, arr)

    def test_select_sort_descending(self):
        arr = self.desc_arr
        select_sort.SelectSort.sort(arr)

        self.assertEqual(self.desc_expect, arr)

    def test_select_sort_ascending(self):
        arr = self.asc_arr
        select_sort.SelectSort.sort(arr)

        self.assertEqual(self.asc_expect, arr)

    def test_select_sort_2kinds(self):
        arr = self.two_kinds_arr
        select_sort.SelectSort.sort(arr)

        self.assertEqual(self.two_kinds_expect, arr)

    def test_select_sort_random(self):
        arr = self.random_arr
        select_sort.SelectSort.sort(arr)

        self.assertEqual(self.random_expect, arr)

if __name__ == '__main__':
    unittest.main()

