# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from pandas.api.types import is_string_dtype, is_numeric_dtype, is_object_dtype


def check_min_length(object, min_length):
    if len(object) < min_length:
        raise Exception(f'Object is of length {len(object)}, expected length '
                        + f'to be at least {min_length}')


def check_nan_vals(df):
    for column in df.columns:
        if df[column].isna().any():
            raise Exception(f'DataFrame has NaNs in column {column}')


def check_type(object, object_type):
    if type(object) is not object_type:
        raise Exception(f'Invalid type of object. Expected: {object_type}, '
                        + f'Actual: {type(object)})')


def check_df_cols(df, string_type_cols=[], numeric_type_cols=[],
                  object_type_cols=[]):
    columns = set(df.columns)
    column_names = string_type_cols + numeric_type_cols + object_type_cols

    # check column names
    for column in column_names:
        if column not in columns:
            raise Exception(f'Column {column} not present in DataFrame')

    # check column types
    for col in string_type_cols:
        if not is_string_dtype(df[col]):
            raise Exception(f'Invalid dtype for column {col} of input '
                            + 'DataFrame. Expected: string dtype, Actual: '
                            + f'{df[col].dtype}')
    for col in numeric_type_cols:
        if not is_numeric_dtype(df[col]):
            raise Exception(f'Invalid dtype for column {col} of input '
                            + 'DataFrame. Expected: numeric dtype, Actual:'
                            + f' {df[col].dtype}')
    for col in object_type_cols:
        if not is_object_dtype(df[col]):
            raise Exception(f'Invalid dtype for column {col} of input '
                            + 'DataFrame. Expected: object dtype, Actual:'
                            + f' {df[col].dtype}')


def check_dict_keys(dict, expected_keys):
    for key in expected_keys:
        if key not in dict.keys():
            raise Exception(f'Expected key {key} not in dictionary')


def check_duplicates(values):
    if len(set(values)) != len(values):
        raise Exception(f'Duplicate values present in {values}')
