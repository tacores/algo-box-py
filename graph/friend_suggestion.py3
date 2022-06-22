#!/usr/bin/python3

import sys
import queue

# Bidirectional Dijkstra（双方向ダイクストラ）で最短距離を返す
# 最短パスを返すには、prev[v] を追加で管理する必要がある
class BiDij:
    def __init__(self, n, adj, cost):
        self.n = n;                             # Number of nodes
        self.inf = n*10**6                      # All distances in the graph are smaller
        self.d = [[self.inf]*n, [self.inf]*n]   # Initialize distances for forward and backward searches
        self.workset = []                       # All the nodes visited by forward or backward search
        self.adj = adj
        self.cost = cost

    def clear(self):
        for v in self.workset:
            self.d[0][v] = self.d[1][v] = self.inf
        del self.workset[0:len(self.workset)]

    def visit(self, q, proc, side, u):
        for j in range(len(self.adj[side][u])):
            v = self.adj[side][u][j]
            if self.d[side][v] > self.d[side][u] + self.cost[side][u][j]:
                self.d[side][v] = self.d[side][u] + self.cost[side][u][j]
                q[side].put((self.d[side][v], v))
                self.workset.append(v)
        proc[side].append(u)
        
    def query(self, s, t):
        if s == t:
            return 0

        self.clear()
        q = [queue.PriorityQueue(), queue.PriorityQueue()]
        proc = [[], []]
        self.visit(q, proc, 0, s)
        self.d[0][s] = 0
        q[0].put((0, s))
        self.workset.append(s)

        self.visit(q, proc, 1, t)
        self.d[1][t] = 0
        q[1].put((0, t))
        self.workset.append(t)

        while not (q[0].empty() and q[1].empty()):
            for side in range(2):
                if q[side].empty():
                    continue
                (dist, u) = q[side].get()
                self.visit(q, proc, side, u)

                if u in proc[1 if side == 0 else 0]:
                    return self.shortestDistance(proc)
        return -1
    
    def shortestDistance(self, proc):
        mergedList = proc[0]
        mergedList.extend(proc[1])
        procSet = set(mergedList)

        distance = self.inf
        for u in procSet:
            if distance > self.d[0][u] + self.d[1][u]:
                distance = self.d[0][u] + self.d[1][u]
        return distance

def readl():
    return map(int, sys.stdin.readline().split())


if __name__ == '__main__':
    n,m = readl()
    adj = [[[] for _ in range(n)], [[] for _ in range(n)]]
    cost = [[[] for _ in range(n)], [[] for _ in range(n)]]
    for e in range(m):
        u,v,c = readl()
        adj[0][u-1].append(v-1)
        cost[0][u-1].append(c)
        adj[1][v-1].append(u-1)
        cost[1][v-1].append(c)
    t, = readl()
    bidij = BiDij(n, adj, cost)
    for i in range(t):
        s, t = readl()
        print(bidij.query(s-1, t-1))
