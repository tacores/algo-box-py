
from bwtinverse import InverseBWT
import unittest

class bwtinverseTest(unittest.TestCase):

    def test_sample1(self):
        param = "AC$A"
        expected = "ACA$"
        self.assertEqual(InverseBWT(param), expected)

    def test_sample2(self):
        param = "AGGGAA$"
        expected = "GAGAGA$"
        self.assertEqual(InverseBWT(param), expected)

if __name__ == '__main__':
    unittest.main()
