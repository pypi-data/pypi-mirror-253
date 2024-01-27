# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from copy import deepcopy
import numpy as np
import pandas as pd
from envdesign_model.io_validation.input_validation import InputValidation
from tests.utils import check_exception
from tests.mock_data import (
    MOCK_DIMENSION_DICTS, MOCK_RELATIONSHIPS_DFS, MOCK_OBJ_FUNC_DICTS,
    MOCK_SCOPE_DFS)
from functools import reduce


MOCK_DIM_DICTS1 = [
    {
        'name': 'HW', 'value': 'HW',
        'df': pd.DataFrame({
            'HW': ['HW1', 'HW2'],
            'Score': [1, 1]
        })
    },
    {
        'name': 'VM', 'value': 'VM',
        'df': pd.DataFrame({
            'VM': ['VM1'],
            'Score': [1]
        })
    },
    {
        'name': 'WL', 'value': 'WL',
        'df': pd.DataFrame({
            'WL': ['WL1', 'WL2'],
            'Score': [1, 1]
        })
    }
]
MOCK_DIM_DICTS2 = [
    {
        'name': 'HW', 'value': 'HW',
        'df': pd.DataFrame({
            'HW': ['HW1'],
            'Score': [1]
        })
    },
    {
        'name': 'VM', 'value': 'VM',
        'df': pd.DataFrame({
            'VM': ['VM1'],
            'Score': [1]
        })
    },
    {
        'name': 'WL', 'value': 'WL',
        'df': pd.DataFrame({
            'WL': ['WL1', 'WL2'],
            'Score': [1, 1]
        })
    }
]
MOCK_DIM_DICTS3 = [
    {
        'name': 'HW', 'value': 'HW',
        'df': pd.DataFrame({
            'HW': ['HW1', 'HW2'],
            'Score': [1, 1]
        })
    },
    {
        'name': 'WL', 'value': 'WL',
        'df': pd.DataFrame({
            'WL': ['WL1', 'WL2'],
            'Score': [1, 1]
        })
    }
]
MOCK_REL_DF1 = pd.DataFrame({
    'Dimension1': ['HW', 'HW', 'VM', 'HW', 'HW'],
    'Value1': ['HW1', 'HW2', 'VM1', 'HW1', 'HW2'],
    'Dimension2': ['VM', 'VM', 'WL', 'WL', 'WL'],
    'Value2': ['VM1', 'VM1', '<ANY>', 'WL1', 'WL2'],
    'Score': [1, 1, 1, 1, 1],
    'RelationshipMetaData': [
        [{'name': 'One_To_Many', 'value': 2}],
        [], [], [], []
    ]
})
MOCK_REL_DF2 = pd.DataFrame({
    'Dimension1': ['HW', 'HW', 'VM', 'VM', 'HW', 'HW'],
    'Value1': ['HW1', 'HW2', 'VM1', 'VM1', 'HW1', 'HW2'],
    'Dimension2': ['VM', 'VM', 'WL', 'WL', 'WL', 'WL'],
    'Value2': ['VM1', 'VM1', 'WL1', 'WL2', 'WL1', 'WL2'],
    'Score': [1, 1, 1, 1, 1, 1],
    'RelationshipMetaData': [
        [{'name': 'One_To_Many', 'value': 2}],
        [], [], [], [], []
    ]
})


def test_validate_scope_df():
    # test case: scope dataframe, boolean for expecting Exception
    TEST_CASES = [
        (MOCK_SCOPE_DFS[0], False),
        (MOCK_SCOPE_DFS[1], False),
        (MOCK_SCOPE_DFS[2], False),
        (MOCK_SCOPE_DFS[3], False),
        (MOCK_SCOPE_DFS[4], False),
        (pd.DataFrame({
        'Property': ['Hardware', 'Hardware', 'Virtual_Machine', 'Workload'],
        'Value': ['HW1', 'HW3', 'VM1', 'WL3'],
        'Status': ['Include', 'Include', 'Exclude', 'Exclude'],
        'OtherColumn': ['X', 'X', 'X', 'X']
        }), False),
        (pd.DataFrame(), False),
        (None, False),
        (
            pd.DataFrame({
                'Property': ['X', 'Y'],
                'Value': ['A', 'B']
            }), True
            # expect Exception since Status column is missing
        ),
        (
            pd.DataFrame({
                'Property': ['X', 'Y'],
                'Value': ['A', 'B'],
                'Status': ['I', 'J']
            }), True
            # expect Exception since Status column values are invalid
        )
    ]
    for test_case in TEST_CASES:
        scope_df, exception = test_case
        input_validation = InputValidation(
            MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 10,
            MOCK_OBJ_FUNC_DICTS[0], scope_df)
        try:
            input_validation._validate_scope_df()
        except Exception:
            check_exception(True, exception, test_case)
        else:
            check_exception(False, exception, test_case)


