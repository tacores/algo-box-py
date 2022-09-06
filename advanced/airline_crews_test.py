
from airline_crews import max_flow
from airline_crews import assign_crew
from airline_crews import FlowGraph
import unittest

def add_edge(graph, flight_index, crew_can_works, flights, crews):
    for i in range(len(crew_can_works)):
        if crew_can_works[i] == 1:
            graph.add_edge(flight_index, flights + i, 1)    # flight -> crew

def add_edge_src_sink(graph, flights, crews):
    for i in range(flights):
        graph.add_edge(flights + crews, i, 1)
    for i in range(crews):
        graph.add_edge(flights + i, flights + crews + 1, 1)
    
class airline_crews_test(unittest.TestCase):

    def test_sample1(self):
        graph = FlowGraph(3+4+2)    # flights, crews, src, sink
        add_edge(graph, 0, [1,1,0,1], 3, 4)
        add_edge(graph, 1, [0,1,0,0], 3, 4)
        add_edge(graph, 2, [0,0,0,0], 3, 4)
        add_edge_src_sink(graph, 3, 4)

        expected = [1,2,-1]
        max_flow(graph, graph.size() - 2, graph.size() - 1)
        self.assertEqual(assign_crew(graph, 3), expected)

    def test_sample2(self):
        graph = FlowGraph(2+2+2)    # flights, crews, src, sink
        add_edge(graph, 0, [1,1], 2, 2)
        add_edge(graph, 1, [1,0], 2, 2)
        add_edge_src_sink(graph, 2, 2)

        expected = [2,1]
        max_flow(graph, graph.size() - 2, graph.size() - 1)
        self.assertEqual(assign_crew(graph, 2), expected)


if __name__ == '__main__':
    unittest.main()
