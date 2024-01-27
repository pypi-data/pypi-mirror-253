# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from envdesign_model.optimization.algorithms.expand_clique_cover_sa import\
    ExpandCliqueCoverSA
from envdesign_model.optimization.objective_functions.mean_squared_error\
    import DimensionMSE, RelationshipMSE, CombinationMSE
from graphing.graph import Graph
from tests.utils import check_exception
from functools import reduce


MOCK_CLIQUE_COVERS = [
    [(0, 2, 4), (1, 3, 5)],
    [(0, 2, 4), (0, 2, 5), (1, 3, 5)],
    [(0, 3, 5), (1, 3, 6), (2, 4, 7)],
    [(1, 3, 5), (2, 4, 7), (0, 3, 6)]
]
MOCK_GRAPHS = [
    Graph({(0, 2), (2, 0), (0, 4), (4, 0), (2, 4), (4, 2), (1, 3), (3, 1),
           (3, 5), (5, 3), (1, 5), (5, 1)}),
    Graph({(0, 2), (2, 0), (0, 4), (4, 0), (2, 4), (4, 2), (1, 3), (3, 1),
           (3, 5), (5, 3), (1, 5), (5, 1), (0, 5), (5, 0), (2, 5), (5, 2)}),
    Graph({(0, 3), (3, 0), (0, 5), (5, 0), (3, 5), (5, 3), (1, 3), (3, 1),
           (3, 6), (6, 3), (1, 6), (6, 1), (2, 4), (4, 2), (4, 7), (7, 4),
           (2, 7), (7, 2)}),
    Graph({(1, 3), (3, 1), (1, 5), (5, 1), (3, 5), (5, 3), (0, 3), (3, 0),
           (3, 6), (6, 3), (0, 6), (6, 0), (2, 4), (4, 2), (4, 7), (7, 4),
           (2, 7), (7, 2)}),
    Graph({(0, 2), (2, 0), (0, 4), (4, 0), (2, 4), (4, 2), (1, 3),
           (3, 1), (3, 5), (5, 3), (1, 5), (5, 1), (1, 4), (4, 1),
           (3, 4), (4, 3)}),
    Graph({(0, 2), (2, 0), (0, 4), (4, 0), (2, 4), (4, 2), (1, 3),
           (3, 1), (3, 5), (5, 3), (1, 5), (5, 1), (0, 5), (5, 0),
           (2, 5), (5, 2)}),
    Graph({(0, 3), (3, 0), (0, 5), (5, 0), (3, 5), (5, 3), (1, 3),
           (3, 1), (3, 6), (6, 3), (1, 6), (6, 1), (2, 4), (4, 2),
           (4, 7), (7, 4), (2, 7), (7, 2), (1, 4), (4, 1), (4, 6),
           (6, 4)})
]
MOCK_OBJ_FUNCS = [
    {
        0: DimensionMSE({0: 1, 1: 1}, 0.2, True),
        1: DimensionMSE({2: 1, 3: 1}, 0.4, True),
        2: DimensionMSE({4: 1, 5: 1}, 0.4, True),
    },
    {
        (0, 1): RelationshipMSE({(0, 2): 1, (1, 3): 1}, 3, True),
        (0, 2): RelationshipMSE({(0, 4): 1, (0, 5): 1, (1, 5): 1}, 3, True),
        (1, 2): RelationshipMSE({(2, 4): 1, (2, 5): 1, (3, 5): 1}, 4, True)
    },
    {
        (0, 1): RelationshipMSE({
            (0, 3): 1, (1, 3): 1, (1, 4): 1, (2, 4): 1
        }, 1/3),
        (1, 2): RelationshipMSE({
            (3, 5): 1, (3, 6): 1, (4, 7): 1
        }, 1/3),
        (0, 2): RelationshipMSE({
            (0, 5): 1, (0, 6): 1, (1, 5): 1, (1, 6): 1, (1, 7): 1,
            (2, 7): 1
        }, 1/3),
    },
    CombinationMSE({(0, 3, 5): 1, (1, 3, 6): 1, (2, 4, 7): 1}),
    {
        0: DimensionMSE({0: 1, 1: 1}, 1, True),
        1: DimensionMSE({2: 1, 3: 1}, 1, True),
        2: DimensionMSE({4: 1, 5: 1}, 1, True)
    },
    {
        0: DimensionMSE({0: 1, 1: 1, 2: 1}, 1, True),
        1: DimensionMSE({3: 1, 4: 1}, 1, True),
        2: DimensionMSE({5: 1, 6: 1, 7: 1}, 1, True)
    }
]
TEST_CASES = [
    # test case: tuple(graph, clique cover, number of groups, objective function,
    # solution, expected MSE, expected cost results)
    (MOCK_GRAPHS[0], MOCK_CLIQUE_COVERS[0], 4, MOCK_OBJ_FUNCS[0],
     [(0, 2, 4), (1, 3, 5), (0, 2, 4), (1, 3, 5)], 0, {0: 0, 1: 0, 2: 0}),
    (MOCK_GRAPHS[0], MOCK_CLIQUE_COVERS[0], 3, MOCK_OBJ_FUNCS[0],
     [(0, 2, 4), (1, 3, 5), (0, 2, 4)], 0.0277777778,
     {0: 0.0055555556, 1: 0.0111111111, 2: 0.0111111111}),
    (MOCK_GRAPHS[1], MOCK_CLIQUE_COVERS[1], 6, MOCK_OBJ_FUNCS[1],
     [(0, 2, 4), (1, 3, 5), (0, 2, 5), (0, 2, 4), (1, 3, 5), (0, 2, 5)],
     0.0833333333, {(0, 1): 0.0833333333, (0, 2): 0, (1, 2): 0}),
    (MOCK_GRAPHS[0], MOCK_CLIQUE_COVERS[0], 6, MOCK_OBJ_FUNCS[1],
     [(0, 2, 4), (1, 3, 5), (0, 2, 4), (1, 3, 5), (0, 2, 4), (1, 3, 5)],
     0.3888888888, {(0, 1): 0, (0, 2): 0.1666666667, (1, 2): 0.2222222222}),
    (MOCK_GRAPHS[3], MOCK_CLIQUE_COVERS[3], 6, MOCK_OBJ_FUNCS[2],
     [(1, 3, 5), (2, 4, 7), (0, 3, 6), (0, 3, 6), (2, 4, 7), (1, 3, 5)],
     0.016203703703703703,
     {(0, 1): 0.006944444444444444, (1, 2): 0.0, (0, 2): 0.009259259259259259}
     ),
    (MOCK_GRAPHS[2], MOCK_CLIQUE_COVERS[2], 6, MOCK_OBJ_FUNCS[3],
     [(0, 3, 5), (1, 3, 6), (2, 4, 7), (0, 3, 5), (1, 3, 6), (2, 4, 7)],
     0, 0),
    (MOCK_GRAPHS[2], MOCK_CLIQUE_COVERS[2], 6, MOCK_OBJ_FUNCS[3],
     [(0, 3, 5), (1, 3, 6), (2, 4, 7), (0, 3, 5), (1, 3, 6), (2, 4, 6)],
     0.0138888889, 0.0138888889)
]