def test_scope_dim_dicts():
    TEST_CASES = [
        # test case: tuple(dimension dicts, scope df, expected dimension dicts,
        # boolean for expecting Exception)
        (
            MOCK_DIMENSION_DICTS[0:3],
            pd.DataFrame({
                'Property': [],
                'Value': [],
                'Status': []
            }),
            [
                {
                    'name': 'Hardware',
                    'value': 'HW',
                    'df': pd.DataFrame({
                        'HW': ['HW1', 'HW2'],
                        'Score': [1, 1]
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
            False
        ),
        (
            MOCK_DIMENSION_DICTS[0:3],
            MOCK_SCOPE_DFS[0],
            [
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
                        'VM': ['VM2'],
                        'Score': [1]
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
            False
        ),
        (
            MOCK_DIMENSION_DICTS[0:3],
            pd.DataFrame({
                'Property': ['Hardware', 'Hardware', 'Virtual_Machine',
                             'Workload'],
                'Value': ['hw1', 'HW3', 'VM1', 'wl3'],
                'Status': ['Include', 'Include', 'Exclude', 'Exclude']
            }),
            [
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
                        'VM': ['VM2'],
                        'Score': [1]
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
            False
        ),
        (
            MOCK_DIMENSION_DICTS[0:3],
            pd.DataFrame({
                'Property': ['Hardware', 'Hardware', 'Virtual_Machine'],
                'Value': ['HW1', 'HW2', 'VM1'],
                'Status': ['Exclude'] * 3
            }),
            [
                {
                    'name': 'Hardware',
                    'value': 'HW',
                    'df': pd.DataFrame({
                        'HW': [],
                        'Score': []
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
                        'WL': ['WL1', 'WL2'],
                        'Score': [1, 1]
                    })
                }
            ],
            True
            # expect Exception because Hardware dimension value DataFrame is
            # empty after scoping
        )
    ]
    for test_case in TEST_CASES:
        dim_dicts, scope_df, scoped_dim_dicts, exception = test_case
        input_validation = InputValidation(
            dim_dicts, MOCK_RELATIONSHIPS_DFS[0], 300,
            MOCK_OBJ_FUNC_DICTS[0], scope_df)
        try:
            input_validation._scope_dim_dicts()
        except Exception:
            check_exception(True, exception, test_case)
        else:
            check_exception(False, exception, test_case)
        
            # check lists of dimension dictionaries are the same length
            exp_len = len(scoped_dim_dicts)
            act_len = len(input_validation.dimension_dicts)
            assert exp_len == act_len, 'Incorrect length of dimension '\
                + f'dictionaries. Expected: {exp_len}. Actual: {act_len}'

            # check that dimension dictionaries are equal
            act_dim_dicts = input_validation.dimension_dicts
            for i in range(len(scoped_dim_dicts)):
                act_dim_dict = act_dim_dicts[i]
                exp_dim_dict = scoped_dim_dicts[i]
                act_name = act_dim_dict['name']
                exp_name = exp_dim_dict['name']
                assert act_name == exp_name, 'Incorrect dimension name. '\
                    + f'Expected: {exp_name}. Actual: {act_name}'
                act_value = act_dim_dict['value']
                exp_value = exp_dim_dict['value']
                assert act_value == exp_value, 'Incorrect dimension value '\
                    + f'column. Expected: {exp_value}. Actual: {act_value}'
                act_dim_df = act_dim_dict['df']
                exp_dim_df = exp_dim_dict['df']
                assert act_dim_df.equals(exp_dim_df), 'Incorrect dimension '\
                    + f'DataFrame. Expected: {exp_dim_df}. Actual: '\
                    + f'{act_dim_df}'


def test_infer_dimension_dicts():
    # test case: tuple(given dimension dicts, given relationships DataFrame,
    # expected dimension dicts)
    PASS_CASES = [
        ([], MOCK_REL_DF2, MOCK_DIM_DICTS1),
        (None, MOCK_REL_DF2, MOCK_DIM_DICTS1),
        (None, MOCK_REL_DF2[
            ~((MOCK_REL_DF2['Dimension1'] == 'VM')
            | (MOCK_REL_DF2['Dimension2'] == 'VM'))
            ], MOCK_DIM_DICTS3),
        ([], MOCK_REL_DF2[
            ~((MOCK_REL_DF2['Dimension1'] == 'VM')
            | (MOCK_REL_DF2['Dimension2'] == 'VM'))
            ], MOCK_DIM_DICTS3)
    ]
    FAIL_CASES = [
        (None, MOCK_REL_DF1, MOCK_DIM_DICTS1
         # expect Exception because relationships DataFrame has <ANY> values
         # and dimension dicts are unspecified
         ),
        ([], MOCK_REL_DF1, MOCK_DIM_DICTS1
         # expect Exception because relationships DataFrame has <ANY> values
         # and dimension dicts are unspecified
         )
    ]
    for cases, exception in [(PASS_CASES, False), (FAIL_CASES, True)]:
        for test_case in cases:
            given_dim_dicts, given_rel_df, exp_dim_dicts = test_case
            try:
                input_validation = InputValidation(
                    given_dim_dicts, given_rel_df, 100, MOCK_OBJ_FUNC_DICTS[0])
                input_validation._infer_dimension_dicts()
                act_dim_dicts = input_validation.dimension_dicts
                assert len(act_dim_dicts) == len(exp_dim_dicts),\
                    f'Incorrect number of dimension dictionaries. Expected: '\
                    + f'{len(exp_dim_dicts)}, Actual: {len(act_dim_dicts)}'
                for i in range(len(act_dim_dicts)):
                    act_dim_dict = act_dim_dicts[i]
                    exp_dim_dict = exp_dim_dicts[i]
                    
                    act_dim_dict_keys = set(act_dim_dict.keys())\
                        .difference({'df'})
                    exp_dim_dict_keys = set(exp_dim_dict.keys())\
                        .difference({'df'})
                    assert act_dim_dict_keys == exp_dim_dict_keys,\
                        + f'Incorrect keys for dimension dictionary {i}. '\
                        + f'Expected: {exp_dim_dict_keys}, Actual: '\
                        + f'{act_dim_dict_keys}'
                    for key in exp_dim_dict_keys:
                        act_value = act_dim_dict[key]
                        exp_value = exp_dim_dict[key]
                        assert act_value == exp_value,\
                            f'Incorrect value for key {key} in dimension '\
                            + f'dictionary {i}. Expected: {exp_value}, '\
                            + f'Actual: {act_value}'

                    act_df = act_dim_dict['df']
                    exp_df = exp_dim_dict['df']                  
                    assert act_df.equals(exp_df), 'Incorrect dimension '\
                        + f'values DataFrame for dimension dictionary {i}. '\
                        + f'Expected: {exp_df}, Actual: {act_df}'
            except Exception:
                check_exception(True, exception, test_case)
            else:
                check_exception(False, exception, test_case)


def test_validate_format_relationships_df():
    # test case: relationships DataFrame
    PASS_CASES = [
        MOCK_RELATIONSHIPS_DFS[0],
        MOCK_RELATIONSHIPS_DFS[1],
        MOCK_RELATIONSHIPS_DFS[2]
    ]
    FAIL_CASES = [
        # expect Exception because there are not enough relationships
        # for a clique to be formed
        pd.DataFrame({
        'Dimension1': ['Hardware', 'Virtual_Machine', 'Virtual_Machine',
                       'Hardware', 'Virtual_Machine', 'Hardware'],
        'Value1': ['HW1', 'VM1', 'VM1', 'HW2', 'VM2', 'HW2'],
        'Dimension2': ['Workload', 'Workload', 'Hardware',
                       'Workload', 'Workload', 'Virtual_Machine'],
        'Value2': ['WL1', 'WL1', 'HW1', 'WL2', 'WL2', 'VM2'],
        'Score': [1, 1, np.nan, 1, 1, 1],
        'RelationshipMetaData': [
            [], [], [{'name': 'Many_To_One', 'value': 2}], [], [],
            [{'name': 'One_To_Many', 'value': 2}]]
    }),
        # expect Exception because relationships DataFrame is empty
        pd.DataFrame() 
    ]
    for cases, exception in [(PASS_CASES, False), (FAIL_CASES, True)]:
        for test_case in cases:
            relationships_df = test_case
            try:
                input_validation = InputValidation(
                    MOCK_DIMENSION_DICTS[0:3], relationships_df, 100,
                    MOCK_OBJ_FUNC_DICTS[0])
                input_validation._validate_format_relationships_df()
            except Exception:
                check_exception(True, exception, test_case)
            else:
                check_exception(False, exception, test_case)


def test_scope_relationships_df():
    # test case: tuple(given dimension dicts, given relationships DataFrame,
    # expected relationships DataFrame)
    TEST_CASES = [
        # filter to only HW and VM relationships
        (MOCK_DIM_DICTS1[0:2], MOCK_REL_DF1, MOCK_REL_DF1.iloc[0:2]),
        (MOCK_DIM_DICTS1[0:2], MOCK_REL_DF2, MOCK_REL_DF2.iloc[0:2]),
        # filter to only VM and WL relationships
        (MOCK_DIM_DICTS1[1:3], MOCK_REL_DF1,
         MOCK_REL_DF1.iloc[2:3].reset_index(drop=True)),
        (MOCK_DIM_DICTS1[1:3], MOCK_REL_DF2,
         MOCK_REL_DF2.iloc[2:4].reset_index(drop=True)),
        # filter to only HW and WL relationships
        ([MOCK_DIM_DICTS1[0], MOCK_DIM_DICTS1[2]], MOCK_REL_DF1,
         MOCK_REL_DF1.iloc[3:5].reset_index(drop=True)),
        ([MOCK_DIM_DICTS1[0], MOCK_DIM_DICTS1[2]], MOCK_REL_DF2,
         MOCK_REL_DF2.iloc[4:6].reset_index(drop=True)),
        # no filtering of relationships or inferring of dimension values
        (MOCK_DIM_DICTS1, MOCK_REL_DF1, MOCK_REL_DF1),
        (MOCK_DIM_DICTS1, MOCK_REL_DF2, MOCK_REL_DF2),
    ]
    for test_case in TEST_CASES:
        given_dim_dicts, given_rel_df, exp_rel_df = test_case
        input_validation = InputValidation(
            given_dim_dicts, given_rel_df, 100, MOCK_OBJ_FUNC_DICTS[0])
        input_validation._scope_relationships_df()
        act_rel_df = input_validation.relationships_df
        assert exp_rel_df.equals(act_rel_df), 'Incorrect '\
            + f'relationships DataFrame. Expected: {exp_rel_df}, '\
            + f'Actual: {act_rel_df}'


def test_validation_dimension_dicts_empty_null_vals():
    # test_case: tuple(dimension dicts, expected dimension dicts with null/
    # empty dimension values removed)
    TEST_CASES = [
        (MOCK_DIMENSION_DICTS[0:3], MOCK_DIMENSION_DICTS[0:3]),
        (MOCK_DIMENSION_DICTS[0:2], MOCK_DIMENSION_DICTS[0:2]),
        (
            MOCK_DIMENSION_DICTS[0:2] + [{
                'name': 'Workload',
                'value': 'WL',
                'df': pd.DataFrame({
                    'WL': ['WL1', 'WL2', ''],
                    'Score': [1, 1, 2]
                })
            }],
            MOCK_DIMENSION_DICTS[0:3]
         ),
        (
            MOCK_DIMENSION_DICTS[0:2] + [{
                'name': 'Workload',
                'value': 'WL',
                'df': pd.DataFrame({
                    'WL': ['WL1', 'WL2', None],
                    'Score': [1, 1, 2]
                })
            }],
            MOCK_DIMENSION_DICTS[0:3]
         )
    ]
    for test_case in TEST_CASES:
        dim_dicts, exp_dim_dicts = test_case
        input_validation = InputValidation(
            dim_dicts, MOCK_RELATIONSHIPS_DFS[0], 10,
            MOCK_OBJ_FUNC_DICTS)
        input_validation._validate_dimension_dicts()
        act_dim_dicts = input_validation.dimension_dicts
        
        # check length of dimension dictionaries
        exp_len = len(exp_dim_dicts)
        act_len = len(act_dim_dicts)
        assert exp_len == act_len, 'Incorrect length of resulting dimension '\
            + f'dictionaries. Expected: {exp_len}. Actual: {act_len}'
        
        # check dimension dictionaries
        for i in range(len(exp_dim_dicts)):
            exp_dim_dict = exp_dim_dicts[i]
            act_dim_dict = act_dim_dicts[i]
            for attr in ['name', 'value', 'df']:
                exp_val = exp_dim_dict[attr]
                act_val = act_dim_dict[attr]
                if attr == 'df':
                    equal = exp_val.equals(act_val)
                else:
                    equal = exp_val == act_val
                assert equal, f'Incorrect value for "{attr}". '\
                    + f'Expected: {exp_val}. Actual: {act_val}'


def test_validate_dimension_dicts():
    # test case: tuple(dimension dicts, relationships DataFrame, number of
    # groups, objective function)
    PASS_CASES = [
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 100,
         MOCK_OBJ_FUNC_DICTS[0]),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[1], 100,
         MOCK_OBJ_FUNC_DICTS[1])
    ]
    fail_case1 = ([MOCK_DIMENSION_DICTS[0]], MOCK_RELATIONSHIPS_DFS[0], 100,
                  MOCK_OBJ_FUNC_DICTS[0]
                  # expect Exception because number of dimension dicts is 1
                  )
    fail_case2_dim_dicts = deepcopy(MOCK_DIMENSION_DICTS[0:3])
    fail_case2_dim_dicts[0]['value'] = 'X'
    fail_case2 = (fail_case2_dim_dicts, MOCK_RELATIONSHIPS_DFS[1], 100,
                  MOCK_OBJ_FUNC_DICTS[0]
                  # expect Exception because 'X' column does not exist in
                  # dimension DataFrame
                  )
    FAIL_CASES = [fail_case1, fail_case2]
    for cases, exception in [(PASS_CASES, False), (FAIL_CASES, True)]:
        for test_case in cases:
            dim_dicts, relationships_df, num_groups, objective_function\
                = test_case
            try:
                input_validation = InputValidation(
                    dim_dicts, relationships_df, num_groups,
                    objective_function)
                input_validation._validate_dimension_dicts()
            except Exception:
                check_exception(True, exception, test_case)
            else:
                check_exception(False, exception, test_case)


def test_create_dim_mappings():
    # test case: tuple(dimension dicts, relationships DataFrame, number of
    # groups, objective function, expected dimension value to int mapping,
    # expected int to dimension value mapping, expected dimension name to
    # values mapping, expected dimension name to dimension DataFrame mapping)
    PASS_CASES = [
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 100,
         MOCK_OBJ_FUNC_DICTS[0],
         {'Hardware': {'HW1', 'HW2'}, 'Virtual_Machine': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}},
         {'Hardware': MOCK_DIMENSION_DICTS[0]['df'],
          'Virtual_Machine': MOCK_DIMENSION_DICTS[1]['df'],
          'Workload': MOCK_DIMENSION_DICTS[2]['df']}),
        (MOCK_DIMENSION_DICTS[1:3], MOCK_RELATIONSHIPS_DFS[1], 100,
         MOCK_OBJ_FUNC_DICTS[1],
         {'Virtual_Machine': {'VM1', 'VM2'}, 'Workload': {'WL1', 'WL2'}},
         {'Virtual_Machine': MOCK_DIMENSION_DICTS[1]['df'],
          'Workload': MOCK_DIMENSION_DICTS[2]['df']})
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
         MOCK_RELATIONSHIPS_DFS[0], 100, MOCK_OBJ_FUNC_DICTS[0],
         {'HW': {'HW1', 'HW2', '<ANY>'}, 'VM': {'VM1', 'VM2'}, 'WL':
          {'WL1', 'WL2'}},
         {'Hardware': fail_case1_hw_dim_dict['df'],
          'Virtual_Machine': MOCK_DIMENSION_DICTS[1]['df'],
          'Workload': MOCK_DIMENSION_DICTS[2]['df']}
         # expect Exception because <ANY> cannot be used as a dimension value
         ),
        ([fail_case2_vm_dim_dict] + MOCK_DIMENSION_DICTS[2:3],
         MOCK_RELATIONSHIPS_DFS[1], 100, MOCK_OBJ_FUNC_DICTS[1],
         {'Virtual_Machine': {'VM1', 'VM2', '<ANY>'}, 'Workload': {'WL1', 'WL2'}},
         {'Virtual_Machine': fail_case2_vm_dim_dict['df'],
          'Workload': MOCK_DIMENSION_DICTS[2]['df']}
         # expect Exception because <ANY> cannot be used as a dimension value
         )
    ]
    for cases, exception in [(PASS_CASES, False), (FAIL_CASES, True)]:
        for test_case in cases:
            (dim_dicts, relationships_df, num_groups, objective_function,
             dim_name_to_dim_values, dim_name_to_dim_df)\
                = test_case
            try:
                input_validation = InputValidation(
                    dim_dicts, relationships_df, num_groups,
                    objective_function)
                input_validation._create_dim_mappings()
                if input_validation.dim_name_to_dim_values !=\
                        dim_name_to_dim_values:
                    raise Exception(
                        'Incorrect dimension name to dimension values '
                        + f'mappings. Expected: {dim_name_to_dim_values}, '
                        + f'Actual: {input_validation.dim_name_to_dim_values}')
                if input_validation.dim_name_to_dim_df !=\
                        dim_name_to_dim_df:
                    raise Exception(
                        'Incorrect dimension name to '
                        + 'dimension DataFrame mappings. Expected: '
                        + f'{dim_name_to_dim_df}, Actual: '
                        + f'{input_validation.dim_name_to_dim_df}')
            except Exception:
                check_exception(True, exception, test_case)
            else:
                check_exception(False, exception, test_case)


def test_validate_relationships_df():
    # test case: tuple(dimension dicts, relationships DataFrame, number of
    # groups, objective function, mocked dimension name to values mapping)
    PASS_CASES = [
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 100,
         MOCK_OBJ_FUNC_DICTS[0],
         {'Hardware': {'HW1', 'HW2'}, 'Virtual_Machine': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}}),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[1], 100,
         MOCK_OBJ_FUNC_DICTS[1],
         {'Hardware': {'HW1', 'HW2'}, 'Virtual_Machine': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}}),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[2], 100,
         MOCK_OBJ_FUNC_DICTS[1],
         {'Hardware': {'HW1', 'HW2'}, 'Virtual_Machine': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}})
    ]
    FAIL_CASES = [
        (MOCK_DIMENSION_DICTS[1:3], MOCK_RELATIONSHIPS_DFS[0], 100,
         MOCK_OBJ_FUNC_DICTS[0],
         {'Virtual_Machine': {'VM1', 'VM2'}, 'Workload': {'WL1', 'WL2'}},
         # expect Exception because relationships DataFrame has relationships
         # for Hardware values, but no dimension dictionary was provided
         # for Hardware
         ),
        (MOCK_DIMENSION_DICTS[0:3], pd.DataFrame(), 100,
         MOCK_OBJ_FUNC_DICTS[1],
         {'Hardware': {'HW1', 'HW2'}, 'Virtual_Machine': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}},
         # expect Exception because relationships DataFrame is empty
         ),
        (MOCK_DIMENSION_DICTS[0:3], pd.DataFrame({
            'Dimension1': ['Hardware', 'Virtual_Machine', 'Hardware',
                           'Virtual_Machine'],
            'Value1': ['HW1', 'VM1', 'HW2', 'VM2'],
            'Dimension2': ['Workload', 'Workload', 'Workload', 'Workload'],
            'Value2': ['WL1', 'WL1', 'WL2', 'WL2'],
            'Score': [1, 1, 1, 1],
            'RelationshipMetaData': [[], [], [], []]
         }), 100, MOCK_OBJ_FUNC_DICTS[1],
         {'Hardware': {'HW1', 'HW2'}, 'Virtual_Machine': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}},
         # expect Exception because relationships DataFrame has no HW-VM
         # relationships
         )
    ]
    for cases, exception in [(PASS_CASES, False), (FAIL_CASES, True)]:
        for test_case in cases:
            (dim_dicts, relationships_df, num_groups, objective_function,
             dim_name_to_dim_values)\
                = test_case
            try:
                input_validation = InputValidation(
                    dim_dicts, relationships_df, num_groups,
                    objective_function)
                input_validation.dim_name_to_dim_values =\
                    dim_name_to_dim_values
                input_validation._validate_relationships_df()
            except Exception:
                check_exception(True, exception, test_case)
            else:
                check_exception(False, exception, test_case)


