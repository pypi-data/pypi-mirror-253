# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import pandas as pd
from envdesign_model.optimization.optimization_strategies\
    .optimization_strategy_utils import get_schedules_from_cliques,\
        process_cost
from envdesign_model.optimization.objective_functions.mean_squared_error\
    import DimensionMSE, RelationshipMSE, CombinationMSE
from tests.mock_data import MOCK_DIMENSION_DICTS


# classes for mocking OptParams
class MockInputValidation:
    def __init__(self, dimension_dicts):
        self.dimension_dicts = dimension_dicts
class MockOptParams:
    def __init__(self, dim_int_to_dim_name, dim_val_int_to_dim_val,
                 objective_functions):
        self.input_validation = MockInputValidation(
            MOCK_DIMENSION_DICTS[0:3])
        self.dim_int_to_dim_name = dim_int_to_dim_name
        self.dim_val_int_to_dim_val = dim_val_int_to_dim_val
        self.objective_functions = objective_functions


def test_get_schedules_from_cliques():
    # test case: (list of cliques, DataFrame of expected schedules
    # (only dimension value columns))
    TEST_CASES = [
        ([(0, 2, 4), (1, 3, 5), (0, 2, 5)],
         pd.DataFrame({
             'Hardware': ['HW1', 'HW2', 'HW1'],
             'Virtual_Machine': ['VM1', 'VM2', 'VM1'],
             'Workload': ['WL1', 'WL2', 'WL2']
         })),
        ([(0, 3, 4), (1, 2, 5), (0, 2, 5)],
         pd.DataFrame({
             'Hardware': ['HW1', 'HW2', 'HW1'],
             'Virtual_Machine': ['VM2', 'VM1', 'VM1'],
             'Workload': ['WL1', 'WL2', 'WL2']
         })),
    ]
    for test_case in TEST_CASES:
        sol_cliques, expected_scheds_df = test_case
        dim_int_to_dim_name = {
            0: 'Hardware', 1: 'Virtual_Machine', 2: 'Workload'}
        dim_val_int_to_dim_val = {
            0: 'HW1', 1: 'HW2', 2: 'VM1', 3: 'VM2', 4: 'WL1', 5: 'WL2'}
        opt_params = MockOptParams(dim_int_to_dim_name, dim_val_int_to_dim_val,
                                   None)
        scheds_df = get_schedules_from_cliques(opt_params, sol_cliques)
        dim_val_cols = list(dim_int_to_dim_name.values())
        assert scheds_df[dim_val_cols].equals(
            expected_scheds_df[dim_val_cols]),\
            'Incorrect dimension values in schedules obtained from cliques. '\
            + f'Expected: {scheds_df[dim_val_cols]}. Actual: '\
            + f'{expected_scheds_df[dim_val_cols]}'


def test_process_cost():
    # test case: (cost tuple, objective function, expected processed
    # cost tuple)
    TEST_CASES = [
        ((0, 2, {0: 0, 1: 0, 2: 0}),
         {
            0: DimensionMSE({0: 1, 1: 1, 2: 1}),
            1: DimensionMSE({3: 2, 4: 1}),
            2: DimensionMSE({5: 1, 6: 1, 7: 1})
         },
         (0, 2, {'Hardware': 0, 'Virtual_Machine': 0, 'Workload': 0})),
        ((0, 3, {(0, 1): 0, (1, 2): 0, (0, 2): 0}),
         {
            (0, 1): RelationshipMSE({(0, 3): 1, (1, 3): 1, (0, 4): 1}),
            (1, 2): RelationshipMSE({(3, 5): 1, (3, 6): 1, (4, 7): 1}),
            (0, 2): RelationshipMSE({(0, 5): 1, (1, 6): 1, (2, 7): 1}),
         },
         (0, 3, {('Hardware', 'Virtual_Machine'): 0,
                 ('Virtual_Machine', 'Workload'): 0,
                 ('Hardware', 'Workload'): 0})),
        ((0, 2, 0),
         CombinationMSE({(0, 3, 5): 1, (1, 3, 6): 1, (2, 4, 7): 1}),
         (0, 2, 0))
    ]
    for test_case in TEST_CASES:
        cost, obj_funcs, exp_cost = test_case
        dim_int_to_dim_name = {
            0: 'Hardware', 1: 'Virtual_Machine', 2: 'Workload'}
        opt_params = MockOptParams(
            dim_int_to_dim_name, None, obj_funcs)
        processed_cost = process_cost(opt_params, cost)
        assert processed_cost == exp_cost, 'Incorrect processed cost. '\
            + f'Expected: {exp_cost}. Actual: {processed_cost}'
