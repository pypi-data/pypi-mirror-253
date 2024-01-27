# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from envdesign_model.graph_algorithms.build_clique import build_clique
from graphing.graph import Graph
from tests.utils import check_exception


def test_build_clique():
    # test case: (graph edges, clique size, initial clique, exclude vertices,
    # boolean for expecting valid clique to be returned, boolean for expecting
    # Exception)
    MOCK_GRAPH_EDGES = [
        {(0, 2), (2, 0), (0, 4), (4, 0), (2, 4), (4, 2), (1, 3), (3, 1),
         (1, 5), (5, 1), (3, 5), (5, 3)},
        {(0, 2), (2, 0), (0, 4), (4, 0), (1, 3), (3, 1), (1, 5), (5, 1),
         (3, 5), (5, 3)}
    ]
    TEST_CASES = [
        (MOCK_GRAPH_EDGES[0], 3, None, set(), False, True
         # expect Exception since initial clique is None
         ),
        (MOCK_GRAPH_EDGES[0], 3, set(), set(), False, True
         # expect Exception since initial clique is empty
         ),
        (MOCK_GRAPH_EDGES[0], 3, {0}, {0, 2}, False, True
         # expect Exception since initial clique has a vertex in the 
         # exclude vertices set
         ),
        (MOCK_GRAPH_EDGES[0], 3, {0, 2}, {0}, False, True
         # expect Exception since initial clique has a vertex in the
         # exclude vertices set
         ),
        (MOCK_GRAPH_EDGES[0], 3, {2}, set(), True, False),
        (MOCK_GRAPH_EDGES[0], 3, {3}, set(), True, False),
        (MOCK_GRAPH_EDGES[0], 3, {0, 2}, set(), True, False),
        (MOCK_GRAPH_EDGES[0], 3, {1, 3}, set(), True, False),
        (MOCK_GRAPH_EDGES[0], 3, {0}, set(), True, False),
        (MOCK_GRAPH_EDGES[0], 3, {0, 4}, set(), True, False),
        (MOCK_GRAPH_EDGES[0], 3, {0, 2}, {4}, False, False),
        (MOCK_GRAPH_EDGES[0], 3, {0}, {2}, False, False),
        (MOCK_GRAPH_EDGES[0], 3, {0, 4}, {3}, True, False),
        (MOCK_GRAPH_EDGES[1], 3, {0}, set(), False, False),
        (MOCK_GRAPH_EDGES[1], 3, {0, 4}, set(), False, False),
        (MOCK_GRAPH_EDGES[1], 3, {0, 2}, set(), False, False)
    ]
    for test_case in TEST_CASES:
        edges, clique_size, init_clique, exclude_vertices,\
            expecting_complete_clique, exception = test_case
        graph = Graph(edges)
        try:
            complete_clique = build_clique(
                graph, clique_size, init_clique, exclude_vertices)
        except Exception:
            check_exception(True, exception, test_case)
        else:
            check_exception(False, exception, test_case)
            if expecting_complete_clique:
                assert complete_clique is not None, 'Expected clique to be '\
                    + f'returned, instead got None, for test case: {test_case}'
                complete_clique = tuple(complete_clique)
                if init_clique is not None:
                    uncovered_existing_verts = init_clique.difference(
                        set(complete_clique))
                    assert len(uncovered_existing_verts) == 0,\
                        + f'Vertices ({uncovered_existing_verts}) from '\
                        + f'initial clique ({init_clique}) are not '\
                        + f'present in resulting clique ({complete_clique})'
                for i in range(len(complete_clique) - 1):
                    for j in range(i + 1, len(complete_clique)):
                        v1 = complete_clique[i]
                        v2 = complete_clique[j]
                        assert (v1, v2) in graph.edges and (v1, v2) in\
                            graph.edges, f'Invalid clique {complete_clique} '\
                            + f'for test case: {test_case}. Edges between '\
                            + f'vertices {v1} and {v2} not present in the '\
                            + f'graph.'
            else:
                assert complete_clique is None, 'Expected no clique to be '\
                    + f'returned, instead got new clique {complete_clique}, '\
                    + f'for test case: {test_case}'
