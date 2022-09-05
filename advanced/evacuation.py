# python3

"""
Residual Network(残差ネットワーク)を用いた Maxflow計算
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
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph

def max_flow(graph, from_, to):
    """
    graphネットワークの from から to への Maxflow を返す
    """
    path = bfs(graph, from_, to)
    while path != None:
        #print(graph)
        flow = min(graph.get_edge(id).capacity - graph.get_edge(id).flow for id in path)
        for id in path:
            graph.add_flow(id, flow)
        path = bfs(graph, from_, to)
    #print(graph)

    sum_flow = 0
    for i in range(graph.size()):
        for id in graph.get_ids(i):
            edge = graph.get_edge(id)
            # to に流入するフローの合計を Maxflow とする
            if edge.v == to:
                sum_flow += edge.flow
    return sum_flow

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

if __name__ == '__main__':
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))
