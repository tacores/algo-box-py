# python3
from collections import deque
import sys
import threading

# 2-SAT（充足可能性問題）を解く。
# (x1 V y1)(~x1 V z2)(~y2 V z3)・・・
# を満たす変数が存在するか、存在する場合はその値を返す。

# SCC(Strongly Connected Components)を返す
def scc(N, G, RG):
    order = []
    used = [0]*N
    def dfs(s):
        used[s] = 1
        for t in G[s]:
            if not used[t]:
                dfs(t)
        order.append(s)
    for i in range(N):
        if not used[i]:
            dfs(i)
    group = [-1]*N
    label = 0
    order.reverse()
    for s in order:
        if group[s] != -1:
            continue
        que = deque([s])
        group[s] = label
        while que:
            v = que.popleft()
            for w in RG[v]:
                if group[w] != -1:
                    continue
                que.append(w)
                group[w] = label
        label += 1
    return group # topological ordering

# add (a ∨ b)
# a =  x_i if neg_i = 0
# a = ~x_i if neg_i = 1
def add_edge(i, neg_i, j, neg_j, N, G, RG):
    if neg_i:
        i0 = i + N; i1 = i
    else:
        i0 = i; i1 = i + N
    if neg_j:
        j0 = j + N; j1 = j
    else:
        j0 = j; j1 = j + N
    # add (~a ⇒ b)
    G[i1].append(j0); RG[j0].append(i1)
    # add (~b ⇒ a)
    G[j1].append(i0); RG[i0].append(j1)

# check if the formula is satisfiable
def check(N, group):
    for i in range(N):
        if group[i] == group[i+N]:
            return False
    return True

# assign values to variables
# [1, 1, 0, 1, 1] のような形式
def assign(N, group):
    res = [0]*N
    for i in range(N):
        if group[i] > group[i+N]:
            res[i] = 1
    return res

# 充足可能かどうかを判定する
# 充足可能な場合は、条件を満たす変数の値を返す
# [1, 2, -3, 4] のような形式で返す
def isSatisfiable(N, G, RG):
    group = scc(2*N, G, RG)
    if not check(N, group):
        return None
    else:
        result = assign(N, group)
        answer = [0] * N
        for i in range(N):
            if result[i] == 1:
                answer[i] = result[i] * (i + 1)
            else:
                answer[i] = -1 * (i + 1)
        return answer

def main():
    N, m = map(int, input().split())
    G = [[] for i in range(2*N)]
    RG = [[] for i in range(2*N)]
    for i in range(m):
        a, b = map(int, input().split())
        a_negate = 0 if a > 0 else 1
        b_negate = 0 if b > 0 else 1
        if a < 0:
            a = -a
        if b < 0:
            b = -b
        add_edge(a - 1, a_negate, b - 1, b_negate, N, G, RG)

    result = isSatisfiable(N, G, RG)
    if result == None:
        print("UNSATISFIABLE")
    else:
        print("SATISFIABLE")
        print(" ".join([str(v) for v in result]))


if __name__ == '__main__':
    sys.setrecursionlimit(10**6)
    threading.stack_size(2**26)
    threading.Thread(target=main).start()


