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


class TestFloydWarshall(unittest.TestCase):

    def test_floyd_warshall(self):
        """Test the algorithm on a 5q x 4 depth circuit."""
        dag = retworkx.PyDAG()
        # inputs
        qr_0 = dag.add_node('qr[0]')
        qr_1 = dag.add_node('qr[1]')
        qr_2 = dag.add_node('qr[2]')
        cr_0 = dag.add_node('cr[0]')
        cr_1 = dag.add_node('cr[1]')
        # wires
        cx_1 = dag.add_node('cx_1')
        dag.add_edge(qr_0, cx_1, 'qr[0]')
        dag.add_edge(qr_1, cx_1, 'qr[1]')
        h_1 = dag.add_node('h_1')
        dag.add_edge(cx_1, h_1, 'qr[0]')
        cx_2 = dag.add_node('cx_2')
        dag.add_edge(cx_1, cx_2, 'qr[1]')
        dag.add_edge(qr_2, cx_2, 'qr[2]')
        cx_3 = dag.add_node('cx_3')
        dag.add_edge(h_1, cx_3, 'qr[0]')
        dag.add_edge(cx_2, cx_3, 'qr[2]')
        h_2 = dag.add_node('h_2')
        dag.add_edge(cx_3, h_2, 'qr[2]')
        # # outputs
        qr_0_out = dag.add_node('qr[0]_out')
        dag.add_edge(cx_3, qr_0_out, 'qr[0]')
        qr_1_out = dag.add_node('qr[1]_out')
        dag.add_edge(cx_2, qr_1_out, 'qr[1]')
        qr_2_out = dag.add_node('qr[2]_out')
        dag.add_edge(h_2, qr_2_out, 'qr[2]')
        cr_0_out = dag.add_node('cr[0]_out')
        dag.add_edge(cr_0, cr_0_out, 'qr[2]')
        cr_1_out = dag.add_node('cr[1]_out')
        dag.add_edge(cr_1, cr_1_out, 'cr[1]')

        result = retworkx.floyd_warshall(dag)
        expected = {
            0: {0: 0, 5: 1, 6: 2, 7: 2, 8: 3, 9: 4, 10: 4, 11: 3, 12: 5},
            1: {1: 0, 5: 1, 6: 2, 7: 2, 8: 3, 9: 4, 10: 4, 11: 3, 12: 5},
            2: {2: 0, 7: 1, 8: 2, 9: 3, 10: 3, 11: 2, 12: 4},
            3: {3: 0, 13: 1},
            4: {4: 0, 14: 1},
            5: {5: 0, 6: 1, 7: 1, 8: 2, 9: 3, 10: 3, 11: 2, 12: 4},
            6: {6: 0, 8: 1, 9: 2, 10: 2, 12: 3},
            7: {7: 0, 8: 1, 9: 2, 10: 2, 11: 1, 12: 3},
            8: {8: 0, 9: 1, 10: 1, 12: 2},
            9: {9: 0, 12: 1},
            10: {10: 0},
            11: {11: 0},
            12: {12: 0},
            13: {13: 0},
            14: {14: 0},
        }
        self.assertDictEqual(result, expected)
