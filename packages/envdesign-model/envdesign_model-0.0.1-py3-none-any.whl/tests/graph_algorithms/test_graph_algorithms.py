# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import pandas as pd
from functools import reduce
from envdesign_model.graph_algorithms.graph_algorithms import GraphAlgorithms,\
    UncoverableDimensionValuesWarning
from tests.mock_data import MOCK_DIMENSION_DICTS, MOCK_RELATIONSHIPS_DFS,\
    MOCK_SCOPE_DFS, MOCK_OBJ_FUNC_DICTS
from tests.utils import check_exception, check_warning
from graphing.graph import Graph
import warnings


def test_create_dim_mappings():
    # test case: tuple(dimension dicts, relationships DataFrame, expected
    # dimension value to int mapping, expected int to dimension value mapping,
    # expected dimension name to values mapping, expected int to dimension name
    # mapping, expected dimension name to ints mapping)
    case2_relationships_df = MOCK_RELATIONSHIPS_DFS[1].copy()
    case2_relationships_df = case2_relationships_df[
        (case2_relationships_df['Dimension1'] == 'Hardware')
        | (case2_relationships_df['Dimension2'] == 'Hardware')]
    PASS_CASES = [
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0],
         {'HW1': 0, 'HW2': 1, 'VM1': 2, 'VM2': 3, 'WL1': 4, 'WL2': 5},
         {0: 'HW1', 1: 'HW2', 2: 'VM1', 3: 'VM2', 4: 'WL1', 5: 'WL2'},
         {'Hardware': {'HW1', 'HW2'}, 'Virtual_Machine': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}},
         {0: 'Hardware', 1: 'Hardware', 2: 'Virtual_Machine',
          3: 'Virtual_Machine', 4: 'Workload', 5: 'Workload'},
         {'Hardware': {0, 1}, 'Virtual_Machine': {2, 3}, 'Workload': {4, 5}}
         ),
        (MOCK_DIMENSION_DICTS[1:3], case2_relationships_df,
         {'VM1': 0, 'VM2': 1, 'WL1': 2, 'WL2': 3},
         {0: 'VM1', 1: 'VM2', 2: 'WL1', 3: 'WL2'},
         {'Virtual_Machine': {'VM1', 'VM2'}, 'Workload': {'WL1', 'WL2'}},
         {0: 'Virtual_Machine', 1: 'Virtual_Machine', 2: 'Workload',
          3: 'Workload'},
         {'Virtual_Machine': {0, 1}, 'Workload': {2, 3}}
         )
    ]
    fail_case1_hw_dim_df = pd.concat([
        MOCK_DIMENSION_DICTS[0]['df'].copy(),
        pd.DataFrame([{'HW': '<ANY>', 'Score': 1}])], ignore_index=True)
    fail_case1_hw_dim_dict = dict()
    fail_case1_hw_dim_dict['name'] = MOCK_DIMENSION_DICTS[0]['name']
    fail_case1_hw_dim_dict['value'] = MOCK_DIMENSION_DICTS[0]['value']
    fail_case1_hw_dim_dict['df'] = fail_case1_hw_dim_df
    fail_case2_vm_dim_df = pd.concat([
        MOCK_DIMENSION_DICTS[1]['df'].copy(),
        pd.DataFrame([{'VM': '<ANY>', 'Score': 1}])], ignore_index=True)
    fail_case2_vm_dim_dict = dict()
    fail_case2_vm_dim_dict['name'] = MOCK_DIMENSION_DICTS[1]['name']
    fail_case2_vm_dim_dict['value'] = MOCK_DIMENSION_DICTS[1]['value']
    fail_case2_vm_dim_dict['df'] = fail_case2_vm_dim_df
    FAIL_CASES = [
        ([fail_case1_hw_dim_dict] + MOCK_DIMENSION_DICTS[1:3],
         MOCK_RELATIONSHIPS_DFS[0],
         {'HW1': 0, 'HW2': 1, '<ANY>': 2, 'VM1': 3, 'VM2': 4, 'WL1': 5,
          'WL2': 6},
         {0: 'HW1', 1: 'HW2', 2: '<ANY>', 3: 'VM1', 4: 'VM2', 5: 'WL1',
          6: 'WL2'},
         {'Hardware': {'HW1', 'HW2', '<ANY>'},
          'Virtual_Machine': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}},
         {0: 'Hardware', 1: 'Hardware', 2: 'Virtual_Machine',
          3: 'Virtual_Machine', 4: 'Workload', 5: 'Workload'},
         {'Hardware': {0, 1}, 'Virtual_Machine': {2, 3}, 'Workload': {4, 5}}
         # expect Exception because <ANY> cannot be used as a dimension value
         ),
        ([fail_case2_vm_dim_dict] + MOCK_DIMENSION_DICTS[2:3],
         case2_relationships_df,
         {'VM1': 0, 'VM2': 1, '<ANY>': 2, 'WL1': 3, 'WL2': 4},
         {0: 'VM1', 1: 'VM2', 2: '<ANY>', 3: 'WL1', 4: 'WL2'},
         {'Virtual_Machine': {'VM1', 'VM2', '<ANY>'},
          'Workload': {'WL1', 'WL2'}},
         {0: 'Virtual_Machine', 1: 'Virtual_Machine', 2: 'Workload',
          3: 'Workload'},
         {'Virtual_Machine': {0, 1}, 'Workload': {2, 3}}
         # expect Exception because <ANY> cannot be used as a dimension value
         )
    ]
    for cases, exception in [(PASS_CASES, False), (FAIL_CASES, True)]:
        for test_case in cases:
            (dim_dicts, relationships_df, dim_value_to_int, int_to_dim_value,
             dim_name_to_dim_values, int_to_dim_name, dim_name_to_ints)\
                = test_case
            try:
                graph_algorithms = GraphAlgorithms(
                    dim_dicts, relationships_df, 10, MOCK_OBJ_FUNC_DICTS[0])
                graph_algorithms._create_dim_mappings()
                if graph_algorithms.dim_value_to_int != dim_value_to_int:
                    raise Exception(
                        'Incorrect dimension value to integer mappings. '
                        + f'Expected:  {dim_value_to_int}, Actual: '
                        + f'{graph_algorithms.dim_value_to_int}')
                if graph_algorithms.int_to_dim_value != int_to_dim_value:
                    raise Exception(
                        'Incorrect integer to dimension value mappings. '
                        + f'Expected: {int_to_dim_value}, Actual: '
                        + f'{graph_algorithms.int_to_dim_value}')
                if graph_algorithms.dim_name_to_dim_values !=\
                        dim_name_to_dim_values:
                    raise Exception(
                        'Incorrect dimension name to dimension values '
                        + f'mappings. Expected: {dim_name_to_dim_values}, '
                        + f'Actual: {graph_algorithms.dim_name_to_dim_values}')
                if graph_algorithms.int_to_dim_name != int_to_dim_name:
                    raise Exception(
                        'Incorrect integer to dimension name '
                        + f'mappings. Expected: {int_to_dim_name}, '
                        + f'Actual: {graph_algorithms.int_to_dim_name}')
                if graph_algorithms.dim_name_to_ints != dim_name_to_ints:
                    raise Exception(
                        'Incorrect dimension name to integers'
                        + f'mappings. Expected: {dim_name_to_ints}, '
                        + f'Actual: {graph_algorithms.dim_name_to_ints}')
            except Exception:
                check_exception(True, exception, test_case)
            else:
                check_exception(False, exception, test_case)


