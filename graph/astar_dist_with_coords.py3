#!/usr/bin/python3

import sys
import queue
import math

class AStar:
    def __init__(self, n, m, adj, cost, x, y):
        self.n = n;
        self.m = m
        self.adj = adj
        self.cost = cost
        self.inf = n*10**6
        self.d = [self.inf]*n
        self.h = [self.inf]*n
        self.visited = [False]*n
        self.workset = []
        # Coordinates of the nodes
        self.x = x
        self.y = y

    def clear(self):
        for v in self.workset:
            self.d[v] = self.inf
            self.visited[v] = False;
        del self.workset[0:len(self.workset)]

    def visit(self, q, u):
        for j in range(len(self.adj[u])):
            v = self.adj[u][j]
            if self.d[v] > self.d[u] + self.cost[u][j]:
                self.d[v] = self.d[u] + self.cost[u][j]
                h = self.d[v] + self.potential(v)
                #print('p : ', p)
                q.put((h, v))
                self.workset.append(v)

    # Returns the distance from s to t in the graph
    def query(self, s, t):
        self.clear()
        self.s = s
        self.t = t
        q = queue.PriorityQueue()

        q.put((0, s))
        self.d[s] = 0
        self.workset.append(s)

        while not q.empty():
            (h, u) = q.get()
            self.visit(q, u)

            # u がゴールの場合、探索を打ち切る
            # 推測値が実際の距離を上回らない場合は、これで最適解が出る
            if u == t:
                break

        if self.d[t] != self.inf:
            return self.d[t]
        else:
            return -1


    # ポテンシャルとして、2次元平面上の、vからtまでの距離を返す   
    def potential(self, v):
        t = self.t
        result = math.sqrt((self.x[v] - self.x[t]) ** 2 + (self.y[v] - self.y[t]) ** 2)
        #print('potential : ', result)
        return result


def readl():
    return map(int, sys.stdin.readline().split())

if __name__ == '__main__':
    n,m = readl()
    x = [0 for _ in range(n)]
    y = [0 for _ in range(n)]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for i in range(n):
        a, b = readl()
        x[i] = a
        y[i] = b
    for e in range(m):
        u,v,c = readl()
        adj[u-1].append(v-1)
        cost[u-1].append(c)
    t, = readl()
    astar = AStar(n, m, adj, cost, x, y)
    for i in range(t):
        s, t = readl()
        print(astar.query(s-1, t-1))
