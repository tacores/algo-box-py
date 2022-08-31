# python3
import sys

"""Suffix Array を利用し、text中のpatternの出現位置を特定する。"""

class suffix_array_builder:
    """Suffix Array のビルダークラス"""

    # 文字列に許容する文字（辞書順を維持すること）
    Symbols = ['$', 'A', 'C', 'G', 'T']

    def build_suffix_array(self, S):
        """suffix文字列のソート順を返す。"""
        """例えば、AACA$ という文字列が与えられたとき、"""
        """ $ < A$ < AACA$ < ACA$ < CA$ であるため、"""
        """[4, 3, 0, 1, 2] を返す。"""

        # 一文字のカウントソート
        order = self.sort_characters(S)
        # ソート順が等しい文字列をクラス分け
        cls = self.compute_char_classes(S, order)
        L = 1
        while L < len(S):
            # ソートする文字列を２倍ずつ長くしていく。
            # 文字列の前半分と後半分を比較するだけでソートできる。
            order = self.sort_doubled(S, L, order, cls)
            cls = self.update_classes(order, cls, L)
            L *= 2
        return order

    def sort_characters(self, S):
        order = [-1] * len(S)
        count = {}
        for c in self.Symbols:
            count[c] = 0

        for i in range(len(S)):
            count[S[i]] = count[S[i]] + 1
        for j in range(1, len(self.Symbols)):
            count[self.Symbols[j]] = count[self.Symbols[j]] + count[self.Symbols[j - 1]]
        for i in range(len(S) - 1, -1, -1):
            c = S[i]
            count[c] = count[c] - 1
            order[count[c]] = i
        return order

    def compute_char_classes(self, S, order):
        cls = [-1] * len(S)
        cls[order[0]] = 0
        for i in range(1, len(S)):
            if S[order[i]] != S[order[i - 1]]:
                cls[order[i]] = cls[order[i - 1]] + 1
            else:
                cls[order[i]] = cls[order[i - 1]]
        return cls

    def sort_doubled(self, S, L, order, cls):
        count = [0] * len(S)
        newOrder = [-1] * len(S)
        for i in range(len(S)):
            count[cls[i]] = count[cls[i]] + 1
        for j in range(1, len(S)):
            count[j] = count[j] + count[j - 1]
        for i in range(len(S) - 1, -1, -1):
            start = (order[i] - L + len(S)) % (len(S))
            cl = cls[start]
            count[cl] = count[cl] - 1
            newOrder[count[cl]] = start
        return newOrder

    def update_classes(self, newOrder, cls, L):
        n = len(newOrder)
        newCls = [-1] * n
        newCls[newOrder[0]] = 0
        for i in range(1, n):
            cur = newOrder[i]
            prev = newOrder[i - 1]
            mid = (cur + L) % n
            midPrev = (prev + L) % n
            if cls[cur] != cls[prev] or cls[mid] != cls[midPrev]:
                newCls[cur] = newCls[prev] + 1
            else:
                newCls[cur] = newCls[prev]
        return newCls

def find_occurrences(text, patterns):
    """text中で、patternが出現する位置の集合を返す。"""
    occs = set()
    # suffix array をビルド
    text = text + '$'
    suffix_array = suffix_array_builder().build_suffix_array(text)
    #for i in range(len(suffix_array)):
    #    print(str(i) + ' : ' + text[suffix_array[i]:])

    for pattern in patterns:
        start, end = match_pattern_with_suffix_array(text, pattern, suffix_array)
        for i in range(start, end):
            occs.add(suffix_array[i])

    return occs

# suffix arrayを使い、patternが出現する範囲を返す。
# 2分探索で絞り込む。
def match_pattern_with_suffix_array(text, pattern, suffix_array):
    start = end = 0
    minIndex = 0
    maxIndex = len(text)
    while minIndex < maxIndex:
        midIndex = int((minIndex + maxIndex) / 2)
        suffix = text[suffix_array[midIndex]:]
        if pattern > suffix:
            minIndex = midIndex + 1
        else:
            maxIndex = midIndex
    start = minIndex

    maxIndex = len(text)
    while minIndex < maxIndex:
        midIndex = int((minIndex + maxIndex) / 2)
        suffix = text[suffix_array[midIndex]:]
        # patternで始まる場合は、範囲に含まれる
        if pattern < suffix and not suffix.startswith(pattern):
            maxIndex = midIndex
        else:
            minIndex = midIndex + 1
        end = maxIndex
    return (start, end)


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    occs = find_occurrences(text, patterns)
    print(" ".join(map(str, occs)))