def test_create_graph():
    # test case: tuple(dimension dicts, relationships DataFrame, dimension
    # value to integer mapping, integer to dimension value mapping, dimension
    # name to dimension values mapping, true graph edge set)
    TEST_CASES = [
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0],
         {'HW1': 0, 'HW2': 1, 'VM1': 2, 'VM2': 3, 'WL1': 4, 'WL2': 5},
         {0: 'HW1', 1: 'HW2', 2: 'VM1', 3: 'VM2', 4: 'WL1', 5: 'WL2'},
         {'Hardware': {'HW1', 'HW2'}, 'Virtual_Machine': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}},
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1)}
         ),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[1],
         {'HW1': 0, 'HW2': 1, 'VM1': 2, 'VM2': 3, 'WL1': 4, 'WL2': 5},
         {0: 'HW1', 1: 'HW2', 2: 'VM1', 3: 'VM2', 4: 'WL1', 5: 'WL2'},
         {'Hardware': {'HW1', 'HW2'}, 'Virtual_Machine': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}},
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1), (0, 5), (5, 0), (2, 5), (5, 2)}
         ),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[2],
         {'HW1': 0, 'HW2': 1, 'VM1': 2, 'VM2': 3, 'WL1': 4, 'WL2': 5},
         {0: 'HW1', 1: 'HW2', 2: 'VM1', 3: 'VM2', 4: 'WL1', 5: 'WL2'},
         {'Hardware': {'HW1', 'HW2'}, 'Virtual_Machine': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}},
         {(0, 2), (2, 0), (0, 3), (3, 0), (1, 2), (2, 1), (1, 3), (3, 1),
          (0, 4), (4, 0), (2, 4), (4, 2), (1, 5), (5, 1), (3, 5), (5, 3)}
         )
    ]
    for test_case in TEST_CASES:
        (dim_dicts, relationships_df, dim_value_to_int, int_to_dim_value,
            dim_name_to_dim_values, edge_set) = test_case
        graph_algorithms = GraphAlgorithms(
            dim_dicts, relationships_df, 10, MOCK_OBJ_FUNC_DICTS[0])
        # mock creation of dimension mappings
        graph_algorithms.dim_name_to_dim_values =\
            dim_name_to_dim_values
        graph_algorithms.dim_value_to_int = dim_value_to_int
        graph_algorithms.int_to_dim_value = int_to_dim_value
        # create graph
        graph_algorithms._create_graph()
        graph_edges = graph_algorithms.graph.edges
        assert graph_edges == edge_set, 'Invalid graph edge set. '\
            + f'Expected: {edge_set}, Actual: {graph_edges}'
        for edge in edge_set:
            assert edge[1] in set(
                    graph_algorithms.graph.adj[edge[0]].keys()),\
                f'Vertex {edge[1]} not in adjacency map for '\
                + f'vertex {edge[0]}'    


def test_clique_cover_vertices():
    # test_case: tuple(scope DataFrame, dimension dictionaries, relationships
    # DataFrame, graph edge set, dimension value to int mapping
    # int to dimension value mapping, int to dimension name mapping,
    # dimension name to dimension values mapping, existing clique cover,
    # vertices to cover, list of possible expected clique covers)
    TEST_CASES = [
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1)},
         {'HW1': 0, 'HW2': 1, 'VM1': 2, 'VM2': 3, 'WL1': 4, 'WL2': 5},
         {0: 'HW1', 1: 'HW2', 2: 'VM1', 3: 'VM2', 4: 'WL1', 5: 'WL2'},
         {0: 'Hardware', 1: 'Vm_Type', 2: 'Workload'},
         {'Hardware': {'HW1', 'HW2'}, 'Vm_Type': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}}, [{1, 3, 5}], {0},
         [[{1, 3, 5}, {0, 2, 4}]]),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1)},
         {'HW1': 0, 'HW2': 1, 'VM1': 2, 'VM2': 3, 'WL1': 4, 'WL2': 5},
         {0: 'HW1', 1: 'HW2', 2: 'VM1', 3: 'VM2', 4: 'WL1', 5: 'WL2'},
         {0: 'Hardware', 1: 'Vm_Type', 2: 'Workload'},
         {'Hardware': {'HW1', 'HW2'}, 'Vm_Type': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}}, [{0, 2, 4}, {1, 3, 5}], set(),
         [[{0, 2, 4}, {1, 3, 5}]]),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1)},
         {'HW1': 0, 'HW2': 1, 'VM1': 2, 'VM2': 3, 'WL1': 4, 'WL2': 5},
         {0: 'HW1', 1: 'HW2', 2: 'VM1', 3: 'VM2', 4: 'WL1', 5: 'WL2'},
         {0: 'Hardware', 1: 'Vm_Type', 2: 'Workload'},
         {'Hardware': {'HW1', 'HW2'}, 'Vm_Type': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}}, [{0, 2, 4}], {1, 3, 5},
         [[{0, 2, 4}, {1, 3, 5}]]),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1)},
         {'HW1': 0, 'HW2': 1, 'VM1': 2, 'VM2': 3, 'WL1': 4, 'WL2': 5},
         {0: 'HW1', 1: 'HW2', 2: 'VM1', 3: 'VM2', 4: 'WL1', 5: 'WL2'},
         {0: 'Hardware', 1: 'Vm_Type', 2: 'Workload'},
         {'Hardware': {'HW1', 'HW2'}, 'Vm_Type': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}}, [{0, 2, 4}], {3},
         [[{0, 2, 4}, {1, 3, 5}]]),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1)},
         {'HW1': 0, 'HW2': 1, 'VM1': 2, 'VM2': 3, 'WL1': 4, 'WL2': 5},
         {0: 'HW1', 1: 'HW2', 2: 'VM1', 3: 'VM2', 4: 'WL1', 5: 'WL2'},
         {0: 'Hardware', 1: 'Vm_Type', 2: 'Workload'},
         {'Hardware': {'HW1', 'HW2'}, 'Vm_Type': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}}, [{1, 3, 5}], {2, 4},
         [[{1, 3, 5}, {0, 2, 4}]]),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1)},
         {'HW1': 0, 'HW2': 1, 'VM1': 2, 'VM2': 3, 'WL1': 4, 'WL2': 5},
         {0: 'HW1', 1: 'HW2', 2: 'VM1', 3: 'VM2', 4: 'WL1', 5: 'WL2'},
         {0: 'Hardware', 1: 'Vm_Type', 2: 'Workload'},
         {'Hardware': {'HW1', 'HW2'}, 'Vm_Type': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}}, [], {1, 3, 5},
         [[{1, 3, 5}]]),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1)},
         {'HW1': 0, 'HW2': 1, 'VM1': 2, 'VM2': 3, 'WL1': 4, 'WL2': 5},
         {0: 'HW1', 1: 'HW2', 2: 'VM1', 3: 'VM2', 4: 'WL1', 5: 'WL2'},
         {0: 'Hardware', 1: 'Vm_Type', 2: 'Workload'},
         {'Hardware': {'HW1', 'HW2'}, 'Vm_Type': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}}, [], {1, 3, 5, 0, 2, 4},
         [[{1, 3, 5}, {0, 2, 4}], [{0, 2, 4}, {1, 3, 5}]])
    ]
    for test_case in TEST_CASES:
        dim_dicts, rel_df, edge_set, dim_val_to_int, int_to_dim_val,\
            int_to_dim_name, dim_name_to_dim_vals, existing_cc,\
            cover_vertices, expected_ccs = test_case
        graph_algorithms = GraphAlgorithms(
            dim_dicts, rel_df, 10, MOCK_OBJ_FUNC_DICTS[0])
        graph_algorithms.dim_value_to_int = dim_val_to_int
        graph_algorithms.int_to_dim_value = int_to_dim_val
        graph_algorithms.int_to_dim_name = int_to_dim_name
        graph_algorithms.dim_name_to_dim_values = dim_name_to_dim_vals
        graph_algorithms.clique_cover = existing_cc
        graph_algorithms.clique_covered_vertices = set(
            reduce(lambda c1, c2: set(c1).union(set(c2)), existing_cc, set()))
        graph_algorithms.graph = Graph(edge_set)
        graph_algorithms._clique_cover_vertices(cover_vertices, False)
        
        # check that clique cover is one of the expected clique covers
        cc = graph_algorithms.clique_cover
        assert cc in expected_ccs, f'Clique cover {cc} is not one '\
            + f'of the expected clique covers: {expected_ccs}'
        
        # check set of clique covered vertices
        exp_covered_verts = set(
            reduce(lambda c1, c2: set(c1).union(c2), existing_cc, set()))\
            .union(cover_vertices)
        uncovered_vertices = exp_covered_verts.difference(
            graph_algorithms.clique_covered_vertices)
        assert len(uncovered_vertices) == 0, f'Vertices expected to be '\
            + f'covered by cliques are not covered. Uncovered vertices: '\
            + f'{uncovered_vertices}'


