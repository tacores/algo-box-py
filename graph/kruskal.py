#Uses python3
import sys
import math
import queue

# 平面座標を与えられたとき、Kruskalアルゴリズムで
# MSTを計算し、MSTの合計長を返す
def minimum_distance(x, y):
    return kruskal(x, y)

def calc_length(x1, y1, x2, y2):
    length = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return length

def kruskal(x, y):
    n = len(x)
    pointSet = [-1] * n
    pq = queue.PriorityQueue()

    for i in range(n):
        for j in range(n):
            if i < j:
                length = calc_length(x[i], y[i], x[j], y[j])
                pq.put((length, (i, j)))
    result = 0.
    while not pq.empty():
        (length, (u, v)) = pq.get()
        u_root = find(pointSet, u)
        v_root = find(pointSet, v)
        if u_root != v_root:
            union(pointSet, u, v)
            result += length
    return result

def find(pointSet, u):
    while pointSet[u] != -1:
        u = pointSet[u]
    return u

def union(pointSet, u, v):
    u_root = find(pointSet, u)
    v_root = find(pointSet, v)
    if u_root != v_root:
        pointSet[v_root] = u_root

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
