#Uses python3
import sys
import math
import queue

# 平面座標を与えられたとき、Kruskalアルゴリズムで
# サブ集合が指定の個数になるまでクラスタリングして
# その時点でのサブ集合間の距離の最小値を返す
def clustering(x, y, k):
    return kruskal(x, y, k)

def calc_length(x1, y1, x2, y2):
    length = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return length

def kruskal(x, y, k):
    n = len(x)
    pointSet = [-1] * n
    pq = queue.PriorityQueue()

    for i in range(n):
        for j in range(n):
            if i < j:
                length = calc_length(x[i], y[i], x[j], y[j])
                pq.put((length, (i, j)))

    result = 0
    while not pq.empty():
        (length, (u, v)) = pq.get()
        u_root = find(pointSet, u)
        v_root = find(pointSet, v)
        if u_root != v_root:
            union(pointSet, u, v)
            num = numOfSubset(pointSet)
            result = length
            if num < k:
                break
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

def numOfSubset(pointSet):
    count = 0
    for i in range(len(pointSet)):
        if pointSet[i] == -1:
            count += 1
    return count

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
