# python3

"""
各エッジに最低流量が設定された有向グラフで、フローサイクルを探索する。
フローサイクルが存在しない場合は"NO"を出力し、
存在する場合は"YES"と、各エッジの流量を出力する。
最大フロー問題として解いている。
"""

class Edge:

    def __init__(self, u, v, capacity, lb):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.lb = lb
        self.flow = 0

class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]
        self.dv = [0] * (n + 2) # 各ノードの最低流量の流入と流出を保持する
        self.DD = 0 # ソースからエッジへの流量

    def add_edge(self, from_, to, capacity, lb):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity, lb)
        backward_edge = Edge(to, from_, 0, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)
        self.dv[from_] += lb
        self.dv[to] -= lb

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow
    
    # for debugging
    def __str__(self):
        str = "************************************\n"
        for edge in self.edges:
            str = "{} {}, {}, {}, {}\n".format(str, edge.u+1, edge.v+1, edge.flow, edge.capacity)
        return str

# 標準入力から読み込み
def read_data():
    N, E = map(int, input().split())
    edges = []
    for _ in range(E):
        edges.append(map(int, input().split()))
    return (N, E, edges)

def construct_graph(N, E, edges):
    # N + source + sink
    graph = FlowGraph(N + 2) 
    for (u, v, l, c) in edges:
        # キャパシティから最低流量を引いておく
        graph.add_edge(u - 1, v - 1, c -l, l)
    
    for v in range(N):
        if graph.dv[v] < 0:
            # 最低流量の流出の方が大きい場合は、ソースノードからの流入エッジを追加する
            graph.add_edge(N, v, -graph.dv[v], 0)
        else:
            # 最低流量の流入の方が大きい場合は、シンクノードへの流出エッジを追加する
            graph.add_edge(v, N + 1, graph.dv[v], 0)
            # ソースからエッジへの流量
            graph.DD += graph.dv[v]
    return graph

def max_flow(graph, from_, to):
    """
    graphネットワークの from から to への Maxflow を計算する
    """
    path = bfs(graph, from_, to)
    result = 0
    while path != None:
        #print(graph)
        flow = min(graph.get_edge(id).capacity - graph.get_edge(id).flow for id in path)
        for id in path:
            graph.add_flow(id, flow)
        result += flow
        path = bfs(graph, from_, to)
    return result
    #print(graph)

#find path by using BFS
def bfs(graph, s, t):
    queue = [s]
    paths = {s:[]}
    explored = [s]
    if s == t:
        return paths[s]
    while queue: 
        u = queue.pop(0)
        for id in graph.get_ids(u):
            edge = graph.get_edge(id)
            assert u == edge.u
            v = edge.v
            if (edge.capacity - edge.flow > 0) and v not in explored:
                paths[v] = paths[u] + [id]
                explored.append(v)
                if v == t:
                    return paths[v]
                queue.append(v)
    return None

def solve(graph, N, E):
    # source->sink のMaxflowを計算する
    flow = max_flow(graph, N, N + 1)
    result = []
    if flow != graph.DD:
        result.append("NO")
    else:
        result.append("YES")
        for i in range(E):
            forward_edge = graph.edges[i * 2]
            # 最低流量分を事前にキャパシティから引いてあるので、
            # 求めたフローに最低流量を加算したものが解になる
            result.append(forward_edge.flow + forward_edge.lb)
    return result

if __name__ == '__main__':
    (N, E, edges) = read_data()
    graph = construct_graph(N, E, edges)
    result = solve(graph, N, E)
    for line in result:
        print(line)

