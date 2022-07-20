# python3
import sys

# $で終わる文字列の部分文字列の、トライツリー構築(Compressed)
class Node:
  def __init__ (self, index, length, node_no):
    # 部分文字列を保持する代わりに、text内の位置と長さを保持する
    self.index = index
    self.length = length
    self.node_no = node_no

def build_suffix_tree(text):
  """
  Build a suffix tree of the string text and return a list
  with all of the labels of its edges (the corresponding 
  substrings of the text) in any order.
  """
  tree = dict()
  tree[0] = {}
  head_node = 1

  # 例えば、ABC$ という文字列の場合、ABC$, BC$, C$, $ の順に処理
  for p in range(len(text)):
    suffix = text[p:]
    current_node = 0

    # サブ文字列の先頭から一文字ずつ処理
    i = 0
    while i < len(suffix):
      c = suffix[i]
      cur_str = suffix[i:]
      idx_on_suffix = i
      #print(suffix, cur_str)

      # 現在のノードから、c で始まるエッジが出ている
      if c in tree[current_node]:
        next_node = tree[current_node][c]
        next_str = text[next_node.index : next_node.index + next_node.length]
        next_len = len(next_str)
        cur_len = len(cur_str)

        compare_len = min(next_len, cur_len)
        for u in range(compare_len):
          # 既存のエッジと１文字が一致
          if next_str[u] == cur_str[u]:
            if u != 0: # 0の分は for でインクリメントされるので
              # １文字進む
              i = i + 1
            if u == next_len - 1:
              # 次のノードとの比較に進む
              current_node = next_node.node_no
          else:
            # ①既存のエッジを分割するノードを追加
            new_node = Node(next_node.index, u, head_node)
            cur_node = tree[current_node][c]
            tree[current_node][c] = new_node
            print_nodechange(current_node, c, new_node)

            # ②　①で作成したノードと既存のノードを連結
            if head_node not in tree:
              tree[head_node] = {}
            next_node.index = next_node.index + u
            next_node.length = next_node.length - u
            tree[head_node][next_str[u]] = next_node
            print_nodechange(head_node, next_str[u], next_node)
            current_node = head_node
            head_node = head_node + 1

            # ③　①から分岐するノードを追加            
            if cur_len > u:
              if head_node not in tree:
                tree[head_node] = {}
              new_node = Node(p + idx_on_suffix + u, cur_len - u, head_node)
              tree[current_node][text[p + idx_on_suffix + u]] = new_node
              print_nodechange(current_node, text[p + idx_on_suffix + u], new_node)
              current_node = head_node
              head_node = head_node + 1
              i = len(suffix) #whileループから出るように
            break
      # 現在のノードから、c で始まるエッジが出ていない
      else:
        # 単純にノードを追加
        new_node = Node(p + i, len(suffix) - i, head_node)
        tree[current_node][c] = new_node
        print_nodechange(current_node, c, new_node)
        current_node = head_node
        head_node = head_node + 1
        break
      i = i + 1


  result = []
  #print("*******************")
  for i in tree:
    for j in tree[i]:
      node = tree[i][j]
      print_nodechange(i, j, node)
      next_str = text[node.index : node.index + node.length]
      result.append(next_str)
  #print("*******************")
  return result

def print_nodechange(i, j, node):
  pass
  #print(node.node_no, text[node.index : node.index + node.length], i, j)

if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  result = build_suffix_tree(text)
  print("\n".join(result))