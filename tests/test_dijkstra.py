# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import unittest

import retworkx


class TestDijkstraDiGraph(unittest.TestCase):
    def setUp(self):
        self.graph = retworkx.PyDiGraph()
        self.a = self.graph.add_node("A")
        self.b = self.graph.add_node("B")
        self.c = self.graph.add_node("C")
        self.d = self.graph.add_node("D")
        self.e = self.graph.add_node("E")
        self.f = self.graph.add_node("F")
        edge_list = [
            (self.a, self.b, 7),
            (self.c, self.a, 9),
            (self.a, self.d, 14),
            (self.b, self.c, 10),
            (self.d, self.c, 2),
            (self.d, self.e, 9),
            (self.b, self.f, 15),
            (self.c, self.f, 11),
            (self.e, self.f, 6),
        ]
        self.graph.add_edges_from(edge_list)

    def test_dijkstra(self):
        path = retworkx.digraph_dijkstra_shortest_path_lengths(
            self.graph, self.a, lambda x: float(x), self.e)
        expected = {4: 23.0}
        self.assertEqual(expected, path)

    def test_dijkstra_path(self):
        paths = retworkx.digraph_dijkstra_shortest_paths(self.graph, self.a)
        expected = {
            # a -> b
            1: [0, 1],
            # a -> c: a, d, c
            2: [0, 3, 2],
            # a -> d
            3: [0, 3],
            # a -> e: a, d, e
            4: [0, 3, 4],
            # a -> f: a, b, f
            5: [0, 1, 5],
        }
        self.assertEqual(expected, paths)

    def test_dijkstra_path_with_weight_fn(self):
        paths = retworkx.digraph_dijkstra_shortest_paths(
            self.graph, self.a, weight_fn=lambda x: x)
        expected = {
            1: [0, 1],
            2: [0, 1, 2],
            3: [0, 3],
            4: [0, 3, 4],
            5: [0, 1, 5],
        }
        self.assertEqual(expected, paths)

    def test_dijkstra_path_with_target(self):
        paths = retworkx.digraph_dijkstra_shortest_paths(self.graph, self.a,
                                                         target=self.e)
        expected = {
            4: [0, 3, 4],
        }
        self.assertEqual(expected, paths)

    def test_dijkstra_path_with_weight_fn_and_target(self):
        paths = retworkx.digraph_dijkstra_shortest_paths(
            self.graph, self.a, target=self.e, weight_fn=lambda x: x)
        expected = {
            4: [0, 3, 4],
        }
        self.assertEqual(expected, paths)

    def test_dijkstra_path_undirected(self):
        paths = retworkx.digraph_dijkstra_shortest_paths(self.graph, self.a,
                                                         as_undirected=True)
        expected = {
            1: [0, 1],
            2: [0, 2],
            3: [0, 3],
            4: [0, 3, 4],
            5: [0, 1, 5],
        }
        self.assertEqual(expected, paths)

    def test_dijkstra_path_undirected_with_weight_fn(self):
        paths = retworkx.digraph_dijkstra_shortest_paths(self.graph, self.a,
                                                         weight_fn=lambda x: x,
                                                         as_undirected=True)
        expected = {
            1: [0, 1],
            2: [0, 2],
            3: [0, 3],
            4: [0, 3, 4],
            5: [0, 1, 5],
        }
        self.assertEqual(expected, paths)

    def test_dijkstra_path_undirected_with_target(self):
        paths = retworkx.digraph_dijkstra_shortest_paths(self.graph, self.a,
                                                         target=self.e,
                                                         as_undirected=True)
        expected = {
            4: [0, 3, 4],
        }
        self.assertEqual(expected, paths)

    def test_dijkstra_path_undirected_with_weight_fn_and_target(self):
        paths = retworkx.digraph_dijkstra_shortest_paths(self.graph, self.a,
                                                         target=self.e,
                                                         weight_fn=lambda x: x,
                                                         as_undirected=True)
        expected = {
            4: [0, 3, 4],
        }
        self.assertEqual(expected, paths)

    def test_dijkstra_with_no_goal_set(self):
        path = retworkx.digraph_dijkstra_shortest_path_lengths(
            self.graph, self.a, lambda x: 1)
        expected = {1: 1.0, 2: 2.0, 3: 1.0, 4: 2.0, 5: 2.0}
        self.assertEqual(expected, path)

    def test_dijkstra_with_no_path(self):
        g = retworkx.PyDiGraph()
        a = g.add_node('A')
        g.add_node('B')
        path = retworkx.digraph_dijkstra_shortest_path_lengths(
            g, a, lambda x: float(x))
        expected = {}
        self.assertEqual(expected, path)

    def test_dijkstra_path_with_no_path(self):
        g = retworkx.PyDiGraph()
        a = g.add_node('A')
        g.add_node('B')
        path = retworkx.digraph_dijkstra_shortest_paths(
            g, a)
        expected = {}
        self.assertEqual(expected, path)

    def test_dijkstra_with_disconnected_nodes(self):
        g = retworkx.PyDiGraph()
        a = g.add_node('A')
        b = g.add_child(a, 'B', 1.2)
        g.add_node('C')
        g.add_parent(b, 'D', 2.4)
        path = retworkx.digraph_dijkstra_shortest_path_lengths(
            g, a, lambda x: x)
        expected = {1: 1.2}
        self.assertEqual(expected, path)

    def test_dijkstra_with_graph_input(self):
        g = retworkx.PyGraph()
        g.add_node(0)
        with self.assertRaises(TypeError):
            retworkx.digraph_dijkstra_shortest_path_lengths(g, 0, lambda x: x)


