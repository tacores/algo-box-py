# python3

"""
二部グラフ（Bipartite）の最大マッチングを計算する。
フライトと乗務員の最大マッチング問題。

src->フライト、乗務員->sink の接続を追加してMaxflow問題として解く。
"""

class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

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
    flights, crews = map(int, input().split())
    adj_matrix = [list(map(int, input().split())) for i in range(flights)]

    # flights, crews, src, sink の順でノードを作る
    graph = FlowGraph(flights + crews + 2) 
    s = flights + crews       # src は最後尾から2番目
    t = flights + crews + 1   # sink(target) は最後尾とする

    # flight -> crew
    for i in range(flights):
        for j in range(crews):
            if adj_matrix[i][j] == 1:
                graph.add_edge(i, flights + j, 1)
    # src -> flight
    for i in range(flights):
        graph.add_edge(flights + crews, i, 1)
    # crew -> sink
    for i in range(crews):
        graph.add_edge(flights + i, flights + crews + 1, 1)

    return (graph, flights, crews)

def max_flow(graph, from_, to):
    """
    graphネットワークの from から to への Maxflow を計算する
    """
    path = bfs(graph, from_, to)
    while path != None:
        #print(graph)
        flow = min(graph.get_edge(id).capacity - graph.get_edge(id).flow for id in path)
        for id in path:
            graph.add_flow(id, flow)
        path = bfs(graph, from_, to)
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

# graphから出力のデータ形式を作る
def assign_crew(graph, number_of_flights):
    # 各フライトにどの乗務員を割り当てるかの配列
    result = [-1] * number_of_flights
    for i in range(number_of_flights):
        ids = graph.get_ids(i)
        for id in ids:
            edge = graph.get_edge(id)
            if edge.flow == 1:
                flight = edge.u
                crew = edge.v - number_of_flights
                assert result[flight] == -1
                result[flight] = crew + 1   # 1-based index
    return result

if __name__ == '__main__':
    graph, flights, crews = read_data()
    # srcからsinkへのMaxflowを計算する
    # src は最後尾から2番目、sink は最後尾
    max_flow(graph, graph.size() - 2, graph.size() - 1)
    result = assign_crew(graph, flights)
    print(" ".join(str(v) for v in result))
