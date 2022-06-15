#Uses python3

import sys
import queue


def distance(adj, cost, s, t):
    n = len(adj)
    D = {v:float('inf') for v in range(n)}
    D[s] = 0
    visited = {}

    pq = queue.PriorityQueue()
    pq.put((0, s))

    while not pq.empty():
        (dist, u) = pq.get()
        visited[u] = 1

        for i in range(len(adj[u])):
            v = adj[u][i]
            distance = cost[u][i]
            if v not in visited:
                old_cost = D[v]
                new_cost = D[u] + distance
                if new_cost < old_cost:
                    pq.put((new_cost, v))
                    D[v] = new_cost

    if D[t] != float('inf'):
        return D[t]
    else:
        return -1


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
