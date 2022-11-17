# python3

"""
長い文字列（遺伝子情報）の断片が大量に与えられたとき、
元の文字列情報を復元するアルゴリズム。
このバージョンでは確率で発生する読み取りエラーは考慮していない。
"""

class suffix_array:
    symbols = ['$', 'A', 'C', 'G', 'T']

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
        for c in self.symbols:
            count[c] = 0

        for i in range(len(S)):
            count[S[i]] = count[S[i]] + 1
        for j in range(1, len(self.symbols)):
            count[self.symbols[j]] = count[self.symbols[j]] + count[self.symbols[j - 1]]
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

class string_recovery_from_fragments:

    def bwt_from_suffix_array(self, text, order):
        l = len(text)
        bwt = [''] * l
        for i in range(l):
            bwt[i] = text[(order[i] + l - 1) % l]

        counts = dict()
        starts = dict()
        for char in suffix_array.symbols:
            counts[char] = [0] * (l + 1)
        for i in range(l):
            cuurent_Char = bwt[i]
            for char, count in counts.items():
                counts[char][i + 1] = counts[char][i]
            counts[cuurent_Char][i + 1] += 1
        current_index = 0
        for char in sorted(suffix_array.symbols):
            starts[char] = current_index
            current_index += counts[char][l]
        return bwt, starts, counts

    def find_longest_overlap(self, text, patterns, k=12):

        sa = suffix_array()
        order = sa.build_suffix_array(text)
        bwt, starts, counts = self.bwt_from_suffix_array(text, order)
        l = len(text) - 1

        occs = dict()
        for i, pattern_list in enumerate(patterns):
            pattern = pattern_list[:k]
            top = 0
            bottom = len(bwt) - 1
            current_Index = len(pattern) - 1
            while top <= bottom:
                if current_Index >= 0:
                    symbol = pattern[current_Index]
                    current_Index -= 1
                    if counts[symbol][bottom + 1] - counts[symbol][top] > 0:
                        top = starts[symbol] + counts[symbol][top]
                        bottom = starts[symbol] + counts[symbol][bottom + 1] - 1
                    else:
                        break
                else:
                    for j in range(top, bottom + 1):
                        if not order[j] in occs:
                            occs[order[j]] = []
                        occs[order[j]].append(i)
                    break
        overlap = 0
        for pos, iList in sorted(occs.items()):
            for i in iList:
                if text[pos:-1] == patterns[i][:l - pos]:
                    return i, l - pos
        return i, overlap

    def recover(self, reads):
        current_Index = 0
        genome = reads[0]
        firstRead = reads[current_Index]
        while True:
            current_Read = reads[current_Index]
            if 1 == len(reads):
                break
            del reads[current_Index]
            current_Index, overlap = self.find_longest_overlap(current_Read + '$', reads)
            genome += reads[current_Index][overlap:]
        current_Index, overlap = self.find_longest_overlap(reads[0] + '$', [firstRead])
        if overlap > 0:
            return genome[:-overlap]
        else:
            return genome

def read_data(N):
    reads = []
    for i in range(N):
        reads.append(input())
    return reads

def execute(reads):
    srff = string_recovery_from_fragments()
    s = srff.recover(reads)
    return s

if __name__ == '__main__':
    N = 1618
    reads = read_data(N)
    s = execute(reads)
    print(s)