def test_clique_cover_vertices_limit_cc_size():
    # test_case: tuple(scope DataFrame, dimension dictionaries, relationships
    # DataFrame, graph edge set, number of groups, dimension value to int
    # mapping, int to dimension value mapping, int to dimension name mapping,
    # dimension name to dimension values mapping, existing clique cover,
    # vertices to cover, list of possible expected clique covers)
    TEST_CASES = [
        (pd.DataFrame({
            'Property': ['Hardware', 'Hardware'],
            'Value': ['HW1', 'HW2'],
            'Status': ['Include', 'Include']
         }), MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1)}, 2,
         {'HW1': 0, 'HW2': 1, 'VM1': 2, 'VM2': 3, 'WL1': 4, 'WL2': 5},
         {0: 'HW1', 1: 'HW2', 2: 'VM1', 3: 'VM2', 4: 'WL1', 5: 'WL2'},
         {0: 'Hardware', 1: 'Vm_Type', 2: 'Workload'},
         {'Hardware': {'HW1', 'HW2'}, 'Vm_Type': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}}, [{1, 3, 5}], {0, 2, 4},
         [[{1, 3, 5}, {0, 2, 4}]]),
        (pd.DataFrame({
            'Property': ['Hardware', 'Vm_Type'],
            'Value': ['HW1', 'VM2'],
            'Status': ['Include', 'Include']
         }), MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1)}, 1,
         {'HW1': 0, 'HW2': 1, 'VM1': 2, 'VM2': 3, 'WL1': 4, 'WL2': 5},
         {0: 'HW1', 1: 'HW2', 2: 'VM1', 3: 'VM2', 4: 'WL1', 5: 'WL2'},
         {0: 'Hardware', 1: 'Vm_Type', 2: 'Workload'},
         {'Hardware': {'HW1', 'HW2'}, 'Vm_Type': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}}, [{0, 2, 4}, {1, 3, 5}], set(),
         [[{0, 2, 4}, {1, 3, 5}]]),
        (pd.DataFrame({
            'Property': ['Hardware', 'Hardware'],
            'Value': ['HW1', 'HW2'],
            'Status': ['Include', 'Include']
         }), MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1)}, 3,
         {'HW1': 0, 'HW2': 1, 'VM1': 2, 'VM2': 3, 'WL1': 4, 'WL2': 5},
         {0: 'HW1', 1: 'HW2', 2: 'VM1', 3: 'VM2', 4: 'WL1', 5: 'WL2'},
         {0: 'Hardware', 1: 'Vm_Type', 2: 'Workload'},
         {'Hardware': {'HW1', 'HW2'}, 'Vm_Type': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}}, [{0, 2, 4}], {1, 3, 5},
         [[{0, 2, 4}, {1, 3, 5}]]),
        (pd.DataFrame({
            'Property': ['Hardware'],
            'Value': ['HW3'],
            'Status': ['Exclude']
         }), MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1)}, 1,
         {'HW1': 0, 'HW2': 1, 'VM1': 2, 'VM2': 3, 'WL1': 4, 'WL2': 5},
         {0: 'HW1', 1: 'HW2', 2: 'VM1', 3: 'VM2', 4: 'WL1', 5: 'WL2'},
         {0: 'Hardware', 1: 'Vm_Type', 2: 'Workload'},
         {'Hardware': {'HW1', 'HW2'}, 'Vm_Type': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}}, [{1, 3, 5}], {0, 2, 4},
         [[{1, 3, 5}]]),
        (pd.DataFrame({
            'Property': ['Hardware'],
            'Value': ['HW3'],
            'Status': ['Exclude']
         }), MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1)}, 2,
         {'HW1': 0, 'HW2': 1, 'VM1': 2, 'VM2': 3, 'WL1': 4, 'WL2': 5},
         {0: 'HW1', 1: 'HW2', 2: 'VM1', 3: 'VM2', 4: 'WL1', 5: 'WL2'},
         {0: 'Hardware', 1: 'Vm_Type', 2: 'Workload'},
         {'Hardware': {'HW1', 'HW2'}, 'Vm_Type': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}}, [{1, 3, 5}], {0, 2, 4},
         [[{1, 3, 5}, {0, 2, 4}]]),
        (pd.DataFrame({
            'Property': ['Hardware'],
            'Value': ['HW3'],
            'Status': ['Exclude']
         }), MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1)}, 1,
         {'HW1': 0, 'HW2': 1, 'VM1': 2, 'VM2': 3, 'WL1': 4, 'WL2': 5},
         {0: 'HW1', 1: 'HW2', 2: 'VM1', 3: 'VM2', 4: 'WL1', 5: 'WL2'},
         {0: 'Hardware', 1: 'Vm_Type', 2: 'Workload'},
         {'Hardware': {'HW1', 'HW2'}, 'Vm_Type': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}}, [], {1, 3, 5, 0, 2, 4},
          [[{1, 3, 5}], [{0, 2, 4}]]),
        (pd.DataFrame({
            'Property': ['Hardware'],
            'Value': ['HW3'],
            'Status': ['Exclude']
         }), MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1)}, 2,
         {'HW1': 0, 'HW2': 1, 'VM1': 2, 'VM2': 3, 'WL1': 4, 'WL2': 5},
         {0: 'HW1', 1: 'HW2', 2: 'VM1', 3: 'VM2', 4: 'WL1', 5: 'WL2'},
         {0: 'Hardware', 1: 'Vm_Type', 2: 'Workload'},
         {'Hardware': {'HW1', 'HW2'}, 'Vm_Type': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}}, [], {1, 3, 5, 0, 2, 4},
          [[{1, 3, 5}, {0, 2, 4}], [{0, 2, 4}, {1, 3, 5}]])
    ]
    for test_case in TEST_CASES:
        scope_df, dim_dicts, rel_df, edge_set, num_groups, dim_val_to_int,\
            int_to_dim_val, int_to_dim_name, dim_name_to_dim_vals,\
            existing_cc, cover_vertices, expected_ccs = test_case
        graph_algorithms = GraphAlgorithms(
            dim_dicts, rel_df, num_groups, MOCK_OBJ_FUNC_DICTS[0], scope_df)
        graph_algorithms.dim_value_to_int = dim_val_to_int
        graph_algorithms.int_to_dim_value = int_to_dim_val
        graph_algorithms.int_to_dim_name = int_to_dim_name
        graph_algorithms.dim_name_to_dim_values = dim_name_to_dim_vals
        graph_algorithms.clique_cover = existing_cc
        graph_algorithms.clique_covered_vertices = set(
            reduce(lambda c1, c2: set(c1).union(set(c2)), existing_cc, set()))
        graph_algorithms.graph = Graph(edge_set)
        graph_algorithms._clique_cover_vertices(cover_vertices, True)
        
        # check that clique cover is one of the expected clique covers
        cc = graph_algorithms.clique_cover
        assert cc in expected_ccs, f'Clique cover {cc} is not one '\
            + f'of the expected clique covers: {expected_ccs}'
        
        # check set of clique covered vertices
        exp_covered_verts = set(
            reduce(lambda c1, c2: set(c1).union(c2),
                   graph_algorithms.clique_cover, set()))
        uncovered_vertices = exp_covered_verts.difference(
            graph_algorithms.clique_covered_vertices)
        assert len(uncovered_vertices) == 0, f'Vertices expected to be '\
            + f'covered by cliques are not covered. Uncovered vertices: '\
            + f'{uncovered_vertices}'