def test_validate_num_groups():
    # test case: tuple(dimension dicts, relationships DataFrame, number of
    # groups, objective function)
    PASS_CASES = [
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 100,
         MOCK_OBJ_FUNC_DICTS[0]),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[2], 100,
         MOCK_OBJ_FUNC_DICTS[1])
    ]
    FAIL_CASES = [
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 0,
         MOCK_OBJ_FUNC_DICTS[0]
         # expect Exception because number of groups is 0
         ),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[2], -100,
         MOCK_OBJ_FUNC_DICTS[1]
         # expect Exception because number of groups is -100
         )
    ]
    for cases, exception in [(PASS_CASES, False), (FAIL_CASES, True)]:
        for test_case in cases:
            dim_dicts, relationships_df, num_groups, objective_function\
                 = test_case
            try:
                input_validation = InputValidation(
                    dim_dicts, relationships_df, num_groups,
                    objective_function)
                input_validation._validate_num_groups()
            except Exception:
                check_exception(True, exception, test_case)
            else:
                check_exception(False, exception, test_case)


def test_validate_objective_function():
    # test case: tuple(dimension dicts, relationships DataFrame, number of
    # groups, objective function)
    pass_case4_obj_func = deepcopy(MOCK_OBJ_FUNC_DICTS[2])
    pass_case4_obj_func['specifics'][0]['combinations'][0]\
        ['combination'][1]['value'] = 'X'
    PASS_CASES = [
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[1], 100,
         MOCK_OBJ_FUNC_DICTS[0]),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[2], 100,
         MOCK_OBJ_FUNC_DICTS[1]),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 100,
         MOCK_OBJ_FUNC_DICTS[2]),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 100,
         pass_case4_obj_func
         ),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 100,
         MOCK_OBJ_FUNC_DICTS[4]
         )
    ]
    fail_case1_obj_func = deepcopy(MOCK_OBJ_FUNC_DICTS[0])
    fail_case1_obj_func['specifics'][0]['name'] = 'X'
    fail_case2_obj_func = deepcopy(MOCK_OBJ_FUNC_DICTS[1])
    fail_case2_obj_func['specifics'][0]['metric'] = 'X'
    fail_case3_obj_func = deepcopy(MOCK_OBJ_FUNC_DICTS[1])
    fail_case3_obj_func['specifics'] += fail_case3_obj_func['specifics']
    fail_case4_obj_func = deepcopy(MOCK_OBJ_FUNC_DICTS[2])
    fail_case4_obj_func['specifics'][0]['combinations'][0]\
        ['metric_values'] = []
    fail_case5_obj_func = deepcopy(MOCK_OBJ_FUNC_DICTS[2])
    fail_case5_obj_func['specifics'][0]['combinations'] = []
    fail_case6_obj_func = deepcopy(MOCK_OBJ_FUNC_DICTS[2])
    fail_case6_obj_func['specifics'] += fail_case6_obj_func['specifics']
    fail_case7_obj_func = deepcopy(MOCK_OBJ_FUNC_DICTS[2])
    fail_case7_obj_func['specifics'] = []
    FAIL_CASES = [
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[1], 100,
         fail_case1_obj_func
         # expect Exception because 'X' is not a valid dimension name
         ),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[2], 100,
         fail_case2_obj_func
         # expect Exception because 'X' column is not present in
         # dimension DataFrame
         ),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[2], 100,
         fail_case3_obj_func
         # expect Exception because objective function dict's specifics
         # contains duplicate dimension pairs
         ),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 100,
         fail_case4_obj_func
         # expect Exception because metric values is an empty list
         ),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 100,
         fail_case5_obj_func
         # expect Exception because combinations list is empty
         ),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 100,
         fail_case6_obj_func
         # expect Exception because specifics list has more than one element
         ),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 100,
         fail_case7_obj_func
         # expect Exception because specifics list is empty
         ),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 100,
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
         }
         # expect Exception because combination-based objective function
         # will have an empty list of combinations (after removing the 
         # combinations that do not correspond to valid dimension values)
        )
    ]
    for cases, exception in [(PASS_CASES, False), (FAIL_CASES, True)]:
        for test_case in cases:
            (dim_dicts, relationships_df, num_groups, objective_function)\
                = test_case
            try:
                input_validation = InputValidation(
                    dim_dicts, relationships_df, num_groups,
                    objective_function)
                input_validation.dim_name_to_dim_df = {
                    'Hardware': MOCK_DIMENSION_DICTS[0]['df'],
                    'Virtual_Machine': MOCK_DIMENSION_DICTS[1]['df'],
                    'Workload': MOCK_DIMENSION_DICTS[2]['df']}
                input_validation.dim_name_to_dim_values = {
                    'Hardware': {'HW1', 'HW2'}, 
                    'Virtual_Machine': {'VM1', 'VM2'},
                    'Workload': {'WL1', 'WL2'}}
                input_validation._validate_objective_function()

                # if objective function is combination based, check that
                # remaining combinations are only between valid dimension
                # values
                valid_dim_vals = set(reduce(
                    lambda s1, s2: set(s1).union(set(s2)),
                    input_validation.dim_name_to_dim_values.values(),
                    set()))
                valid_dim_vals.add('<ANY>')
                if input_validation.objective_function['type'] ==\
                        'combination':
                    specs = input_validation.objective_function['specifics']
                    for spec in specs:
                        combos = spec['combinations']
                        assert len(combos) != 0, 'Combination based '\
                            + 'objective function specifics contains an '\
                            + 'empty list of combinations'
                        for combo in combos:
                            vals = set(map(lambda d: d['value'],
                                           combo['combination']))
                            invalid_vals = vals.difference(valid_dim_vals)
                            assert len(invalid_vals) == 0, 'Combination '\
                                + f'{combo["combination"]} has invalid '\
                                + f'dimension values: {invalid_vals}'
            except Exception:
                check_exception(True, exception, test_case)
            else:
                check_exception(False, exception, test_case)