def _check_solution(sol, expand_cc_sa, preserve_cc=True):
    assert sol is not None, 'Solution cannot be None'
    assert len(sol) == expand_cc_sa.num_groups,\
        'Incorrect length of solution. Expected: '\
        + f'{expand_cc_sa.num_groups}, Actual: '\
        + f'{len(sol)}'
    covered_vertices = set(reduce(lambda c1, c2: set(c1).union(set(c2)),
                                  sol, set()))
    assert expand_cc_sa.vertices == covered_vertices, 'Incorrect '\
        + 'coverage of vertices in solution. Expected: '\
        + f'{expand_cc_sa.vertices}. Actual: {covered_vertices}'
    if preserve_cc:
        assert set(expand_cc_sa.clique_cover) == set(sol[
            :len(expand_cc_sa.clique_cover)]),\
            f'Clique cover not preserved in solution: {sol}'


def test_constructor_get_candidate():
    for test_case in TEST_CASES:
        graph, clique_cover, num_groups, objective_function,\
            _, _, _ = test_case
        expand_cc_sa = ExpandCliqueCoverSA(
            graph, clique_cover, num_groups, objective_function)
        _check_solution(expand_cc_sa.candidate, expand_cc_sa, preserve_cc=True)

        # min clique cover length > number of groups (set to 0)
        try:
            expand_cc_sa = ExpandCliqueCoverSA(
                graph, clique_cover, 0, objective_function)
            check_exception(False, True, test_case)
        except Exception:
            check_exception(True, True, test_case)


def test_next_candidate():
    for test_case in TEST_CASES:
        graph, clique_cover, num_groups, objective_function,\
            sol, _, _ = test_case
        for preserve_cc in [True, False]:
            for get_new_clique_approach in [0, 1, 2]:
                expand_cc_sa = ExpandCliqueCoverSA(
                    graph, clique_cover, num_groups, objective_function,
                    preserve_cc, get_new_clique_approach)
                next_sol = expand_cc_sa.next_candidate(expand_cc_sa.candidate)
                _check_solution(next_sol, expand_cc_sa, preserve_cc)
                next_sol = expand_cc_sa.next_candidate(sol)
                _check_solution(next_sol, expand_cc_sa, preserve_cc)


