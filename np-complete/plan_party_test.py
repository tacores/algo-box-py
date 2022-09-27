
from plan_party import MaxWeightIndependentTreeSubset
from plan_party import Vertex
import unittest

def buildTree(weight, edges):
    tree = [Vertex(w) for w in weight]
    for [a, b] in edges:
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree

class plan_party_test(unittest.TestCase):

    def test_isSatisfiable_sample1(self):
        n = 5
        weight = [1000]
        edges = []
        expected = 1000

        tree = buildTree(weight, edges)
        result = MaxWeightIndependentTreeSubset(tree)
        self.assertTrue(result, expected)

    def test_isSatisfiable_sample2(self):
        n = 2
        weight = [1, 2]
        edges = [[1, 2]]
        expected = 2

        tree = buildTree(weight, edges)
        result = MaxWeightIndependentTreeSubset(tree)
        self.assertTrue(result, expected)

    def test_isSatisfiable_sample3(self):
        n = 5
        weight = [1, 5, 3, 7, 5]
        edges = [[5, 4], [2, 3], [4, 2], [1, 2]]
        expected = 11

        tree = buildTree(weight, edges)
        result = MaxWeightIndependentTreeSubset(tree)
        self.assertTrue(result, expected)

if __name__ == '__main__':
    unittest.main()
