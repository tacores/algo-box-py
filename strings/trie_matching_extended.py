# python3
import sys

# text中の、patterns の出現位置を出力する。
# patternsからトライツリーを構築し、
# それをtextのサブ文字列に順次当てはめる。

class Trie:
	def __init__ (self, patterns):
		self.trie = self.build_trie(patterns)
	
	def trie(self):
		return self.trie

	def build_trie(self, patterns):
		tree = dict()
		head_node = 0
		tree[0] = {}
		
		for pattern in patterns:
			current_node = 0
			for i in range(len(pattern)):
				p = pattern[i]
				found = False
				# ノードが既存の場合は移動するだけ
				if p in tree[current_node]:
					current_node = tree[current_node][p]
					found = True

				# ノードが無い場合は作る
				if not found:
					head_node = head_node + 1
					tree[current_node][p] = head_node
					tree[head_node] = {}
					current_node = head_node
				
				# パターンの終端の場合、$ノードを作る
				if i == len(pattern) - 1:
					head_node = head_node + 1
					tree[current_node]['$'] = head_node
					tree[head_node] = {}
					current_node = head_node
					pass

		return tree
	
	def find(self, text):
		current_node = 0

		for i in range(len(text)):
			c = text[i]
			if c in self.trie[current_node]:
				current_node = self.trie[current_node][c]
			else:
				break

			if '$' in self.trie[current_node]:
				return True

		return False


def solve (text, n, patterns):
	result = []

	trie = Trie(patterns)

	for i in range(len(text)):
		if trie.find(text[i:]):
			result.append(i)

	return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