def test_get_clique_cover():
    # test case: tuple(scope DataFrame, dimension dictionaries, relationships
    # DataFrame, graph edge set, max dimension size, dimension value to int
    # mapping, int to dimension name mapping, dimension name to dimension
    # values mapping)
    TEST_CASES = [
        (pd.DataFrame(), MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0],
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1)}, 10,
         {'HW1': 0, 'HW2': 1, 'VM1': 2, 'VM2': 3, 'WL1': 4, 'WL2': 5},
         {0: 'HW1', 1: 'HW2', 2: 'VM1', 3: 'VM2', 4: 'WL1', 5: 'WL2'},
         {'Hardware': {'HW1', 'HW2'}, 'Virtual_Machine': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}}
         ),
        (None, MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[1],
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1), (0, 5), (5, 0), (2, 5), (5, 2)}, 10,
         {'HW1': 0, 'HW2': 1, 'VM1': 2, 'VM2': 3, 'WL1': 4, 'WL2': 5},
         {0: 'HW1', 1: 'HW2', 2: 'VM1', 3: 'VM2', 4: 'WL1', 5: 'WL2'},
         {'Hardware': {'HW1', 'HW2'}, 'Virtual_Machine': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}}
         ),
        (None, MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[2],
         {(0, 2), (2, 0), (0, 3), (3, 0), (1, 2), (2, 1), (1, 3), (3, 1),
          (0, 4), (4, 0), (2, 4), (4, 2), (1, 5), (5, 1), (3, 5), (5, 3)}, 10,
         {'HW1': 0, 'HW2': 1, 'VM1': 2, 'VM2': 3, 'WL1': 4, 'WL2': 5},
         {0: 'HW1', 1: 'HW2', 2: 'VM1', 3: 'VM2', 4: 'WL1', 5: 'WL2'},
         {'Hardware': {'HW1', 'HW2'}, 'Virtual_Machine': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}}
         ),
        (MOCK_SCOPE_DFS[3], [
            {
                'name': 'Hardware',
                'value': 'HW',
                'df': pd.DataFrame({
                    'HW': ['HW2'],
                    'Score': [1]
                })
            },
            {
                'name': 'Virtual_Machine',
                'value': 'VM',
                'df': pd.DataFrame({
                    'VM': ['VM2'],
                    'Score': [1]
                })
            },
            {
                'name': 'Workload',
                'value': 'WL',
                'df': pd.DataFrame({
                    'WL': ['WL2'],
                    'Score': [1]
                })
            }
         ],
         pd.DataFrame({
            'Dimension1': ['Hardware', 'Virtual_Machine', 'Virtual_Machine'],
            'Value1': ['HW2', 'VM2', 'VM2'],
            'Dimension2': ['Workload', 'Workload', 'Hardware'],
            'Value2': ['WL2', 'WL2', 'HW2'],
            'Score': [1, 1, 1],
            'RelationshipMetaData': [
                [], [], [{'name': 'Many_To_One', 'value': 2}]]
         }),
         {(0, 1), (1, 0), (0, 2), (2, 0), (1, 2), (2, 1)}, 1,
         {'HW2': 0, 'VM2': 1, 'WL2': 2}, {0: 'HW2', 1: 'VM2', 2: 'WL2'},
         {'Hardware': {'HW2'}, 'Virtual_Machine': {'VM2'}, 'Workload': {'WL2'}}
         ),
        (MOCK_SCOPE_DFS[1], [
            {
                'name': 'Hardware',
                'value': 'HW',
                'df': pd.DataFrame({
                    'HW': ['HW1'],
                    'Score': [1]
                })
            },
            {
                'name': 'Virtual_Machine',
                'value': 'VM',
                'df': pd.DataFrame({
                    'VM': ['VM1'],
                    'Score': [1]
                })
            },
            {
                'name': 'Workload',
                'value': 'WL',
                'df': pd.DataFrame({
                    'WL': ['WL1'],
                    'Score': [1]
                })
            }
         ],
         pd.DataFrame({
            'Dimension1': ['Hardware', 'Virtual_Machine', 'Virtual_Machine'],
            'Value1': ['HW1', 'VM1', 'VM1'],
            'Dimension2': ['Workload', 'Workload', 'Hardware'],
            'Value2': ['WL1', 'WL1', 'HW1'],
            'Score': [1, 1, 1],
            'RelationshipMetaData': [
                [], [], [{'name': 'Many_To_One', 'value': 2}]]
         }),
         {(0, 1), (1, 0), (1, 2), (2, 1), (0, 2), (2, 0)}, 2,
         {'HW1': 0, 'VM1': 1, 'WL1': 2},
         {0: 'HW1', 1: 'VM1', 2: 'WL1'},
         {'Hardware': {'HW1'}, 'Virtual_Machine': {'VM1'}, 'Workload': {'WL1'}}
         ),
        (MOCK_SCOPE_DFS[4], [
            {
                'name': 'Hardware',
                'value': 'HW',
                'df': pd.DataFrame({
                    'HW': ['HW2'],
                    'Score': [1]
                })
            },
            {
                'name': 'Virtual_Machine',
                'value': 'VM',
                'df': pd.DataFrame({
                    'VM': ['VM1', 'VM2'],
                    'Score': [1, 1]
                })
            },
            {
                'name': 'Workload',
                'value': 'WL',
                'df': pd.DataFrame({
                    'WL': ['WL1', 'WL2'],
                    'Score': [1, 1]
                })
            }
         ],
         pd.DataFrame({
            'Dimension1': ['Virtual_Machine', 'Hardware', 'Virtual_Machine',
                           'Hardware'],
            'Value1': ['VM1', 'HW2', 'VM2', 'HW2'],
            'Dimension2': ['Workload', 'Workload', 'Workload',
                           'Virtual_Machine'],
            'Value2': ['WL1', 'WL2', 'WL2', 'VM2'],
            'Score': [1, 1, 1, 1],
            'RelationshipMetaData': [
                [], [], [], [{'name': 'One_To_Many', 'value': 2}]]
         }),
         {(1, 3), (3, 1), (0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0)}, 2,
         {'HW2': 0, 'VM1': 1, 'VM2': 2, 'WL1': 3, 'WL2': 4},
         {0: 'HW2', 1: 'VM1', 2: 'VM2', 3: 'WL1', 4: 'WL2'},
         {'Hardware': {'HW2'}, 'Virtual_Machine': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}}
         ),
        (MOCK_SCOPE_DFS[4], [
            {
                'name': 'Hardware',
                'value': 'HW',
                'df': pd.DataFrame({
                    'HW': ['HW2'],
                    'Score': [1]
                })
            },
            {
                'name': 'Virtual_Machine',
                'value': 'VM',
                'df': pd.DataFrame({
                    'VM': ['VM1', 'VM2'],
                    'Score': [1, 1]
                })
            },
            {
                'name': 'Workload',
                'value': 'WL',
                'df': pd.DataFrame({
                    'WL': ['WL1', 'WL2'],
                    'Score': [1, 1]
                })
            }
         ],
         pd.DataFrame({
            'Dimension1': ['Virtual_Machine', 'Hardware', 'Virtual_Machine',
                           'Hardware'],
            'Value1': ['VM1', 'HW2', 'VM2', 'HW2'],
            'Dimension2': ['Workload', 'Workload', 'Workload',
                           'Virtual_Machine'],
            'Value2': ['WL1', 'WL2', 'WL2', 'VM2'],
            'Score': [1, 1, 1, 1],
            'RelationshipMetaData': [
                [], [], [], [{'name': 'One_To_Many', 'value': 2}]]
         }),
         {(1, 3), (3, 1), (0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0)}, 1,
         {'HW2': 0, 'VM1': 1, 'VM2': 2, 'WL1': 3, 'WL2': 4},
         {0: 'HW2', 1: 'VM1', 2: 'VM2', 3: 'WL1', 4: 'WL2'},
         {'Hardware': {'HW2'}, 'Virtual_Machine': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}}
         )
    ]
    for test_case in TEST_CASES:
        scope_df, dim_dicts, relationships_df, edge_set, max_dim_size,\
            dim_value_to_int, int_to_dim_value, dim_name_to_dim_values\
            = test_case
        graph_algorithms = GraphAlgorithms(
            dim_dicts, relationships_df, 10, MOCK_OBJ_FUNC_DICTS[0],
            scope_df, max_dim_size)
        # mock creation of dimension mappings
        graph_algorithms.dim_name_to_dim_values =\
            dim_name_to_dim_values
        graph_algorithms.dim_value_to_int = dim_value_to_int
        graph_algorithms.int_to_dim_value = int_to_dim_value
        # mock creation of Graph
        graph_algorithms.graph = Graph(edge_set)
        # get clique cover
        graph_algorithms._get_clique_cover()

        # check that cliques are valid
        for clique in graph_algorithms.clique_cover:
            assert len(clique) == len(dim_dicts), 'Invalid length of clique '\
                + f'{clique}. Expected: {len(dim_dicts)}. Actual: '\
                + f'{len(clique)}'
            clique_verts = list(clique)
            dim_dict_vals = set(reduce(
                lambda s, d: s.union(set(d['df'][d['value']])),
                graph_algorithms.dimension_dicts, set()))
            for vert in clique_verts:
                dim_val = graph_algorithms.int_to_dim_value[vert]
                assert dim_val in dim_dict_vals, f'Dimension value {dim_val} '\
                    + f'present in clique cover but not present in dimension '\
                    + 'dictionaries'
            for i in range(len(clique_verts) - 1):
                dim_val_int1 = clique_verts[i]
                dim_val1 = graph_algorithms.int_to_dim_value[dim_val_int1]
                for j in range(i + 1, len(clique_verts)):
                    dim_val_int2 = clique_verts[j]
                    dim_val2 = graph_algorithms.int_to_dim_value[dim_val_int2]
                    for edge in [(dim_val_int1, dim_val_int2),
                                    (dim_val_int2, dim_val_int1)]:
                        assert edge in edge_set, f'Edge {edge} present in '\
                            + f'clique {clique} but not present in graph '\
                            + f'edge set'
                    sub_rel_df = relationships_df[
                        ((relationships_df['Value1'] == dim_val1)
                        & (relationships_df['Value2'] == dim_val2))
                        | ((relationships_df['Value1'] == dim_val2)
                        & (relationships_df['Value2'] == dim_val1))
                        | ((relationships_df['Value1'] == '<ANY>')
                        & (relationships_df['Value2'] == dim_val1))
                        | ((relationships_df['Value1'] == '<ANY>')
                        & (relationships_df['Value2'] == dim_val2))
                        | ((relationships_df['Value1'] == dim_val1)
                        & (relationships_df['Value2'] == '<ANY>'))
                        | ((relationships_df['Value1'] == dim_val2)
                        & (relationships_df['Value2'] == '<ANY>'))
                        | ((relationships_df['Value1'] == '<ANY>')
                        & (relationships_df['Value2'] == '<ANY>'))
                    ]
                    assert len(sub_rel_df) > 0,\
                        f'Dimension values {dim_val1} and {dim_val2} are in '\
                        + f'a clique but have no specified relationships '\
                        + f'between them'
        
        # perform additional checks based on whether scope DataFrame is
        # provided or not
        if scope_df is not None and len(scope_df) != 0:
            # check that max dimension size is adhered to
            for i in range(len(dim_dicts)):
                dim_dict = dim_dicts[i]
                include_vals = set(graph_algorithms.scope_df[
                    (graph_algorithms.scope_df['Property']
                     == dim_dict['name'])
                    & (graph_algorithms.scope_df['Status'] == 'Include')
                ]['Value'])
                exclude_vals = set(graph_algorithms.scope_df[
                    (graph_algorithms.scope_df['Property']
                     == dim_dict['name'])
                    & (graph_algorithms.scope_df['Status'] == 'Exclude')
                ]['Value'])
                dim_dict_vals = set(dim_dict['df'][dim_dict['value']])
                if len(include_vals) != 0:
                    dim_dict_vals = dim_dict_vals.intersection(include_vals)
                if len(exclude_vals) != 0:
                    dim_dict_vals = dim_dict_vals.difference(exclude_vals)
                orig_dim_dict_vals = set(dim_dict['df'][dim_dict['value']])
                graph_val_dim_dict = graph_algorithms.dimension_dicts[i]
                graph_dim_vals = graph_val_dim_dict['df'][
                    graph_val_dim_dict['value']]
                act_len = len(graph_dim_vals)
                if len(include_vals) != 0:
                    exp_len = len(dim_dict_vals)
                elif len(include_vals) == 0 and len(exclude_vals) == 0:
                    exp_len = min(len(orig_dim_dict_vals), max_dim_size)
                else:
                    exp_len = min(len(dim_dict_vals), max_dim_size)
                assert act_len == exp_len, 'Incorrect dimension size for '\
                    + f'{dim_dict["name"]} dimension. Expected: {exp_len}. '\
                    + f'Actual: {act_len}'

            # check that all vertices pertaining to dimension values in scope
            # function are covered
            covered_verts = graph_algorithms.clique_covered_vertices
            scope_values = graph_algorithms.scope_df[
                graph_algorithms.scope_df['Status'] == 'Include']['Value']
            dim_values = set()
            for dim_dict in dim_dicts:
                dim_values = dim_values.union(
                    set(dim_dict['df'][dim_dict['value']]))
            scope_verts = set()
            for scope_value in scope_values:
                if scope_value in dim_values:
                    scope_verts.add(
                        graph_algorithms.dim_value_to_int[scope_value])
            uncovered_scope_verts = scope_verts.difference(covered_verts)
            uncovered_scope_vals = set(map(
                lambda v: graph_algorithms.int_to_dim_value[v],
                uncovered_scope_verts))
            assert len(uncovered_scope_vals) == 0, 'The following scope '\
                + 'dimension values are not covered by the cliques: '\
                + f'{uncovered_scope_vals}'
        else:
            # check that all dimension values are covered 
            for dim_dict in dim_dicts:
                dim_vals = set(dim_dict['df'][dim_dict['value']])
                dim_val_ints = set(map(
                    lambda v: graph_algorithms.dim_value_to_int[v], dim_vals))
                uncovered_verts = dim_val_ints.difference(
                    graph_algorithms.clique_covered_vertices)
                uncovered_vals = set(map(
                    lambda v: graph_algorithms.int_to_dim_value[v],
                    uncovered_verts))
                assert len(uncovered_vals) == 0, 'The following dimension '\
                    + 'values are not covered by the cliques: '\
                    + f'{uncovered_vals}'