def test_cost():
    for test_case in TEST_CASES:
        graph, clique_cover, num_groups, objective_function, sol,\
            expected_mse, expected_results = test_case
        expand_cc_sa = ExpandCliqueCoverSA(
            graph, clique_cover, num_groups, objective_function)
        mse, _, results = expand_cc_sa.cost(sol)
        threshold = 1e-10
        assert abs(mse - expected_mse) < threshold, 'Incorrect computed MSE '\
            + f'value. Expected: value within {threshold} of {expected_mse}. '\
            + f'Actual: {mse}'
        if type(objective_function) == CombinationMSE:
            assert abs(results - expected_results) <= threshold, 'Incorrect '\
                + f'computed MSE value. Expected: value within {threshold}'\
                + f' of {expected_mse}. Actual: {mse}'
        elif type(objective_function) == dict:
            for cost_key in results.keys():
                assert abs(results[cost_key] - expected_results[cost_key]) \
                    <= threshold, 'Incorrect computed MSE value for '\
                    + f'dimension(s) {cost_key}. Expected: value within '\
                    + f'{threshold} of {expected_results[cost_key]}. '\
                    + f'Actual: {results[cost_key]}'


def test_get_new_clique():
    # test case: (graph, clique cover, objective fucntions, clique, integer 
    # representing get new clique approach, boolean for expecting clique to
    # be returned)
    CUSTOM_TEST_CASES = [
        (MOCK_GRAPHS[4], MOCK_CLIQUE_COVERS[0], MOCK_OBJ_FUNCS[4], (0, 2, 4),
         0, True),
        (MOCK_GRAPHS[4], MOCK_CLIQUE_COVERS[0], MOCK_OBJ_FUNCS[4], (0, 2, 4),
         1, False),
        (MOCK_GRAPHS[4], MOCK_CLIQUE_COVERS[0], MOCK_OBJ_FUNCS[4], (0, 2, 4),
         2, True),
        (MOCK_GRAPHS[4], MOCK_CLIQUE_COVERS[0], MOCK_OBJ_FUNCS[4], (2, 4, 0),
         0, True),
        (MOCK_GRAPHS[4], MOCK_CLIQUE_COVERS[0], MOCK_OBJ_FUNCS[4], (2, 4, 0),
         1, False),
        (MOCK_GRAPHS[4], MOCK_CLIQUE_COVERS[0], MOCK_OBJ_FUNCS[4], (2, 4, 0),
         2, True),
        (MOCK_GRAPHS[4], MOCK_CLIQUE_COVERS[0], MOCK_OBJ_FUNCS[4], (1, 3, 5),
         0, True),
        (MOCK_GRAPHS[4], MOCK_CLIQUE_COVERS[0], MOCK_OBJ_FUNCS[4], (1, 3, 5),
         1, True),
        (MOCK_GRAPHS[4], MOCK_CLIQUE_COVERS[0], MOCK_OBJ_FUNCS[4], (1, 3, 5),
         2, True),
        (MOCK_GRAPHS[4], MOCK_CLIQUE_COVERS[0], MOCK_OBJ_FUNCS[4], (4, 3, 1),
         0, True),
        (MOCK_GRAPHS[4], MOCK_CLIQUE_COVERS[0], MOCK_OBJ_FUNCS[4], (4, 3, 1),
         1, True),
        (MOCK_GRAPHS[4], MOCK_CLIQUE_COVERS[0], MOCK_OBJ_FUNCS[4], (4, 3, 1),
         2, True),
    ]
    for test_case in CUSTOM_TEST_CASES:
        graph, clique_cover, obj_funcs, clique, get_new_clique_approach, \
           clique_returned = test_case
        for preserve_cc in [True, False]:
            expand_cc_sa = ExpandCliqueCoverSA(
                graph, clique_cover, 12, obj_funcs, preserve_cc,
                get_new_clique_approach)
            new_clique = expand_cc_sa._get_new_clique(clique)
            if clique_returned:
                assert new_clique is not None, 'Expected clique to be '\
                    + f'returned, instead got None, for graph edges '\
                    + f'{graph.edges}, clique {clique}, and get new clique '\
                    + f'approach {get_new_clique_approach}'
                for i in range(len(new_clique) - 1):
                    for j in range(i + 1, len(new_clique)):
                        v1 = new_clique[i]
                        v2 = new_clique[j]
                        assert (v1, v2) in graph.edges and (v1, v2) in\
                            graph.edges, f'Invalid clique {new_clique}. '\
                            + f'Edges between vertices {v1} and {v2} not '\
                            + f'present in the graph'
            else:
                assert new_clique is None, 'Expected no clique to be '\
                    + f'returned, instead got new clique {new_clique}, for '\
                    + f'graph edges {graph.edges}, clique {clique}, and get '\
                    + f'new clique approach {get_new_clique_approach}'
