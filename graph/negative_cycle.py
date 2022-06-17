#Uses python3

import sys

# 有向グラフにネガティブサイクルがあるかをBellman-Fordで判定する
# スタートのノードが指定されないタイプ
def negative_cycle(adj, cost):
    n = len(adj)

    if bellman_ford(adj, cost, n):
        return 1
    return 0

# returns true if there is no nagative cycle
# otherwise returns fasle
def bellman_ford(adj, cost, n):
    dist = [10000] * n
    # dist[s] = 0  # スタートのノードが指定されている場合

    for i in range(1, n):   # |V|-1
        distChanged = False
        for u in range(n):
            #if dist[u] == sys.maxsize:
            #    continue
            for i in range(len(adj[u])):
                v = adj[u][i]
                if dist[v] > dist[u] + cost[u][i]:
                    dist[v] = dist[u] + cost[u][i]
                    distChanged = True
        if not distChanged:
            break

    for u in range(n):
        if dist[u] == sys.maxsize:
            continue
        for i in range(len(adj[u])):
            v = adj[u][i]
            if dist[v] > dist[u] + cost[u][i]:
                return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