def test_remove_dim_values():
    # test case: tuple(set of dimension values to remove, dimension dicts,
    # relationships DataFrame, graph edges)
    TEST_CASES = [
        ({'HW1'}, MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0],
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1)}
         ),
        ({'HW1', 'VM2'}, MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[1],
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1), (0, 5), (5, 0), (2, 5), (5, 2)}
         ),
        ({'VM1', 'WL2'}, MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[2],
         {(0, 2), (2, 0), (0, 3), (3, 0), (1, 2), (2, 1), (1, 3), (3, 1),
          (0, 4), (4, 0), (2, 4), (4, 2), (1, 5), (5, 1), (3, 5), (5, 3)}
         )
    ]
    for test_case in TEST_CASES:
        remove_set, dim_dicts, rel_df, graph_edges = test_case
        dim_value_to_int = {'HW1': 0, 'HW2': 1, 'VM1': 2, 'VM2': 3, 'WL1': 4,
                            'WL2': 5}
        int_to_dim_value = {0: 'HW1', 1: 'HW2', 2: 'VM1', 3: 'VM2', 4: 'WL1',
                            5: 'WL2'}
        dim_name_to_dim_values = {'Hardware': {'HW1', 'HW2'},
                                  'Virtual_Machine': {'VM1', 'VM2'},
                                  'Workload': {'WL1', 'WL2'}}
        graph_algorithms = GraphAlgorithms(
            dim_dicts, rel_df, 10, MOCK_OBJ_FUNC_DICTS[0])
        graph_algorithms.dim_value_to_int = dim_value_to_int
        graph_algorithms.int_to_dim_value = int_to_dim_value
        graph_algorithms.dim_name_to_dim_values = dim_name_to_dim_values
        graph_algorithms.graph = Graph(graph_edges)
        graph_algorithms._remove_dim_values(remove_set)

        # check that each specified value to remove was removed
        dim_dict_vals = set()
        for dim_dict in graph_algorithms.dimension_dicts:
            dim_dict_vals = dim_dict_vals.union(set(dim_dict['df']
                                                    [dim_dict['value']]))
        rel_dim_vals = set(graph_algorithms.relationships_df['Value1'])\
            .union(set(graph_algorithms.relationships_df['Value2']))
        dim_name_vals = set()
        for _, dim_vals in graph_algorithms.dim_name_to_dim_values.items():
            dim_name_vals = dim_name_vals.union(set(dim_vals))
        for remove_val in remove_set:
            remove_int = dim_value_to_int[remove_val]

            # check that dimension value is not in dim dicts
            assert remove_val not in dim_dict_vals, 'Dimension value '\
                + f'{remove_val} not removed from dimension dictionaries'
            
            # check that dimension value is not in rel DF
            assert remove_val not in rel_dim_vals, 'Dimension value '\
                + f'{remove_val} not removed from relationships DataFrame'
            
            # check that dimension value and integer are not in dimension value
            # to integer mapping
            assert remove_val not in graph_algorithms.dim_value_to_int.keys(),\
                f'Dimension value {remove_val} not removed from dimension '\
                + 'value to integer mapping'
            assert remove_int not in graph_algorithms.dim_value_to_int\
                .values(), f'Dimension value integer {remove_int} not '\
                + 'removed from dimension value to integer mapping'

            # check that dimension value and integer are not in integer to
            # dimension value mapping
            assert remove_val not in graph_algorithms.int_to_dim_value\
                .values(), f'Dimension value {remove_val} not removed from '\
                + 'integer to dimension value mapping'
            assert remove_int not in graph_algorithms.int_to_dim_value\
                .keys(), f'Dimension value integer {remove_int} not '\
                + 'removed from integer to dimension value mapping'

            # check that dimension value is not in dimension name to dimension
            # values mapping
            assert remove_val not in dim_name_vals, 'Dimension value '\
                + f'{remove_val} not removed from dimension name to '\
                + 'dimension value mapping'
            
            # check that dimension value integer is not in graph edges
            sub_edges = set(
                filter(lambda e: e[0] == remove_int or e[1] == remove_int,
                       graph_algorithms.graph.edges))
            assert len(sub_edges) == 0, 'Dimension value integer '\
                + f'{remove_int} not removed from graph'


