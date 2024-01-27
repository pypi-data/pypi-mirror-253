# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from envdesign_model.io_validation.input_validation import InputValidation
from envdesign_model.graph_algorithms.graph_algorithms import GraphAlgorithms
from envdesign_model.optimization.optimization_strategies.optimization_params\
    import OptimizationParams, _update_target_val_dict, _get_combination_tuples
from envdesign_model.optimization.objective_functions.mean_squared_error\
    import DimensionMSE, RelationshipMSE, CombinationMSE
from tests.mock_data import (MOCK_DIMENSION_DICTS, MOCK_RELATIONSHIPS_DFS,
                             MOCK_OBJ_FUNC_DICTS)


def test_optimization_params():
    # test case: (dimension dicts, relationships DataFrame, number of groups,
    # objective function, expected objective functions)
    TEST_CASES = [
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 100,
         MOCK_OBJ_FUNC_DICTS[0],
         {
            0: DimensionMSE({0: 1, 1: 1}, 0.2, True),
            1: DimensionMSE({2: 1, 3: 1}, 0.4, True),
            2: DimensionMSE({4: 1, 5: 1}, 0.4, True),
         }
         ),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[1], 100,
         MOCK_OBJ_FUNC_DICTS[1],
         {
            (0, 1): RelationshipMSE(
                {(0, 2): 1, (1, 3): 1}, 0.3, True),
            (0, 2): RelationshipMSE(
                {(0, 4): 1, (0, 5): 1, (1, 5): 1}, 0.3, True),
            (1, 2): RelationshipMSE(
                {(2, 4): 1, (2, 5): 1, (3, 5): 1}, 0.4, True),
         }
         ),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[3], 100,
         MOCK_OBJ_FUNC_DICTS[1],
         {
            (0, 1): RelationshipMSE(
                {(0, 2): 1, (1, 2): 2, (1, 3): 1}, 0.3, True),
            (0, 2): RelationshipMSE(
                {(0, 4): 1, (1, 5): 1}, 0.3, True),
            (1, 2): RelationshipMSE(
                {(2, 4): 1, (3, 5): 1}, 0.4, True),
         }
         ),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[4], 100,
         MOCK_OBJ_FUNC_DICTS[1],
         {
            (0, 1): RelationshipMSE(
                {(0, 2): 3, (0, 3): 3, (1, 3): 2}, 0.3, True),
            (0, 2): RelationshipMSE(
                {(0, 4): 1, (1, 5): 1}, 0.3, True),
            (1, 2): RelationshipMSE(
                {(2, 4): 1, (3, 5): 1}, 0.4, True),
         }
         ),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[7], 100,
         MOCK_OBJ_FUNC_DICTS[1],
         {
            (0, 1): RelationshipMSE(
                {(0, 2): 4, (0, 3): 3, (1, 3): 5}, 0.3, True),
            (0, 2): RelationshipMSE(
                {(0, 4): 1, (1, 5): 1}, 0.3, True),
            (1, 2): RelationshipMSE(
                {(2, 4): 1, (3, 5): 1}, 0.4, True),
         }
         ),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[8], 100,
         MOCK_OBJ_FUNC_DICTS[1],
         {
            (0, 1): RelationshipMSE(
                {(0, 2): 4, (0, 3): 2, (1, 3): 5}, 0.3, True),
            (0, 2): RelationshipMSE(
                {(0, 4): 1, (1, 5): 1}, 0.3, True),
            (1, 2): RelationshipMSE(
                {(2, 4): 1, (3, 5): 1}, 0.4, True),
         }
         ),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 100,
         MOCK_OBJ_FUNC_DICTS[2],
         CombinationMSE(
            {
                (0, 2, 4): 1,
                (1, 3, 5): 1,
                (0, 2, 5): 2,
                (0, 3, 5): 2,
                (1, 2, 5): 1,
                (0, 3, 4): 2
            },
            True
         )
         ),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 100,
         MOCK_OBJ_FUNC_DICTS[3],
         CombinationMSE(
            {
                (0, 2, 4): 1,
                (0, 2, 5): 1,
                (0, 3, 4): 1,
                (0, 3, 5): 1,
                (1, 2, 4): 1,
                (1, 2, 5): 1,
                (1, 3, 4): 1,
                (1, 3, 5): 1,
            },
            True
         )
         ),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 100,
         MOCK_OBJ_FUNC_DICTS[5],
         CombinationMSE(
            {
                (0, 2, 4): 2,
                (1, 3, 5): 1,
                (0, 2, 5): 2,
                (0, 3, 5): 2,
                (1, 2, 5): 1,
                (0, 3, 4): 2
            },
            True
         )
         )
    ]
    for test_case in TEST_CASES:
        # process input validation and graph validation instances
        (dim_dicts, relationships_df, num_groups, obj_func,
         objective_functions) = test_case
        input_validation = InputValidation(
            dim_dicts, relationships_df, num_groups, obj_func)
        input_validation.process()
        graph_validation = GraphAlgorithms(
            dim_dicts, relationships_df, num_groups, obj_func)
        graph_validation.process()
        dim_int_to_dim_name = {
            0: 'Hardware', 1: 'Virtual_Machine', 2: 'Workload'}
        dim_name_to_dim_int = {
            'Hardware': 0, 'Virtual_Machine': 1, 'Workload': 2}
        dim_name_to_dim_dict = {
            'Hardware': MOCK_DIMENSION_DICTS[0],
            'Virtual_Machine': MOCK_DIMENSION_DICTS[1],
            'Workload': MOCK_DIMENSION_DICTS[2]}

        # create and check optimization parameters
        opt_params = OptimizationParams(input_validation, graph_validation)
        assert opt_params.dim_int_to_dim_name == dim_int_to_dim_name,\
            'Mapping of dimension integers to dimension names is incorrect. '\
            + f'Expected: {dim_int_to_dim_name}, Actual: '\
            + f'{opt_params.dim_int_to_dim_name}'
        assert opt_params.dim_name_to_dim_int == dim_name_to_dim_int,\
            'Mapping of dimension names to dimension integers is incorrect. '\
            + f'Expected: {dim_name_to_dim_int}, Actual: '\
            + f'{opt_params.dim_name_to_dim_int}'
        exp_keys = set(dim_name_to_dim_dict.keys())
        act_keys = set(opt_params.dim_name_to_dim_dict.keys())
        assert exp_keys == act_keys, 'Incorrect dimension names for mapping '\
            + f'between dimension names and dimension dictionaries. Expected:'\
            + f' {exp_keys}. Actual: {act_keys}'
        for key in exp_keys:
            exp_name = dim_name_to_dim_dict[key]['name']
            act_name = opt_params.dim_name_to_dim_dict[key]['name']
            assert exp_name == act_name, 'Incorrect dimension name. Expected:'\
                + f' {exp_name}. Actual: {act_name}'
            exp_value = dim_name_to_dim_dict[key]['value']
            act_value = opt_params.dim_name_to_dim_dict[key]['value']
            assert exp_value == act_value, 'Incorrect dimension value column.'\
                + f' Expected:  {exp_value}. Actual: {act_value}'
            exp_df = dim_name_to_dim_dict[key]['df']
            act_df = opt_params.dim_name_to_dim_dict[key]['df']
            assert exp_df.equals(act_df), 'Incorrect dimension DataFrame. '\
                + f'Expected: {exp_df}. Actual: {act_df}'
        assert opt_params.objective_functions == objective_functions,\
            'Objective functions are incorrect. Expected: '\
            + f'{objective_functions}, Actual: '\
            + f'{opt_params.objective_functions}'


