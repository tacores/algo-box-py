# python3
import itertools

"""
全ての部屋を１回ずつ巡回する問題。NP完全問題の一種。
問題の解自体を出力するのではなく、
SAT Solver に渡すconjunctive normal form(CNF・連言標準形)を出力する

（例）
Input:（解が存在しないケース）
4 3
1 2
1 3
1 4
Output:（2行目以降をSAT Solverに渡すと、SATISFIABLEかどうか判定される）
43 2106
-352 -701 0
-353 -1051 0
（以下略）
"""

def printEquisatisfiableSatFormula(n, clauses):
    """
    CNF出力。
    1行目に式の節数と変数の数を出力し、2行目以降にCNFを出力する
    """
    print("{} {}".format(len(clauses), (n + 2) * 350 + (n + 2)))
    for l in clauses:
        s = ""
        for p in l:
            s += str(p) + " "
        s += "0"    # 節の最後に0を付ける決まり
        print(s)

def valnum(n, u, v):
    """
    u->v の経路ごとに一意な整数値を割り当てる。
    n:ノード数 u:移動元ノード番号 v:移動先ノード番号
    """
    assert(0 <= u and u <= 301) # 300ノード + srcとsink の仮想ノード
    assert(0 <= v and v <= 301)
    # 変数のサイズが合計12万という制限があったので、切りの悪い350を使っている
    return 350 * (u + 1) + (v + 1) # 0始まりではなく1始まり

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
    巡回問題のCNF生成
    問題で与えられたノードに加えて、
    src と sink の仮想の２ノードを考えるのが、工夫した点。
    """
    clauses = []
    # 各経路は一方向だけ
    for i in range(n):
        nodes_from_i = []
        for j in range(i, n):
            # i -> j へのエッジがある場合
            if edges[i][j]:
                at_most_one(clauses, [valnum(n, i, j), valnum(n, j, i)])

    # i から出る経路は１つだけ
    for i in range(n):
        nodes_from_i = []
        for j in range(n):
            # i -> j へのエッジがある場合
            if edges[i][j]:
                nodes_from_i.append(j)
        # sinkノードへの経路は必ず存在すると考える
        nodes_from_i.append(n + 1)
        exactly_one_of(clauses, [valnum(n, i, v) for v in nodes_from_i])

    # i に入る経路は１つだけ
    for i in range(n):
        nodes_to_i = []
        for j in range(n):
            # i -> j へのエッジがある場合
            if edges[j][i]:
                nodes_to_i.append(j)
        # srcノードからの経路は必ず存在すると考える
        nodes_to_i.append(n)
        exactly_one_of(clauses, [valnum(n, v, i) for v in nodes_to_i])

    # srcノードから出る経路は１つだけ
    exactly_one_of(clauses, [valnum(n, n, v) for v in range(n)])
    # sink ノードに入る経路は１つだけ
    exactly_one_of(clauses, [valnum(n, u, n + 1) for u in range(n)])
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