class TestDijkstraGraph(unittest.TestCase):

    def setUp(self):
        self.graph = retworkx.PyGraph()
        self.a = self.graph.add_node("A")
        self.b = self.graph.add_node("B")
        self.c = self.graph.add_node("C")
        self.d = self.graph.add_node("D")
        self.e = self.graph.add_node("E")
        self.f = self.graph.add_node("F")
        self.graph.add_edge(self.a, self.b, 7)
        self.graph.add_edge(self.c, self.a, 9)
        self.graph.add_edge(self.a, self.d, 14)
        self.graph.add_edge(self.b, self.c, 10)
        self.graph.add_edge(self.d, self.c, 2)
        self.graph.add_edge(self.d, self.e, 9)
        self.graph.add_edge(self.b, self.f, 15)
        self.graph.add_edge(self.c, self.f, 11)
        self.graph.add_edge(self.e, self.f, 6)

    def test_dijkstra(self):
        path = retworkx.graph_dijkstra_shortest_path_lengths(
            self.graph, self.a, lambda x: float(x), self.e)
        expected = {4: 20.0}
        self.assertEqual(expected, path)

    def test_dijkstra_path(self):
        path = retworkx.graph_dijkstra_shortest_paths(
            self.graph, self.a, weight_fn=lambda x: float(x), target=self.e)
        expected = {
            4: [0, 3, 4]
        }
        self.assertEqual(expected, path)

    def test_dijkstra_with_no_goal_set(self):
        path = retworkx.graph_dijkstra_shortest_path_lengths(
            self.graph, self.a, lambda x: 1)
        expected = {1: 1.0, 2: 1.0, 3: 1.0, 4: 2.0, 5: 2.0}
        self.assertEqual(expected, path)

    def test_dijkstra_path_with_no_goal_set(self):
        path = retworkx.graph_dijkstra_shortest_paths(
            self.graph, self.a)
        expected = {
            1: [0, 1],
            2: [0, 2],
            3: [0, 3],
            4: [0, 3, 4],
            5: [0, 1, 5],
        }
        self.assertEqual(expected, path)

    def test_dijkstra_with_no_path(self):
        g = retworkx.PyGraph()
        a = g.add_node('A')
        g.add_node('B')
        path = retworkx.graph_dijkstra_shortest_path_lengths(
            g, a, lambda x: float(x))
        expected = {}
        self.assertEqual(expected, path)

    def test_dijkstra_path_with_no_path(self):
        g = retworkx.PyGraph()
        a = g.add_node('A')
        g.add_node('B')
        path = retworkx.graph_dijkstra_shortest_paths(
            g, a, weight_fn=lambda x: float(x))
        expected = {}
        self.assertEqual(expected, path)

    def test_dijkstra_with_disconnected_nodes(self):
        g = retworkx.PyDiGraph()
        a = g.add_node('A')
        b = g.add_node('B')
        g.add_edge(a, b, 1.2)
        g.add_node('C')
        d = g.add_node('D')
        g.add_edge(b, d, 2.4)
        path = retworkx.digraph_dijkstra_shortest_path_lengths(
            g, a, lambda x: round(x, 1))
        # Computers never work:
        expected = {1: 1.2, 3: 3.5999999999999996}
        self.assertEqual(expected, path)

    def test_dijkstra_graph_with_digraph_input(self):
        g = retworkx.PyDAG()
        g.add_node(0)
        with self.assertRaises(TypeError):
            retworkx.graph_dijkstra_shortest_path_lengths(
                g, 0, lambda x: x)
