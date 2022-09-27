#uses python3

import sys
import threading

# 直属の上司（隣接するノード）と一緒に呼ばないという条件で、
# 幸福度が最大となるようにパーティの参加者を選ぶ問題

class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []

def ReadTree():
    size = int(input())
    tree = [Vertex(w) for w in map(int, input().split())]
    for i in range(1, size):
        a, b = list(map(int, input().split()))
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree

# 深さ優先
def dfs(tree, vertex, parent, grand_parent, fun, children, grand_children):
    for child in tree[vertex].children:
        if child != parent:
            dfs(tree, child, vertex, parent, fun, children, grand_children)
    
    # 子ノードの幸福度合計
    children_total = 0
    for c in children[vertex]:
        children_total += fun[c]

    # 孫ノードの幸福度合計    
    grand_children_total = 0
    for g in grand_children[vertex]:
        grand_children_total += fun[g]

    if len(tree[vertex].children) < 1 and parent != -1: # leaf
        # leaf の場合は自身のweightが幸福度
        fun[vertex] = tree[vertex].weight
    else:   # not leaf
        # 「自分＋孫ノードの合計」と「子ノードの合計」の大きい方を幸福度とする
        fun[vertex] = max(tree[vertex].weight + grand_children_total, children_total)

    # 子と孫を、親ノードから参照できるように保存しておく
    if parent != -1:
        children[parent].append(vertex)
    if grand_parent != -1:
        grand_children[grand_parent].append(vertex)

def MaxWeightIndependentTreeSubset(tree):
    size = len(tree)
    if size == 0:
        return 0
    fun = [0] * size
    children = [[] for _ in range(size)]
    grand_children = [[] for _ in range(size)]
    dfs(tree, 0, -1, -1, fun, children, grand_children)

    return fun[0]


def main():
    tree = ReadTree();
    weight = MaxWeightIndependentTreeSubset(tree);
    print(weight)


if __name__ == '__main__':
    # This code is used to avoid stack overflow issues
    sys.setrecursionlimit(10**6) # max depth of recursion
    threading.stack_size(2**26)  # new thread will get stack of such size
    # This is to avoid stack overflow issues
    threading.Thread(target=main).start()