def test_scope_to_compatible():
    # test case: (scope DataFrame, graph edges, integer to dimension value
    # mapping, dimension value to integer mapping, dimension name to dimension
    # value mapping, expected edge set of graph after removing vertices)
    TEST_CASES = [
        (MOCK_SCOPE_DFS[4],
         {(0, 2), (2, 0), (0, 4), (4, 0), (2, 4), (4, 2),
          (1, 3), (3, 1)},
         {0: 'HW2', 1: 'VM1', 2: 'VM2', 3: 'WL1', 4: 'WL2'},
         {'HW2': 0, 'VM1': 1, 'VM2': 2, 'WL1': 3, 'WL2': 4},
         {'Hardware': {'HW2'}, 'Virtual_Machine': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}},
         {(0, 2), (2, 0), (0, 4), (4, 0), (2, 4), (4, 2)}
         ),
        (pd.DataFrame({
            'Property': ['Hardware'],
            'Value': ['HW1'],
            'Status': ['Include']
         }),
         {(0, 1), (1, 0), (0, 3), (3, 0), (1, 3), (3, 1),
          (2, 4), (4, 2)},
         {0: 'HW1', 1: 'VM1', 2: 'VM2', 3: 'WL1', 4: 'WL2'},
         {'HW1': 0, 'VM1': 1, 'VM2': 2, 'WL1': 3, 'WL2': 4},
         {'Hardware': {'HW1'}, 'Virtual_Machine': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}},
         {(0, 1), (1, 0), (0, 3), (3, 0), (1, 3), (3, 1)}
         ),
        (None,
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1)},
         {0: 'HW1', 1: 'HW2', 2: 'VM1', 3: 'VM2', 4: 'WL1', 5: 'WL2'},
         {'HW1': 0, 'HW2': 1, 'VM1': 2, 'VM2': 3, 'WL1': 4, 'WL2': 5},
         {'Hardware': {'HW1', 'HW2'}, 'Virtual_Machine': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}},
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1)}
         )
    ]
    for test_case in TEST_CASES:
        scope_df, edges, int_to_dim_value, dim_value_to_int,\
            dim_name_to_dim_values, exp_edges = test_case
        graph_algorithms = GraphAlgorithms(
            MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 10,
            MOCK_OBJ_FUNC_DICTS[0], scope_df)
        graph_algorithms.graph = Graph(edges)
        graph_algorithms.int_to_dim_value = int_to_dim_value
        graph_algorithms.dim_value_to_int = dim_value_to_int
        graph_algorithms.dim_name_to_dim_values = dim_name_to_dim_values
        graph_algorithms._scope_to_compatible()
        act_edges = graph_algorithms.graph.edges
        assert act_edges == exp_edges, 'Incorrect graph edge '\
            + f'set. Expected: {exp_edges}. Actual: {act_edges}'