def test_deduplicate_dim_vals():
    MOCK_DIM_DICTS_W_DUPS = [
        {
            'name': 'Hardware',
            'value': 'HW',
            'df': pd.DataFrame({
                'HW': ['HW1', 'HW2', 'HW1'],
                'Score': [2, 1, 1],
                'OtherValue': [3, 1, 2]
            })
        },
        {
            'name': 'Virtual_Machine',
            'value': 'VM',
            'df': pd.DataFrame({
                'VM': ['VM1', 'VM2', 'VM2'],
                'Score': [1, 1, 2],
                'OtherValue': [2, 2, 1]
            })
        },
        {
            'name': 'Workload',
            'value': 'WL',
            'df': pd.DataFrame({
                'WL': ['WL1', 'WL2', 'WL1'],
                'Score': [1, 1, 0],
                'OtherValue': [2, 0, 4]
            })
        }
    ]
    MOCK_DIM_DICTS_W_DUPS_NULLS = [
        {
            'name': 'Hardware',
            'value': 'HW',
            'df': pd.DataFrame({
                'HW': ['HW1', 'HW2', 'HW1'],
                'Score': [2, None, 1],
                'OtherValue': [3, 1, 2]
            })
        },
        {
            'name': 'Virtual_Machine',
            'value': 'VM',
            'df': pd.DataFrame({
                'VM': ['VM1', 'VM2', 'VM2'],
                'Score': [1, 1, ''],
                'OtherValue': [2, 2, 1]
            })
        },
        {
            'name': 'Workload',
            'value': 'WL',
            'df': pd.DataFrame({
                'WL': ['WL1', 'WL2', 'WL1'],
                'Score': [1, 1, 0],
                'OtherValue': [2, 0, 4]
            })
        }
    ]
    TEST_CASES = [
        # test case: (dimension dicts, objective function, expected
        # deduplicated dimension dicts)
        (MOCK_DIMENSION_DICTS, MOCK_OBJ_FUNC_DICTS[0], MOCK_DIMENSION_DICTS),
        (MOCK_DIMENSION_DICTS, MOCK_OBJ_FUNC_DICTS[1], MOCK_DIMENSION_DICTS),
        (MOCK_DIMENSION_DICTS, MOCK_OBJ_FUNC_DICTS[2], MOCK_DIMENSION_DICTS),
        (MOCK_DIM_DICTS_W_DUPS, MOCK_OBJ_FUNC_DICTS[0],
         [
            {
                'name': 'Hardware',
                'value': 'HW',
                'df': pd.DataFrame({
                    'HW': ['HW1', 'HW2'],
                    'Score': [2, 1],
                    'OtherValue': [3, 1]
                })
            },
            {
                'name': 'Virtual_Machine',
                'value': 'VM',
                'df': pd.DataFrame({
                    'VM': ['VM1', 'VM2'],
                    'Score': [1, 2],
                    'OtherValue': [2, 1]
                })
            },
            {
                'name': 'Workload',
                'value': 'WL',
                'df': pd.DataFrame({
                    'WL': ['WL1', 'WL2'],
                    'Score': [1, 1],
                    'OtherValue': [2, 0]
                })
            }
         ]),
        (MOCK_DIM_DICTS_W_DUPS, MOCK_OBJ_FUNC_DICTS[1],
         [
            {
                'name': 'Hardware',
                'value': 'HW',
                'df': pd.DataFrame({
                    'HW': ['HW1', 'HW2'],
                    'Score': [2, 1],
                    'OtherValue': [3, 1]
                })
            },
            {
                'name': 'Virtual_Machine',
                'value': 'VM',
                'df': pd.DataFrame({
                    'VM': ['VM1', 'VM2'],
                    'Score': [1, 1],
                    'OtherValue': [2, 2]
                })
            },
            {
                'name': 'Workload',
                'value': 'WL',
                'df': pd.DataFrame({
                    'WL': ['WL1', 'WL2'],
                    'Score': [1, 1],
                    'OtherValue': [2, 0]
                })
            }
         ]),
        (MOCK_DIM_DICTS_W_DUPS, 
         {
            'type': 'dimension',
            'specifics': [
                {
                    'name': 'Hardware',
                    'objective_function': 'mse',
                    'metric': 'Score',
                    'weight': 0.2
                },
                {
                    'name': 'Virtual_Machine',
                    'objective_function': 'mse',
                    'metric': 'OtherValue',
                    'weight': 0.4
                },
                {
                    'name': 'Workload',
                    'objective_function': 'mse',
                    'metric': 'Score',
                    'weight': 0.4
                }
            ]
         },
         [
            {
                'name': 'Hardware',
                'value': 'HW',
                'df': pd.DataFrame({
                    'HW': ['HW1', 'HW2'],
                    'Score': [2, 1],
                    'OtherValue': [3, 1]
                })
            },
            {
                'name': 'Virtual_Machine',
                'value': 'VM',
                'df': pd.DataFrame({
                    'VM': ['VM1', 'VM2'],
                    'Score': [1, 1],
                    'OtherValue': [2, 2]
                })
            },
            {
                'name': 'Workload',
                'value': 'WL',
                'df': pd.DataFrame({
                    'WL': ['WL1', 'WL2'],
                    'Score': [1, 1],
                    'OtherValue': [2, 0]
                })
            }
         ]),
        (MOCK_DIM_DICTS_W_DUPS_NULLS, MOCK_OBJ_FUNC_DICTS[0],
         [
            {
                'name': 'Hardware',
                'value': 'HW',
                'df': pd.DataFrame({
                    'HW': ['HW1', 'HW2'],
                    'Score': [2, 0],
                    'OtherValue': [3, 1]
                })
            },
            {
                'name': 'Virtual_Machine',
                'value': 'VM',
                'df': pd.DataFrame({
                    'VM': ['VM1', 'VM2'],
                    'Score': [1, 1],
                    'OtherValue': [2, 2]
                })
            },
            {
                'name': 'Workload',
                'value': 'WL',
                'df': pd.DataFrame({
                    'WL': ['WL1', 'WL2'],
                    'Score': [1, 1],
                    'OtherValue': [2, 0]
                })
            }
         ])
    ]
    for test_case in TEST_CASES:
        dim_dicts, obj_func_dict, exp_dim_dicts = test_case
        input_validation = InputValidation(
            dim_dicts, MOCK_RELATIONSHIPS_DFS[0], 10, obj_func_dict)
        input_validation._deduplicate_dim_vals()
        act_dim_dicts = input_validation.dimension_dicts
        assert len(exp_dim_dicts) == len(act_dim_dicts), 'Incorrect length '\
            + 'of deduplicated dimension dictionaries list. Expected: '\
            + f'{len(exp_dim_dicts)}. Actual: {len(act_dim_dicts)}'
        for i in range(len(exp_dim_dicts)):
            exp_dim_dict = exp_dim_dicts[i]
            act_dim_dict = act_dim_dicts[i]
            assert exp_dim_dict['name'] == act_dim_dict['name'], 'Incorrect '\
                + f'"name" attribute for dimension dictionary at index {i}. '\
                + f'Expected: {exp_dim_dict["name"]}. Actual: '\
                + f'{act_dim_dict["name"]}'
            assert exp_dim_dict['value'] == act_dim_dict['value'], 'Incorrect'\
                + f' "value" attribute for dimension dictionary at index {i}.'\
                + f' Expected: {exp_dim_dict["name"]}. Actual: '\
                + f'{act_dim_dict["name"]}'
            # the equals method will return False for equal values if columns
            # are different dtypes, converting numeric columns to float64
            # before checking for equality
            cols = {'Score', 'OtherValue'}
            cols.intersection_update(set(exp_dim_dict['df'].columns))
            cols.intersection_update(set(act_dim_dict['df'].columns))
            for col in cols:
                exp_dim_dict['df'][col] = exp_dim_dict['df'][col].astype(
                    'float64')
                act_dim_dict['df'][col] = act_dim_dict['df'][col].astype(
                    'float64')
            assert exp_dim_dict['df'].equals(act_dim_dict['df']), 'Incorrect'\
                + f' "df" attribute for dimension dictionary at index {i}. '\
                + f'Expected: {exp_dim_dict["df"]}. Actual: '\
                + f'{act_dim_dict["df"]}'
