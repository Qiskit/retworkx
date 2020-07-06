.. _retworkx:

======================
Retworkx API Reference
======================

Graph Classes
-------------


.. autosummary::
   :toctree: stubs

    retworkx.PyGraph
    retworkx.PyDiGraph
    retworkx.PyDAG

Algorithm Functions
-------------------

.. autosummary::
   :toctree: stubs

   retworkx.bfs_successors
   retworkx.dag_longest_path
   retworkx.dag_longest_path_length
   retworkx.number_weakly_connected_components
   retworkx.is_directed_acyclic_graph
   retworkx.is_isomorphic
   retworkx.is_isomorphic_node_match
   retworkx.topological_sort
   retworkx.descendants
   retworkx.ancestors
   retworkx.lexicographical_topological_sort
   retworkx.floyd_warshall
   retworkx.layers
   retworkx.digraph_adjacency_matrix
   retworkx.graph_adjacency_matrix
   retworkx.graph_all_simple_paths
   retworkx.digraph_all_simple_paths
   retworkx.graph_astar_shortest_path
   retworkx.digraph_astar_shortest_path
   retworkx.graph_greedy_color

Exceptions
----------

.. autosummary::
   :toctree: stubs

   retworkx.InvalidNode
   retworkx.DAGWouldCycle
   retworkx.NoEdgeBetweenNodes
   retworkx.DAGHasCycle
   retworkx.NoSuitableNeighbors
   retworkx.NoPathFound
