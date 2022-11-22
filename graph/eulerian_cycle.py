# python3

"""
Eulerian Cycle（オイラーサイクル）を探索するHierholzer（ヒールホルツァー）アルゴリズム。
有向グラフの全ての辺を1回ずつ通り、元のノードに戻るサイクルを探索する。
入力と出力の数が異なるノードが存在する場合（imbalanced）、オイラーサイクルは存在しない。
"""

def hierholzer(N, M, E):
    G = [[] for i in range(N)]
    deg = [0]*N
    rdeg = [0]*N
    for (a, b) in E:
        deg[a] += 1
        rdeg[b] += 1
        G[a].append(b)
    
    # バランスをチェックする。imbalancedの場合、Eulerian Cycle は存在しない。
    for i in range(N):
        if deg[i] != rdeg[i]:
            return None

    # パスを探索する場合の開始ノードの特定（サイクルの場合はどこでも良い）
    s = t = u = -1
    for i in range(N):
        if deg[i] == rdeg[i] == 0:
            continue
        df = deg[i] - rdeg[i]
        if not -1 <= df <= 1:
            return None
        if df == 1:
            if s != -1:
                return None
            s = i
        elif df == -1:
            if t != -1:
                return None
            t = i
        else:
            u = i
    v0 = (s if s != -1 else u)

    # Eulerian Cycle の探索
    res = []
    it = [0]*N
    st = [v0]
    *it, = map(iter, G)
    while st:
        v = st[-1]
        w = next(it[v], -1)
        if w == -1:
            res.append(v)
            st.pop()
            continue
        st.append(w)
    res.reverse()
    if len(res) != M+1:
        return None
    return res[1:]

def read_data():
    (N, M) = tuple(map(int, input().split()))
    edges = []
    for _ in range(M):
        param = list(map(int, input().split()))
        edges.append((param[0]-1, param[1]-1))
    return (N, edges)

if __name__ == '__main__':
    (N, edges) = read_data()
    result = hierholzer(N, len(edges), edges)
    if result != None:
        print("1")
        print(' '.join(list(map(lambda x: str(x + 1), result))))
    else:
        print("0")
