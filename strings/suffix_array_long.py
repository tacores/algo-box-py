# python3
import sys

symbols = ['$', 'A', 'C', 'G', 'T']

def build_suffix_array(S):
  """suffix文字列のソート順を返す。"""
  """例えば、AACA$ という文字列が与えられたとき、"""
  """ $ < A$ < AACA$ < ACA$ < CA$ であるため、"""
  """[4, 3, 0, 1, 2] を返す。"""

  # 一文字のカウントソート
  order = sort_characters(S)
  # ソート順が等しい文字列をクラス分け
  cls = compute_char_classes(S, order)
  L = 1
  while L < len(S):
    # ソートする文字列を２倍ずつ長くしていく。
    # 文字列の前半分と後半分を比較するだけでソートできる。
    order = sort_doubled(S, L, order, cls)
    cls = update_classes(order, cls, L)
    L *= 2
  return order

def sort_characters(S):
  order = [-1] * len(S)
  count = {}
  for c in symbols:
    count[c] = 0

  for i in range(len(S)):
    count[S[i]] = count[S[i]] + 1
  for j in range(1, len(symbols)):
    count[symbols[j]] = count[symbols[j]] + count[symbols[j - 1]]
  for i in range(len(S) - 1, -1, -1):
    c = S[i]
    count[c] = count[c] - 1
    order[count[c]] = i
  return order

def compute_char_classes(S, order):
  cls = [-1] * len(S)
  cls[order[0]] = 0
  for i in range(1, len(S)):
    if S[order[i]] != S[order[i - 1]]:
      cls[order[i]] = cls[order[i - 1]] + 1
    else:
      cls[order[i]] = cls[order[i - 1]]
  return cls

def sort_doubled(S, L, order, cls):
  count = [0] * len(S)
  newOrder = [-1] * len(S)
  for i in range(len(S)):
    count[cls[i]] = count[cls[i]] + 1
  for j in range(1, len(S)):
    count[j] = count[j] + count[j - 1]
  for i in range(len(S) - 1, -1, -1):
    start = (order[i] - L + len(S)) % (len(S))
    cl = cls[start]
    count[cl] = count[cl] - 1
    newOrder[count[cl]] = start
  return newOrder

def update_classes(newOrder, cls, L):
  n = len(newOrder)
  newCls = [-1] * n
  newCls[newOrder[0]] = 0
  for i in range(1, n):
    cur = newOrder[i]
    prev = newOrder[i - 1]
    mid = (cur + L) % n
    midPrev = (prev + L) % n
    if cls[cur] != cls[prev] or cls[mid] != cls[midPrev]:
      newCls[cur] = newCls[prev] + 1
    else:
      newCls[cur] = newCls[prev]
  return newCls

if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))
