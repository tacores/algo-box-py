# python3
from sys import stdin
import math
from itertools import chain, combinations

"""
連立不等式を満たす変数（食事の各ディッシュの数）の集合のうち
満足度を最大にする変数の組を求めるアルゴリズム

n個の不等式、m個の変数、A*amount <= b の連立不等式、cは（満足度/個数）

1. 各個数 >= 0 という m個の不等式と、無限大判定用の不等式を追加する
2. n+m+1個の不等式の中からm個を選ぶ全サブセットを取得する
3. サブセットに含まれる不等式を等式として、連立方程式を解く
4. その解が、サブセットに含まれない不等式の条件を満たすか確認する
5. 満足度がMaxとなる解を保持して、結果として返す
"""
def solve_diet_problem(n, m, A, b, c):  

  # A,b に、amount1 >= 0, amount2 >= 0 ... の不等式を追加
  for i in range(m):
    lst = [0] * m
    lst[i] = -1 # 不等式を「大なり」にするためマイナス
    A.append(lst)
    b.append(0)
  
  # sum(amount(n)) <= 10の9乗 の不等式を追加（解ありとInifinityを区別するため）
  lst = [1] * m
  A.append(lst)
  b.append(10**9)
  
  # n+m+1個の不等式の中からm個を選ぶ全サブセットを計算する
  ps = powerset([i for i in range(n+m+1)])      # 長さで絞らない全サブセット
  ps_nm = [x for x in ps if len(x) == m] # 要素数8で絞ったサブセット

  # サブセットのm個の不等式を等式として連立方程式を解く
  max_pleasure = -float("inf")
  max_result = [0] * m
  for x in ps_nm:
    equation = [[] for _ in range(m)]
    for i in range(m):
      row = x[i]
      equation[i] = A[row] + [b[row]]
    result = SolveEquation(equation)
    if result == None:
      continue

    # 連立方程式の解が、他のn個の不等式を満たすか確認する
    satisfied = True
    for row in range(n + m + 1):
      s = 0
      if row not in x:
        for i in range(m):
          s += A[row][i] * result[i]
      else:
        continue
      if s > b[row]:   # 不等式を満たさない
        satisfied = False
        break
    pleasure = 0
    if satisfied: # 全ての不等式を満たした
      for i in range(m):
        pleasure += result[i] * c[i]

      # max(sum(amount*pleasure)) を満たす amount が求める解となる 
      if max_pleasure < pleasure:
        max_pleasure = pleasure
        max_result = result.copy()
  
  anst = 0
  if max_pleasure == -float("inf"):    # 全ての不等式を満たすケースが無かった
    anst = -1
  elif math.isclose(sum(max_result), 10**9): # 10の9乗より大きい倍はInifinityとする
    anst = 1

  return [anst, max_result]

# powerset（べき集合）を作る
def powerset(iterable):
  "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
  s = list(iterable)
  return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

# 連立方程式を解く
def SolveEquation(a):
  size = len(a)
  rows = size
  vals = size

  for pivot in range(rows):
    #printEquation(a)
    # ピボット行のピボット列が0以外になるように行を入れ替える
    for r in range(pivot, rows):
      if a[r][pivot] != 0:
        if r == pivot:
          break
        a[pivot], a[r] = a[r], a[pivot]
        break
    
    # ピボットの係数を１にスケールする
    scale = a[pivot][pivot]
    if scale == 0:
      return None
    for n in range(vals + 1):
      a[pivot][n] /= scale

    # ピボット行を加減算して、ピボット行以外の行から変数を1つ消す
    for r in range(rows):
      if r != pivot:
        scale = a[r][pivot]
        for n in range(vals + 1):
          a[r][n] -= a[pivot][n] * scale
    #printEquation(a)
  
  result = []
  for v in range(vals):
    result.append(a[v][vals])
  return result


# main
if __name__ == '__main__':
  n, m = list(map(int, stdin.readline().split()))
  A = []
  for i in range(n):
    A += [list(map(int, stdin.readline().split()))]
  b = list(map(int, stdin.readline().split()))
  c = list(map(int, stdin.readline().split()))

  anst, ansx = solve_diet_problem(n, m, A, b, c)

  if anst == -1:
    print("No solution")
  if anst == 0:  
    print("Bounded solution")
    print(' '.join(list(map(lambda x : '%.18f' % x, ansx))))
  if anst == 1:
    print("Infinity")
    
