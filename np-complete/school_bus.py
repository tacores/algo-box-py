# python3
INF = 10 ** 9

# TSP（巡回セールスマン問題）を動的計画法で解くアルゴリズム
# ノードのサブ集合を整数Kで表現していることが特徴
# {i: kのi番目のビットが1}

def read_data():
    n, m = map(int, input().split())
    graph = [[INF] * n for _ in range(n)]
    for _ in range(m):
        u, v, weight = map(int, input().split())
        u -= 1
        v -= 1
        graph[u][v] = graph[v][u] = weight
    return graph

def print_answer(path_weight, path):
    print(path_weight)
    if path_weight == -1:
        return
    print(' '.join(map(str, path)))

def optimal_path(graph):
    n = len(graph)

    # サブ集合を整数kで表現する。{i: kのi番目のビットが1}
    # サイズ（要素数）ごとに、サブ集合のリストを保存しておく
    set_of_length = [[] for _ in range(n + 1)]
    for k in range(2**n + 1):
        bit_count = 0
        for i in range(n + 1):
            if ((k >> i) & 1) == 1:
                bit_count += 1
        set_of_length[bit_count].append(k)

    # サブ集合S内のノードを一回ずつ通るパスで、
    # jを終端にした場合の最小コストを C[S][j] として動的計画法で計算する
    C = [[INF] * n for _ in range(2**n)] 
    C[1][0] = 0    # C({1},1) = 0
    for size in range(2, n + 1):    # サブ集合のサイズ
        for S in set_of_length[size]:   # 特定サイズのサブ集合
            C[S][0] = INF
            for i in range(2, n + 1):
                # i が Sに含まれない場合はスキップ
                if S & (1 << (i - 1)) == 0:
                    continue
                for j in range(1, n + 1):
                    if i == j:
                        continue
                    S_minus_i = (S ^ (1 << (i - 1)))    #サブ集合からiを除く
                    C[S][i - 1] = min(C[S][i - 1], C[S_minus_i][j - 1] + graph[j - 1][i - 1])

    best_ans = INF  # 最適コスト
    wholeS = 2**n - 1   # 全ノードを含む集合（全ビットが1）
    for i in range(n):
        if best_ans > C[wholeS][i] + graph[i][0]:
            best_ans = C[wholeS][i] + graph[i][0]
            last_node = i

    # 最適コストが無い場合、-1 を返す
    if best_ans == INF:
        return (-1, [])

    # 最適なpathを逆にたどる
    best_path = []
    S = (wholeS ^ (1 << last_node)) # サブ集合から最後のノードを除く
    back_val = best_ans - graph[last_node][0]
    best_path.append(last_node + 1)
    for i in range(n):
        for j in range(n):
            if j + 1 in best_path:
                continue
            # j -> last_node が最適パスに含まれる
            if back_val == C[S][j] + graph[j][last_node]:
                best_path.append(j + 1)
                back_val -= graph[j][last_node]
                last_node = j
                # サブ集合からjを除く
                S = (S ^ (1 << j))
                break

    # 正順に並べ替える
    best_path.reverse()
    return (best_ans, best_path)


if __name__ == '__main__':
    print_answer(*optimal_path(read_data()))