def test_remove_uncoverable_vertices():
    # test case: tuple(graph edges, expected edge set of graph after removing
    # vertices)
    PASS_CASES = [
        ({(0, 2), (2, 0), (0, 4), (4, 0), (2, 4), (4, 2),
          (1, 3), (3, 1)},
         {0: 'HW2', 1: 'VM1', 2: 'VM2', 3: 'WL1', 4: 'WL2'},
         {'HW2': 0, 'VM1': 1, 'VM2': 2, 'WL1': 3, 'WL2': 4},
         {'Hardware': {'HW2'}, 'Virtual_Machine': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}},
         {0: 'Hardware', 1: 'Virtual_Machine', 2: 'Virtual_Machine',
          3: 'Workload', 4: 'Workload'},
         {'Hardware': {0}, 'Virtual_Machine': {1, 2}, 'Workload': {3, 4}},
         {(0, 2), (2, 0), (0, 4), (4, 0), (2, 4), (4, 2)},
         None
         ),
        ({(0, 1), (1, 0), (0, 3), (3, 0), (1, 3), (3, 1),
          (2, 4), (4, 2)},
         {0: 'HW1', 1: 'VM1', 2: 'VM2', 3: 'WL1', 4: 'WL2'},
         {'HW1': 0, 'VM1': 1, 'VM2': 2, 'WL1': 3, 'WL2': 4},
         {'Hardware': {'HW1'}, 'Virtual_Machine': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}},
         {0: 'Hardware', 1: 'Virtual_Machine', 2: 'Virtual_Machine',
          3: 'Workload', 4: 'Workload'},
         {'Hardware': {0}, 'Virtual_Machine': {1, 2}, 'Workload': {3, 4}},
         {(0, 1), (1, 0), (0, 3), (3, 0), (1, 3), (3, 1)},
         pd.DataFrame()
         ),
        ({(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1)},
         {0: 'HW1', 1: 'HW2', 2: 'VM1', 3: 'VM2', 4: 'WL1', 5: 'WL2'},
         {'HW1': 0, 'HW2': 1, 'VM1': 2, 'VM2': 3, 'WL1': 4, 'WL2': 5},
         {'Hardware': {'HW1', 'HW2'}, 'Virtual_Machine': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}},
         {0: 'Hardware', 1: 'Hardware', 2: 'Virtual_Machine',
          3: 'Virtual_Machine', 4: 'Workload', 5: 'Workload'},
         {'Hardware': {0, 1}, 'Virtual_Machine': {2, 3}, 'Workload': {4, 5}},
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1)},
         pd.DataFrame({'Property': [], 'Value': [], 'Status': []})
         )
    ]
    FAIL_CASES = [
        ({(0, 2), (2, 0), (0, 4), (4, 0), (2, 4), (4, 2),
          (1, 3), (3, 1)},
         {0: 'HW2', 1: 'VM1', 2: 'VM2', 3: 'WL1', 4: 'WL2'},
         {'HW2': 0, 'VM1': 1, 'VM2': 2, 'WL1': 3, 'WL2': 4},
         {'Hardware': {'HW2'}, 'Virtual_Machine': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}},
         {0: 'Hardware', 1: 'Virtual_Machine', 2: 'Virtual_Machine',
          3: 'Workload', 4: 'Workload'},
         {'Hardware': {0}, 'Virtual_Machine': {1, 2}, 'Workload': {3, 4}},
         {(0, 2), (2, 0), (0, 4), (4, 0), (2, 4), (4, 2)},
         pd.DataFrame({
             'Property': ['Hardware', 'Virtual_Machine', 'Virtual_Machine',
                          'Workload', 'Workload'],
             'Value': ['HW2', 'VM1', 'VM2', 'WL1', 'WL2'],
             'Status': ['Include'] * 5
         })
         # expect Exception because some scope values do not have edges
         # to a dimension in the graph and are removed
         ),
        ({(0, 1), (1, 0), (0, 3), (3, 0), (1, 3), (3, 1),
          (2, 4), (4, 2)},
         {0: 'HW1', 1: 'VM1', 2: 'VM2', 3: 'WL1', 4: 'WL2'},
         {'HW1': 0, 'VM1': 1, 'VM2': 2, 'WL1': 3, 'WL2': 4},
         {'Hardware': {'HW1'}, 'Virtual_Machine': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}},
         {0: 'Hardware', 1: 'Virtual_Machine', 2: 'Virtual_Machine',
          3: 'Workload', 4: 'Workload'},
         {'Hardware': {0}, 'Virtual_Machine': {1, 2}, 'Workload': {3, 4}},
         {(0, 1), (1, 0), (0, 3), (3, 0), (1, 3), (3, 1)},
         pd.DataFrame({
             'Property': ['Hardware', 'Virtual_Machine', 'Virtual_Machine',
                          'Workload', 'Workload'],
             'Value': ['HW1', 'VM1', 'VM2', 'WL1', 'WL2'],
             'Status': ['Include'] * 5
         })
         # expect Exception because some scope values do not have edges
         # to a dimension in the graph and are removed
         )
    ]
    for cases, exception in [(PASS_CASES, False), (FAIL_CASES, True)]:
        for test_case in cases:
            edges, int_to_dim_value, dim_value_to_int, dim_name_to_dim_values,\
                int_to_dim_name, dim_name_to_ints, exp_edges, scope_df\
                    = test_case
            graph_algorithms = GraphAlgorithms(
                MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 10,
                MOCK_OBJ_FUNC_DICTS[0], scope_df)
            graph_algorithms.graph = Graph(edges)
            graph_algorithms.int_to_dim_value = int_to_dim_value
            graph_algorithms.dim_value_to_int = dim_value_to_int
            graph_algorithms.dim_name_to_dim_values = dim_name_to_dim_values
            graph_algorithms.int_to_dim_name = int_to_dim_name
            graph_algorithms.dim_name_to_ints = dim_name_to_ints
            try:
                graph_algorithms._remove_uncoverable_vertices()
            except Exception:
                check_exception(True, exception, test_case)
            else:
                check_exception(False, exception, test_case)
                act_edges = graph_algorithms.graph.edges
                assert act_edges == exp_edges, 'Incorrect graph edge '\
                    + f'set. Expected: {exp_edges}. Actual: {act_edges}'


