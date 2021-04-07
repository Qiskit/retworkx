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


class TestSpringLayout(unittest.TestCase):
    def test_empty_graph(self):
        graph = retworkx.PyGraph()
        res = retworkx.spring_layout(graph)
        self.assertEqual({}, res)

    def test_simple_graph(self):
        graph = retworkx.PyGraph()
        node_a = graph.add_node(1)
        node_b = graph.add_node(2)
        graph.add_edge(node_a, node_b, 1)
        node_c = graph.add_node(3)
        graph.add_edge(node_a, node_c, 1)

        res = retworkx.spring_layout(graph)
        self.assertEqual(len(res), 3)
        self.assertEqual(len(res[0]), 2)
        self.assertIsInstance(res[0][0], float)
