#Uses python3

from dis import dis
import sys
import queue

# ネガティブサイクルを含むかもしれない有向グラフで最短距離を求める
def shortet_paths(adj, cost, s, distance, reachable, shortest):
    n = len(adj)

    distance[s] = 0
    reachable[s] = 1

    # |V|-1 回　→　ネガティブサイクルがなければこのループで収束する
    for i in range(1, n):
        distChanged = False
        for u in range(n):
            if distance[u] == sys.maxsize:
                continue                
            for j in range(len(adj[u])):
                v = adj[u][j]
                if distance[v] > distance[u] + cost[u][j]:
                    distance[v] = distance[u] + cost[u][j]
                    reachable[v] = 1    # スタートノードから到達可能
                    distChanged = True
        if not distChanged:
            break

    # ネガティブサイクルに含まれるノードを検出するループ
    for i in range(1, n):
        distChanged = False
        for u in range(n):
            if distance[u] == sys.maxsize:
                continue                
            for j in range(len(adj[u])):
                v = adj[u][j]
                if distance[v] > distance[u] + cost[u][j]:

                    # ネガティブサイクルを大きく加速させるトリック
                    if cost[u][j] < 0:
                        cost[u][j] = -10**16

                    distance[v] = distance[u] + cost[u][j]
                    shortest[v] = 0     #最短パスは無い（マイナス無限大）
                    distChanged = True
        if not distChanged:
            break


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
    s = data[0]
    s -= 1
    distance = [sys.maxsize] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

