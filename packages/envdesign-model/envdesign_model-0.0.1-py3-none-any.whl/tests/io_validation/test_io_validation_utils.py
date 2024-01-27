# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import numpy as np
import pandas as pd
from tests.mock_data import (MOCK_DIMENSION_DICTS, MOCK_RELATIONSHIPS_DFS,
                             MOCK_OBJ_FUNC_DICTS)
from envdesign_model.io_validation.io_validation_utils import (
    check_df_cols, check_type, check_nan_vals, check_min_length,
    check_dict_keys, check_duplicates)
from tests.utils import check_exception


def test_check_df_cols():
    # test case: tuple(df, string type columns, numeric type columns, object
    # type columns, boolean for expecting Exception)
    PASS_CASES = [
        (MOCK_DIMENSION_DICTS[0]['df'], ['HW'], ['Score'], []),
        (MOCK_RELATIONSHIPS_DFS[0],
         ['Dimension1', 'Value1', 'Dimension2', 'Value2'], ['Score'],
         ['RelationshipMetaData']),
    ]
    FAIL_CASES = [
        (MOCK_DIMENSION_DICTS[0]['df'], ['Score'], ['HW'], [],
         # expect Exception because 'HW' column is string type and 'Score'
         # column is numeric, but lists of columns suggest the opposite
         ),
        (MOCK_RELATIONSHIPS_DFS[0],
         ['Dimension1', 'Value1', 'Dimension2', 'Value2'], ['Score'],
         ['Metadata']
         # expect Exception because 'Metadata' column not in DataFrame
         )
    ]
    for cases, exception in [(PASS_CASES, False), (FAIL_CASES, True)]:
        for test_case in cases:
            df, str_cols, num_cols, obj_cols = test_case
            try:
                check_df_cols(df, str_cols, num_cols, obj_cols)
            except Exception:
                check_exception(True, exception, test_case)
            else:
                check_exception(False, exception, test_case)


def test_check_type():
    # test case: tuple(object, expected type)
    PASS_CASES = [
        (MOCK_DIMENSION_DICTS[0], dict),
        (MOCK_RELATIONSHIPS_DFS[0], pd.DataFrame),
        (MOCK_OBJ_FUNC_DICTS[0], dict)
    ]
    FAIL_CASES = [
        (MOCK_DIMENSION_DICTS[0], pd.DataFrame
         # expect Exception because dimension dict is not a DataFrame
         ),
        (MOCK_RELATIONSHIPS_DFS[0], dict
         # expect Exception because relationships DataFrame is not a dict
         ),
        (MOCK_OBJ_FUNC_DICTS[0], pd.DataFrame
         # expect Exception because objective function dict is not a DataFrame
         )
    ]
    for cases, exception in [(PASS_CASES, False), (FAIL_CASES, True)]:
        for test_case in cases:
            object, object_type = test_case
            try:
                check_type(object, object_type)
            except Exception:
                check_exception(True, exception, test_case)
            else:
                check_exception(False, exception, test_case)


def test_check_nan_vals():
    # test case: tuple(DataFrame)
    PASS_CASES = [
        MOCK_DIMENSION_DICTS[0]['df'],
        MOCK_RELATIONSHIPS_DFS[0]
    ]
    fail_case1_df = MOCK_DIMENSION_DICTS[0]['df'].copy()
    fail_case1_df.loc[0, 'Score'] = np.nan
    fail_case1 = (fail_case1_df
                  # expect Exception because NaN value in DataFrame
                  )
    fail_case2_df = MOCK_RELATIONSHIPS_DFS[0].copy()
    fail_case2_df.loc[0, 'Score'] = np.nan
    fail_case2 = (fail_case2_df
                  # expect Exception because NaN value in DataFrame
                  )
    FAIL_CASES = [fail_case1, fail_case2]
    for cases, exception in [(PASS_CASES, False), (FAIL_CASES, True)]:
        for test_case in cases:
            df = test_case
            try:
                check_nan_vals(df)
            except Exception:
                check_exception(True, exception, test_case)
            else:
                check_exception(False, exception, test_case)


