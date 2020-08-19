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


class TestAstarDigraph(unittest.TestCase):

    def test_astar_null_heuristic(self):
        g = retworkx.PyDAG()
        a = g.add_node("A")
        b = g.add_node("B")
        c = g.add_node("C")
        d = g.add_node("D")
        e = g.add_node("E")
        f = g.add_node("F")
        g.add_edge(a, b, 7)
        g.add_edge(c, a, 9)
        g.add_edge(a, d, 14)
        g.add_edge(b, c, 10)
        g.add_edge(d, c, 2)
        g.add_edge(d, e, 9)
        g.add_edge(b, f, 15)
        g.add_edge(c, f, 11)
        g.add_edge(e, f, 6)
        path = retworkx.digraph_astar_shortest_path(g, a,
                                                    lambda goal: goal == "E",
                                                    lambda x: float(x),
                                                    lambda y: 0)
        expected = [a, d, e]
        self.assertEqual(expected, path)

    def test_astar_manhattan_heuristic(self):
        g = retworkx.PyDAG()
        a = g.add_node((0., 0.))
        b = g.add_node((2., 0.))
        c = g.add_node((1., 1.))
        d = g.add_node((0., 2.))
        e = g.add_node((3., 3.))
        f = g.add_node((4., 2.))
        no_path = g.add_node((5., 5.))  # no path to node
        g.add_edge(a, b, 2.)
        g.add_edge(a, d, 4.)
        g.add_edge(b, c, 1.)
        g.add_edge(b, f, 7.)
        g.add_edge(c, e, 5.)
        g.add_edge(e, f, 1.)
        g.add_edge(d, e, 1.)

        def heuristic_func(f):
            x1, x2 = f
            return abs(x2 - x1)

        def finish_func(node, x):
            return x == g.get_node_data(node)

        expected = [
            [0],
            [0, 1],
            [0, 1, 2],
            [0, 3],
            [0, 3, 4],
            [0, 3, 4, 5],
        ]

        for index, end in enumerate([a, b, c, d, e, f]):
            path = retworkx.digraph_astar_shortest_path(
                g, a, lambda finish: finish_func(end, finish),
                lambda x: float(x), heuristic_func)
            self.assertEqual(expected[index], path)

        with self.assertRaises(retworkx.NoPathFound):
            retworkx.digraph_astar_shortest_path(
                g, a, lambda finish: finish_func(no_path, finish),
                lambda x: float(x), heuristic_func)

    def test_astar_digraph_with_graph_input(self):
        g = retworkx.PyGraph()
        g.add_node(0)
        with self.assertRaises(TypeError):
            retworkx.digraph_astar_shortest_path(g, 0, lambda x: x,
                                                 lambda y: 1, lambda z: 0)


class TestAstarGraph(unittest.TestCase):

    def test_astar_null_heuristic(self):
        g = retworkx.PyGraph()
        a = g.add_node("A")
        b = g.add_node("B")
        c = g.add_node("C")
        d = g.add_node("D")
        e = g.add_node("E")
        f = g.add_node("F")
        g.add_edge(a, b, 7)
        g.add_edge(c, a, 9)
        g.add_edge(a, d, 14)
        g.add_edge(b, c, 10)
        g.add_edge(d, c, 2)
        g.add_edge(d, e, 9)
        g.add_edge(b, f, 15)
        g.add_edge(c, f, 11)
        g.add_edge(e, f, 6)
        path = retworkx.graph_astar_shortest_path(g, a,
                                                  lambda goal: goal == "E",
                                                  lambda x: float(x),
                                                  lambda y: 0)
        expected = [a, c, d, e]
        self.assertEqual(expected, path)

    def test_astar_manhattan_heuristic(self):
        g = retworkx.PyGraph()
        a = g.add_node((0., 0.))
        b = g.add_node((2., 0.))
        c = g.add_node((1., 1.))
        d = g.add_node((0., 2.))
        e = g.add_node((3., 3.))
        f = g.add_node((4., 2.))
        no_path = g.add_node((5., 5.))  # no path to node
        g.add_edge(a, b, 2.)
        g.add_edge(a, d, 4.)
        g.add_edge(b, c, 1.)
        g.add_edge(b, f, 7.)
        g.add_edge(c, e, 5.)
        g.add_edge(e, f, 1.)
        g.add_edge(d, e, 1.)

        def heuristic_func(f):
            x1, x2 = f
            return abs(x2 - x1)

        def finish_func(node, x):
            return x == g.get_node_data(node)

        expected = [
            [0],
            [0, 1],
            [0, 1, 2],
            [0, 3],
            [0, 3, 4],
            [0, 3, 4, 5],
        ]

        for index, end in enumerate([a, b, c, d, e, f]):
            path = retworkx.graph_astar_shortest_path(
                g, a, lambda finish: finish_func(end, finish),
                lambda x: float(x), heuristic_func)
            self.assertEqual(expected[index], path)

        with self.assertRaises(retworkx.NoPathFound):
            retworkx.graph_astar_shortest_path(
                g, a, lambda finish: finish_func(no_path, finish),
                lambda x: float(x), heuristic_func)

    def test_astar_graph_with_digraph_input(self):
        g = retworkx.PyDAG()
        g.add_node(0)
        with self.assertRaises(TypeError):
            retworkx.graph_astar_shortest_path(
                g, 0, lambda x: x, lambda y: 1, lambda z: 0)
