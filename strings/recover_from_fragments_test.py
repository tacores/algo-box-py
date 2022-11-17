
from recover_from_fragments import execute
import unittest
import random

# A, C, G, T
chars = ['A', 'C', 'G', 'T']

def gen_str(N):
    s = ''
    for i in range(N):
        c = chars[random.randint(0, 3)]
        s += c
    #print(s)
    return s

def gen_fragment(s, ln, N):
    sln = len(s)
    result = []
    for i in range(N):
        pos = random.randint(0, sln - 1)
        if pos <= sln - ln:
            flagment = s[pos:pos + ln]
        else:
            flagment = s[pos:] + s[:ln - sln + pos]
        assert(len(flagment) == ln)
        #print(flagment)
        result.append(flagment)
    return result

class w1_rob_test(unittest.TestCase):

    def test_length_under_12(self):

        reads = ["TTTACAGATACAGA", "ACAGATACAGAGGG"]

        # 全組み合わせをチェックしないように、12桁未満の一致は無視する実装
        self.assertEqual(execute(reads), "TTTACAGATACAGAACAGATACAGAGGG")

    def test_length_equal_12(self):

        reads = ["TTTACAGATACAGAT", "ACAGATACAGATGGG"]

        # 12桁が一致する場合は、合成する
        self.assertEqual(execute(reads), "TTTACAGATACAGATGGG")

    def test_random_robust(self):
        """
        断片の数Nが1618個、断片の長さlnが100のとき、
        長さint(N * ln / 10)の文字列をランダムに生成し、
        その文字列の部分文字列をN個ランダムに生成する。
        その断片から、元の文字列を復元し、長さが一致すればOKとする。
        """
        N = 1618
        ln = 100
        s = gen_str(int(N * ln / 10))
        reads = gen_fragment(s, ln, N)

        self.assertEqual(len(execute(reads)), len(s))


if __name__ == '__main__':
    unittest.main()