def test_validate_graph():
    # test case: tuple(scope DataFrame, dimension dicts, relationships
    # DataFrame, objective function, clique cover, clique covered vertices,
    # graph edge set, dimension value integer to dimension value mapping,
    # dimension name to dimension values mapping)
    PASS_CASES = [
        (None, MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0],
         2, MOCK_OBJ_FUNC_DICTS[0],
         {(0, 2, 4), (1, 3, 5)}, {0, 1, 2, 3, 4, 5},
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1)}
         ),
        (pd.DataFrame(), MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[1],
         3, MOCK_OBJ_FUNC_DICTS[0],
         {(0, 2, 4), (1, 3, 5)}, {0, 1, 2, 3, 4, 5},
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1), (0, 5), (5, 0), (2, 5), (5, 2)}
         ),
        (pd.DataFrame(), MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[2],
         5, MOCK_OBJ_FUNC_DICTS[0],
         {(0, 2, 4), (1, 3, 5)}, {0, 1, 2, 3, 4, 5},
         {(0, 2), (2, 0), (0, 3), (3, 0), (1, 2), (2, 1), (1, 3), (3, 1),
          (0, 4), (4, 0), (2, 4), (4, 2), (1, 5), (5, 1), (3, 5), (5, 3)}
         ),
        (MOCK_SCOPE_DFS[1], MOCK_DIMENSION_DICTS[0:3],
         MOCK_RELATIONSHIPS_DFS[0], 1, MOCK_OBJ_FUNC_DICTS[0],
         {(0, 2, 4)}, {0, 2, 4},
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1)}
         ),
        (MOCK_SCOPE_DFS[3], MOCK_DIMENSION_DICTS[0:3],
         MOCK_RELATIONSHIPS_DFS[0], 1, MOCK_OBJ_FUNC_DICTS[0],
         {(1, 3, 5)}, {1, 3, 5},
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1)}),
        (MOCK_SCOPE_DFS[1], MOCK_DIMENSION_DICTS[0:3],
         MOCK_RELATIONSHIPS_DFS[0], 2, MOCK_OBJ_FUNC_DICTS[4],
         {(0, 2, 4)}, {0, 2, 4},
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1)}
         ),
        (MOCK_SCOPE_DFS[1], MOCK_DIMENSION_DICTS[0:3],
         MOCK_RELATIONSHIPS_DFS[0], 2, MOCK_OBJ_FUNC_DICTS[3],
         {(0, 2, 4)}, {0, 2, 4},
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1)}
         )
    ]
    WARNING_CASES = [
        (None, MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0],
         2, MOCK_OBJ_FUNC_DICTS[0],
         {(0, 2, 4)}, {0, 2, 4}, # vertices 1, 3, 5 not covered
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1)}
         ),
        (pd.DataFrame(), MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0],
         1, MOCK_OBJ_FUNC_DICTS[0],
         {(1, 3, 5)}, {1, 3, 5}, # vertices 0, 2, 4 not covered
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1)}
         )
    ]
    FAIL_CASES = [
        (MOCK_SCOPE_DFS[3], MOCK_DIMENSION_DICTS[0:3],
         MOCK_RELATIONSHIPS_DFS[0], 2, MOCK_OBJ_FUNC_DICTS[0],
         {(0, 2, 4)}, {0, 2, 4}, # vertices 1, 3, 5 not covered
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1)}
         ),
        (MOCK_SCOPE_DFS[2], MOCK_DIMENSION_DICTS[0:3],
         MOCK_RELATIONSHIPS_DFS[0], 2, MOCK_OBJ_FUNC_DICTS[0],
         {(1, 3, 5)}, {1, 3, 5}, # vertices 0, 2, 4 not covered
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1)}
         ),
        (MOCK_SCOPE_DFS[2], MOCK_DIMENSION_DICTS[0:3],
         MOCK_RELATIONSHIPS_DFS[0], 2,
         {
            'type': 'combination',
            'specifics': [{
                'combinations': [
                    {
                        'combination': [
                            {
                                'dimension': 'Hardware',
                                'value': 'HW3'
                            },
                            {
                                'dimension': 'Virtual_Machine',
                                'value': 'VM3'
                            },
                            {
                                'dimension': 'Workload',
                                'value': 'WL3'
                            },
                        ],
                        'metric_values': [
                            {
                                'name': 'Score',
                                'value': 1
                            }
                        ]
                    }
                ],
                'metric': 'Score',
                'objective_function': 'mse'
            }]
         },
         {(1, 3, 5)}, {1, 3, 5},
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1)}
         # expect Exception because combination-based objective function
         # will have an empty list of combinations (after removing the 
         # combinations that do not correspond to remaining dimension values)
         ),
        (None, MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0],
         1, MOCK_OBJ_FUNC_DICTS[0],
         {(0, 2, 4), (1, 3, 5)}, {0, 1, 2, 3, 4, 5},
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1)}
         # expect Exception because size of clique cover (2) exceeds number of
         # groups (1)
         ),
        (pd.DataFrame(), MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[1],
         1, MOCK_OBJ_FUNC_DICTS[0],
         {(0, 2, 4), (1, 3, 5)}, {0, 1, 2, 3, 4, 5},
         {(0, 4), (4, 0), (2, 4), (4, 2), (0, 2), (2, 0), (1, 3), (3, 1),
          (3, 5), (5, 3), (1, 5), (5, 1), (0, 5), (5, 0), (2, 5), (5, 2)}
         # expect Exception because size of clique cover (2) exceeds number of
         # groups (1)
         ),
    ]
    # warnings will be raised like errors, makes it easier to check if
    # intended warnings were raised
    warnings.filterwarnings("error")
    for cases, raised_type in [(PASS_CASES, None), (WARNING_CASES, 'warning'),
                               (FAIL_CASES, 'exception')]:
        if raised_type is None:
            exception = False
            warning = False
        elif raised_type == 'warning':
            exception = False
            warning = True
        else:
            exception = True
            warning = False
        for test_case in cases:
            (scope_df, dim_dicts, relationships_df, num_groups, obj_func,
             clique_cover, clique_covered_vertices, edge_set) = test_case
            int_to_dim_value = {0: 'HW1', 1: 'HW2', 2: 'VM1', 3: 'VM2',
                                4: 'WL1', 5: 'WL2'}
            dim_value_to_int = {'HW1': 0, 'HW2': 1, 'VM1': 2, 'VM2': 3,
                                'WL1': 4, 'WL2': 5}
            dim_name_to_dim_values = {
                'Hardware': {'HW1', 'HW2'},
                'Virtual_Machine': {'VM1', 'VM2'},
                'Workload': {'WL1', 'WL2'}
            }
            try:
                graph_algorithms = GraphAlgorithms(
                    dim_dicts, relationships_df, num_groups,
                    MOCK_OBJ_FUNC_DICTS[0], scope_df)
                # mock graph and clique covered vertices
                graph_algorithms.graph = Graph(edge_set)
                graph_algorithms.int_to_dim_value = int_to_dim_value
                graph_algorithms.dim_value_to_int = dim_value_to_int
                graph_algorithms.dim_name_to_dim_values =\
                    dim_name_to_dim_values
                graph_algorithms.clique_cover = clique_cover
                graph_algorithms.clique_covered_vertices =\
                    clique_covered_vertices
                # validate graph
                graph_algorithms._validate_graph()
            except UncoverableDimensionValuesWarning:
                check_warning(True, warning, test_case)
            except Exception:
                check_exception(True, exception, test_case)
            else:
                check_exception(False, exception, test_case)
                check_warning(False, warning, test_case)

                # get uncoverable vertices 
                vertices = set(reduce(
                    lambda s, e: s.union({e[0], e[1]}), edge_set, set()))
                uncoverable_vertices = vertices.difference(
                    clique_covered_vertices)
                uncoverable_dim_vals = set(map(lambda v: int_to_dim_value[v],
                                               uncoverable_vertices))

                # check that uncoverable vertices removed from graph
                graph_edges = graph_algorithms.graph.edges
                graph_vertices = set(reduce(
                    lambda s, e: s.union({e[0], e[1]}), graph_edges, set()))
                invalid_vertices = graph_vertices.intersection(
                    uncoverable_vertices)
                assert len(invalid_vertices) == 0, 'Uncoverable vertices '\
                    + 'that should have been removed from graph are present '\
                    + f'in graph: {invalid_vertices}'
                
                # check that uncoverable vertices removed from dimension dicts
                for i in range(len(graph_algorithms.dimension_dicts)):
                    dim_dict = graph_algorithms.dimension_dicts[i]
                    uncoverable_dim_val_df = dim_dict['df'][
                        (dim_dict['df'][dim_dict['value']].isin(
                        uncoverable_dim_vals))]
                    assert len(uncoverable_dim_val_df) == 0, 'Uncoverable '\
                        + f'dimension values in dimension dictionary {i}: '\
                        + f'{uncoverable_dim_val_df}'
                    
                # check that uncoverable vertics removed from relationships
                # DataFrame
                uncoverable_dim_val_rel_df =\
                    graph_algorithms.relationships_df[
                        (graph_algorithms.relationships_df['Value1']
                         .isin(uncoverable_dim_vals))
                        | (graph_algorithms.relationships_df['Value2']
                           .isin(uncoverable_dim_vals))
                    ]
                assert len(uncoverable_dim_val_rel_df) == 0, 'Uncoverable '\
                        + f'dimension values in relationships DataFrame: '\
                        + f'{uncoverable_dim_val_rel_df}'
                
                # check dimension name to dimension values mapping
                for dim_name, dim_vals in graph_algorithms\
                        .dim_name_to_dim_values.items():
                    uncovered_vals = set(dim_vals).intersection(
                        uncoverable_dim_vals)
                    diff_vals = dim_vals.difference(dim_name_to_dim_values
                                                   [dim_name])
                    assert dim_name in dim_name_to_dim_values.keys() and\
                        len(diff_vals) == 0,\
                        f'Mapping between dimension {dim_name} and dimension '\
                        + f'values {diff_vals} was not present in original '\
                        + f'dimension name to dimension value mapping'
                    assert len(uncovered_vals) == 0, 'Uncoverable dimension '\
                        + f'values in dimension name to dimension values '\
                        + f'mapping. Dimension name: {dim_name}, Dimension '\
                        + f'value: {dim_vals}'

                # check dimension value to dimension value integer mapping
                for dim_val, dim_int in graph_algorithms\
                        .dim_value_to_int.items():
                    assert dim_val in dim_value_to_int.keys() and\
                        dim_int == dim_value_to_int[dim_val],\
                        f'Dimension value {dim_val} was not mapped to '\
                        + f'{dim_int} in original dimension value to '\
                        + f'dimension value integer mapping'
                    assert dim_val not in uncoverable_dim_vals, 'Uncoverable '\
                        + f'dimension value {dim_val} in dimension value to '\
                        + 'dimension value integer mapping'
                    assert dim_int not in uncoverable_vertices, 'Uncoverable '\
                        + f'vertex {dim_int} in dimension value to dimension '\
                        + 'value integer mapping'

                # check integer to dimension value mapping
                for dim_int, dim_val in graph_algorithms\
                        .int_to_dim_value.items():
                    assert dim_int in int_to_dim_value.keys() and\
                        dim_val == int_to_dim_value[dim_int],\
                        f'Dimension value integer {dim_int} was not mapped to'\
                        + f' {dim_val} in original dimension value integer '\
                        + f'to dimension value mapping'
                    assert dim_val not in uncoverable_dim_vals, 'Uncoverable '\
                        + f'dimension value {dim_val} in dimension value '\
                        + 'integer to dimension value mapping'
                    assert dim_int not in uncoverable_vertices, 'Uncoverable '\
                        + f'vertex {dim_int} in dimension value integer to '\
                        + 'dimension value mapping'

                # if objective function is combination-based, check that
                # combinations only correspond to valid dimension values
                obj_func = graph_algorithms.objective_function
                if obj_func['type'] == 'combination':
                    for spec in obj_func['specifics']:
                        combinations = spec['combinations']
                        assert len(combinations) != 0, 'Combination based '\
                            + 'objective function specifics contains an '\
                            + 'empty list of combinations'
                        for combo_info in combinations:
                            for dim_val in combo_info['combination']:
                                dimension = dim_val['dimension']
                                value = dim_val['value']
                                assert value != '<ANY>' and value not in\
                                    graph_algorithms.dim_name_to_dim_values[
                                        dimension],\
                                    'Combination based objective function '\
                                    + 'contains combination with invalid '\
                                    + 'dimension value. Dimension: '\
                                    + f'{dimension}. Value: {value}. '\
                                    + 'Combination: '\
                                    + f'{combo_info["combination"]}'
    # no longer raise warnings like errors
    warnings.filterwarnings("default")