def test_get_combination_tuples():
    # test case: (combination, list of expected combination tuples)
    TEST_CASES = [
        (
            [
                {'dimension': 'Hardware', 'value': 'HW1'},
                {'dimension': 'Virtual_Machine', 'value': 'VM1'},
                {'dimension': 'Workload', 'value': 'WL1'},
            ],
            [(0, 2, 4)]
        ),
        (
            [
                {'dimension': 'Hardware', 'value': 'HW1'},
                {'dimension': 'Virtual_Machine', 'value': '<ANY>'},
                {'dimension': 'Workload', 'value': 'WL1'},
            ],
            [(0, 2, 4), (0, 3, 4)]
        ),
        (
            [
                {'dimension': 'Hardware', 'value': 'HW1'},
                {'dimension': 'Virtual_Machine', 'value': '<ANY>'},
                {'dimension': 'Workload', 'value': '<ANY>'},
            ],
            [(0, 2, 4), (0, 2, 5), (0, 3, 4), (0, 3, 5)]
        )
    ]
    dim_name_to_dim_vals = {
        'Hardware': ['HW1', 'HW2'],
        'Virtual_Machine': ['VM1', 'VM2'],
        'Workload': ['WL1', 'WL2']
    }
    dim_val_to_dim_val_int = {
        'HW1': 0, 'HW2': 1, 'VM1': 2, 'VM2': 3, 'WL1': 4, 'WL2': 5
    }
    for test_case in TEST_CASES:
        combination, exp_combo_list = test_case
        combo_list = _get_combination_tuples(
            combination, dim_name_to_dim_vals, dim_val_to_dim_val_int)
        assert combo_list == exp_combo_list, 'Incorrect combination list. '\
            + f'Expected: {exp_combo_list}. Actual: {combo_list}'


