import unittest 
from HW5 import *

class EncryptTestCase(unittest.TestCase):
    # Tests for 'HW5' 
    def setUp(self):
        g1 = {'A': ['B','D','G'], 
              'B': ['A','E','F'], 
              'C': ['F'], 
              'D': ['A','F'], 
              'E': ['B','G'], 
              'F': ['B','C','D'], 
              'G': ['A','E']}
        g2 = {'F': ['D','C','B'], 
              'A': ['G','D','B'], 
              'B': ['F','A','E'], 
              'E': ['G','B'], 
              'C': ['F'], 
              'D': ['F','A'], 
              'G': ['A','E'], 
              'F': ['D','C','B']}
        g3 = {'B': [('E',3),('C',5)], 
              'F': [], 
              'C': [('F',2)], 
              'A': [('D',3),('B',2),], 
              'D': [('C',1)], 
              'E': [('F',4)]}
        g4 = {'B': [('E',3),('C',5)], 
              'F': [], 
              'C': [('F',2)], 
              'A': [('D',3),('B',2),], 
              'D': [('C')], 
              'E': [('F',4)]}

        self.graph1 = Graph(g1)
        self.graph2 = Graph(g2)
        self.graph3 = Graph(g3)
        self.graph4 = Graph(g4)

    def test_node_not_in_graph_bfs(self):
        self.assertEqual(self.graph1.bfs('Q'), 'error: start node not in graph') 

    def test_node_not_in_graph_dfs(self):
        self.assertEqual(self.graph1.dfs('R'), 'error: start node not in graph')

    def test_node_not_in_graph_dijkstra(self):
        self.assertEqual(self.graph1.dijkstra('W'), 'error: start node not in graph')

    def test_unweighted_bfs_A(self):
        self.assertEqual(self.graph1.bfs('A'), ['A', 'B', 'D', 'G', 'E', 'F', 'C'])

    def test_unweighted_bfs_B(self):
        self.assertEqual(self.graph1.bfs('B'), ['B', 'A', 'E', 'F', 'D', 'G', 'C'])

    def test_unweighted_bfs_C(self):
        self.assertEqual(self.graph1.bfs('C'), ['C', 'F', 'B', 'D', 'A', 'E', 'G'])

    def test_unweighted_bfs_D(self):
        self.assertEqual(self.graph1.bfs('D'), ['D', 'A', 'F', 'B', 'G', 'C', 'E'])

    def test_unweighted_bfs_E(self):
        self.assertEqual(self.graph1.bfs('E'), ['E', 'B', 'G', 'A', 'F', 'D', 'C'])

    def test_unweighted_bfs_F(self):
        self.assertEqual(self.graph1.bfs('F'), ['F', 'B', 'C', 'D', 'A', 'E', 'G'])

    def test_unweighted_bfs_G(self):
        self.assertEqual(self.graph1.bfs('G'), ['G', 'A', 'E', 'B', 'D', 'F', 'C'])

    def test_weighted_bfs(self):
        self.assertEqual(self.graph3.bfs('A'), ['A', 'B', 'D', 'C', 'E', 'F'])

    def test_non_alphabetical_graph_bfs(self):
        self.assertEqual(self.graph2.bfs('A'), ['A', 'B', 'D', 'G', 'E', 'F', 'C'])

    def test_one_node_bfs(self):
        graph5 = Graph({'A':[]})
        self.assertEqual(graph5.bfs('A'), ['A'])

    def test_one_node_dfs(self):
        graph5 = Graph({'A':[]})
        self.assertEqual(graph5.dfs('A'), ['A'])

    def test_unweighted_dfs_A(self):
        self.assertEqual(self.graph1.dfs('A'), ['A', 'B', 'E', 'G', 'F', 'C', 'D'])
    
    def test_unweighted_dfs_B(self):
        self.assertEqual(self.graph1.dfs('B'), ['B', 'A', 'D', 'F', 'C', 'G', 'E'])

    def test_unweighted_dfs_C(self):
        self.assertEqual(self.graph1.dfs('C'), ['C', 'F', 'B', 'A', 'D', 'G', 'E'])

    def test_unweighted_dfs_D(self):
        self.assertEqual(self.graph1.dfs('D'), ['D', 'A', 'B', 'E', 'G', 'F', 'C'])

    def test_unweighted_dfs_E(self):
        self.assertEqual(self.graph1.dfs('E'), ['E', 'B', 'A', 'D', 'F', 'C', 'G'])

    def test_unweighted_dfs_F(self):
        self.assertEqual(self.graph1.dfs('F'), ['F', 'B', 'A', 'D', 'G', 'E', 'C'])

    def test_unweighted_dfs_G(self):
        self.assertEqual(self.graph1.dfs('G'), ['G', 'A', 'B', 'E', 'F', 'C', 'D'])

    def test_weighted_dfs(self):
        self.assertEqual(self.graph3.dfs('A'), ['A', 'B', 'C', 'F', 'E', 'D'])

    def test_non_alphabetical_dfs(self):
        self.assertEqual(self.graph2.dfs('A'), ['A', 'B', 'E', 'G', 'F', 'C', 'D'])

    def test_dijkstra_A(self):
        self.assertEqual(self.graph3.dijkstra('A'), {'A': 0, 'B': 2, 'C': 4, 'D': 3, 'E': 5, 'F': 6})

    def test_dijkstra_unweighted_edges(self):
        self.assertEqual(self.graph4.dijkstra('A'), {'A': 0, 'B': 2, 'C': 4, 'D': 3, 'E': 5, 'F': 6})


if __name__ == '__main__':unittest.main(exit=False)