import unittest

import insert_sort
import bubble_sort

class SortTest(unittest.TestCase):

    def setUp(self):
        self.sut = insert_sort.InsertSort()

    def test_insert_sort_descending(self):
        arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        insert_sort.InsertSort.sort(arr)

        expect = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(expect, arr)

    def test_insert_sort_ascending(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        insert_sort.InsertSort.sort(arr)

        expect = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(expect, arr)

    def test_insert_sort_2kinds(self):
        arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
        insert_sort.InsertSort.sort(arr)

        expect = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
        self.assertEqual(expect, arr)

    def test_insert_sort_random(self):
        arr = [8, 3, 7, 2, 10, 1, 4, 9, 5, 6]
        insert_sort.InsertSort.sort(arr)

        expect = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(expect, arr)

    def test_bubble_sort_descending(self):
        arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        bubble_sort.BubbleSort.sort(arr)

        expect = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(expect, arr)

    def test_bubble_sort_ascending(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        bubble_sort.BubbleSort.sort(arr)

        expect = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(expect, arr)

    def test_bubble_sort_2kinds(self):
        arr = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
        bubble_sort.BubbleSort.sort(arr)

        expect = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
        self.assertEqual(expect, arr)

    def test_bubble_sort_random(self):
        arr = [8, 3, 7, 2, 10, 1, 4, 9, 5, 6]
        bubble_sort.BubbleSort.sort(arr)

        expect = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(expect, arr)


if __name__ == '__main__':
    unittest.main()