def test_update_target_val_dict():
    # test case: (dictionary of target value dictionaries, first dimension
    # value integer, second dimension value integer, target value dictionary,
    # expected dictionary of target value dictionaries)
    TEST_CASES = [
        (
         {
            (1, 3): {'target_val': 3, 'any_count': 1},
            (1, 4): {'target_val': 3, 'any_count': 1},
            (2, 4): {'target_val': 4, 'any_count': 0}
         }, 1, 3, {'target_val': 2, 'any_count': 0},
         {
            (1, 3): {'target_val': 2, 'any_count': 0},
            (1, 4): {'target_val': 3, 'any_count': 1},
            (2, 4): {'target_val': 4, 'any_count': 0}
         }
        ),
        (
         {
            (1, 3): {'target_val': 3, 'any_count': 1},
            (1, 4): {'target_val': 3, 'any_count': 1},
            (2, 4): {'target_val': 4, 'any_count': 0}
         }, 1, 4, {'target_val': 1, 'any_count': 1},
         {
            (1, 3): {'target_val': 3, 'any_count': 1},
            (1, 4): {'target_val': 3, 'any_count': 1},
            (2, 4): {'target_val': 4, 'any_count': 0}
         }
        ),
        (
         {
            (1, 3): {'target_val': 3, 'any_count': 1},
            (1, 4): {'target_val': 3, 'any_count': 1},
            (2, 4): {'target_val': 4, 'any_count': 0}
         }, 1, 4, {'target_val': 1, 'any_count': 2},
         {
            (1, 3): {'target_val': 3, 'any_count': 1},
            (1, 4): {'target_val': 3, 'any_count': 1},
            (2, 4): {'target_val': 4, 'any_count': 0}
         }
        )
    ]
    for test_case in TEST_CASES:
        target_val_dicts, dim_val1_int, dim_val2_int, target_dict,\
            expected_target_val_dicts = test_case
        result_target_val_dicts = _update_target_val_dict(
            target_val_dicts, (dim_val1_int, dim_val2_int), target_dict)
        assert expected_target_val_dicts == result_target_val_dicts,\
            'Dictionary of target value dictionaries was incorrectly '\
            + f'modified. Expected: {expected_target_val_dicts} '\
            + f'Actual: {result_target_val_dicts}'
