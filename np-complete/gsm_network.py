# python3
import itertools

"""
三色塗分け問題。NP完全問題の一種。
問題の解自体を出力するのではなく、
SAT Solver に渡すconjunctive normal form(CNF・連言標準形)を出力する

（例）
Input:（三色に塗分けできる場合）
3 3
1 2
2 3
1 3
Output:（2行目以降をSAT Solverに渡すと、SATISFIABLEかどうか判定される）
21 9
-1 -2 0
-4 -5 0
-7 -8 0
（以下略）
"""

def printEquisatisfiableSatFormula(n, clauses):
    """
    CNF出力。
    1行目に式の節数と変数の数を出力し、2行目以降にCNFを出力する
    """
    print("{} {}".format(len(clauses), n*3))
    for l in clauses:
        s = ""
        for p in l:
            s += str(p) + " "
        s += "0"    # 節の最後に0を付ける決まり
        print(s)

def valnum(n, v, color):
    """
    各ノードの各色ごとに一意な整数値を割り当てる。

    n:ノード数 v:ノード番号 color:色（1-3)
    x[color-1][v] の二次元配列を一次元配列のインデックスで表すようなイメージ
    """
    assert(0 <= v and v <= n - 1)
    assert(1 <= color and color <= 3)
    return n * (color - 1) + (v + 1) # 0始まりではなく1始まり

def exactly_one_of(clauses, literals):
    """
    変数リストの中で１個だけ真であるという条件の生成
    x1, x2, x3 の1個だけが真であることと
    (x1 V x2 V x3)(x1! V x2!)(x2! V x3!)(x3! V x1!) は等価
    """
    clauses.append([l for l in literals])   # (x1 V x2 V x3) の部分
    for pair in itertools.combinations(literals, 2):
        clauses.append([-l for l in pair])

def at_most_one(clauses, literals):
    """
    変数リストの中で最大でも1個だけが真であるという条件の生成
    x1, x2 の最大でも1個だけが真であることと
    (x1! V x2!) は等価
    """
    clauses.append([-l for l in literals])

def solve(n, m, edges):
    """
    三色塗分け問題のCNF生成
    """
    clauses = []
    for i in range(n):
        for j in range(i + 1, n):
            # i -> j へのエッジがある場合
            if edges[i][j]:
                for color in range(1,4):
                    # 隣接するノードが、同じ色であることはない
                    at_most_one(clauses, [valnum(n, i, color), valnum(n, j, color)])
        # ノードは、三色のうち一色
        exactly_one_of(clauses, [valnum(n, i, color) for color in range(1,4)])
    return clauses

def readParams():
    n, m = map(int, input().split())
    #edges = [ list(map(int, input().split())) for i in range(m) ]
    edges = [[False] * n for _ in range(n)]
    for i in range(m):
        u, v = map(int, input().split())
        edges[u-1][v-1] = True
        edges[v-1][u-1] = True
    return n, m, edges

if __name__ == '__main__':
    n, m, edges = readParams()
    clauses = solve(n, m, edges)
    printEquisatisfiableSatFormula(n, clauses)
