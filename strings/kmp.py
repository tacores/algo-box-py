# python3
import sys

"""Knuth-Morris-Pratt アルゴリズム"""

def find_pattern(pattern, text):
  """text中に出てくる pattern の位置を全て返す"""
  S = pattern + '$' + text
  prefix = compute_prefix_function(S)
  result = []

  for i in range(len(pattern) + 1, len(S)):
    if prefix[i] == len(pattern):
      result.append(i - 2 * len(pattern))
  return result

def compute_prefix_function(p):
  """prefix function を計算する"""
  s = [-1] * len(p)
  s[0] = 0
  border = 0

  for i in range(1, len(p)):
    while (border > 0) and (p[i] != p[border]):
      border = s[border - 1]
    if p[i] == p[border]:
      border = border + 1
    else:
      border = 0
    s[i] = border
  return s


if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))