def test_check_min_length():
    # test case: tuple(object, min length)
    PASS_CASES = [
        (MOCK_DIMENSION_DICTS[0:3], 2),
        (MOCK_RELATIONSHIPS_DFS[0], 1),
        (MOCK_OBJ_FUNC_DICTS[0], 2)
    ]
    fail_case1 = ([MOCK_DIMENSION_DICTS[0]], 2
                  # expect Exception since list of dimension dicts,
                  # expected length >= 2
                  )
    fail_case2 = (pd.DataFrame(), 1
                  # expect Exception since DataFrame is empty,
                  # expected length >= 1
                  )
    obj_func_dict = dict()
    obj_func_dict['type'] = MOCK_OBJ_FUNC_DICTS[0]['type']
    fail_case3 = (obj_func_dict, 2
                  # expect Exception since objective function dict has one
                  # key, expected number of keys >= 2
                  )
    FAIL_CASES = [fail_case1, fail_case2, fail_case3]
    for cases, exception in [(PASS_CASES, False), (FAIL_CASES, True)]:
        for test_case in cases:
            object, expected_length = test_case
            try:
                check_min_length(object, expected_length)
            except Exception:
                check_exception(True, exception, test_case)
            else:
                check_exception(False, exception, test_case)


def test_check_dict_keys():
    # test case: tuple(dict, expected keys set)
    PASS_CASES = [
        (MOCK_DIMENSION_DICTS[0], {'name', 'value', 'df'}),
        (MOCK_RELATIONSHIPS_DFS[0]['RelationshipMetaData'][2][0],
         {'name', 'value'}),
        (MOCK_OBJ_FUNC_DICTS[0], {'type', 'specifics'})
    ]
    fail_case1_dict = dict()
    fail_case1_dict['name'] = MOCK_DIMENSION_DICTS[0]['name']
    fail_case1_dict['df'] = MOCK_DIMENSION_DICTS[0]['df']
    fail_case1 = (fail_case1_dict, {'name', 'value', 'df'}
                  # expect Exception because 'value' key not in dict
                  )
    fail_case2_dict = {'Many_To_One': 2}
    fail_case2 = (fail_case2_dict, {'name', 'value'}
                  # expect Exception because 'name' and 'value' keys not in
                  # dict
                  )
    fail_case3_dict = dict()
    fail_case3_dict['type'] = MOCK_OBJ_FUNC_DICTS[0]['type']
    fail_case3 = (fail_case3_dict, {'type', 'specifics'}
                  # expect Exception because 'specifics' key not in dict
                  )
    FAIL_CASES = [fail_case1, fail_case2, fail_case3]
    for cases, exception in [(PASS_CASES, False), (FAIL_CASES, True)]:
        for test_case in cases:
            dictionary, exp_keys = test_case
            try:
                check_dict_keys(dictionary, exp_keys)
            except Exception:
                check_exception(True, exception, test_case)
            else:
                check_exception(False, exception, test_case)


def test_check_duplicates():
    # test case: tuple(values)
    PASS_CASES = [
        list(MOCK_DIMENSION_DICTS[0]['df']['HW'].values),
        list(MOCK_RELATIONSHIPS_DFS[0][['Value1', 'Value2']]
             .itertuples(index=False, name=None))
    ]
    FAIL_CASES = [
        list(MOCK_DIMENSION_DICTS[0]['df']['HW'].values) + ['HW1'],
        list(MOCK_RELATIONSHIPS_DFS[0][['Value1', 'Value2']]
             .itertuples(index=False, name=None)) + [('HW1', 'WL1')]
    ]
    for cases, exception in [(PASS_CASES, False), (FAIL_CASES, True)]:
        for test_case in cases:
            values = test_case
            try:
                check_duplicates(values)
            except Exception:
                check_exception(True, exception, test_case)
            else:
                check_exception(False, exception, test_case)
