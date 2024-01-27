# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from tests.mock_data import (MOCK_DIMENSION_DICTS, MOCK_RELATIONSHIPS_DFS,
                             MOCK_SCHEDULES, MOCK_SCOPE_DFS,\
                             MOCK_COVERAGE_REPORTS)
from envdesign_model.io_validation.output_validation import OutputValidation
from tests.utils import check_exception
from copy import deepcopy
import pandas as pd


def test_dim_names_and_values():
    # test case: tuple(schedules DataFrame, dimension dicts, relationships
    # DataFrame, number of groups, dimension names, dimension values,
    # dimension name to dimension values mapping, relationship metadata info)
    test_case2_sched = MOCK_SCHEDULES[0].copy()
    cols = set(test_case2_sched.columns).difference(
        {'Hardware', 'Hardware_Id'})
    test_case2_sched = test_case2_sched[list(cols)]
    test_case2_relationships_df = MOCK_RELATIONSHIPS_DFS[0].copy()
    test_case2_relationships_df = test_case2_relationships_df[
        ~(test_case2_relationships_df['Dimension1'] == 'Hardware')
        & ~(test_case2_relationships_df['Dimension2'] == 'Hardware')
    ]
    TEST_CASES = [
        (MOCK_SCHEDULES[0], MOCK_DIMENSION_DICTS[0:3],
         MOCK_RELATIONSHIPS_DFS[1], 2,
         ['Hardware', 'Virtual_Machine', 'Workload'],
         {'HW1', 'HW2', 'VM1', 'VM2', 'WL1', 'WL2'},
         {'Hardware': {'HW1', 'HW2'}, 'Virtual_Machine': {'VM1', 'VM2'},
          'Workload': {'WL1', 'WL2'}},
         {
            ('Hardware', 'HW1', 'Virtual_Machine', 'VM1'): {'One_To_Many': 2},
            ('Virtual_Machine', 'VM2', 'Hardware', 'HW2'): {'Many_To_One': 2}
         }),
        (test_case2_sched, MOCK_DIMENSION_DICTS[1:3],
         test_case2_relationships_df, 2,
         ['Virtual_Machine', 'Workload'], {'VM1', 'VM2', 'WL1', 'WL2'},
         {'Virtual_Machine': {'VM1', 'VM2'}, 'Workload': {'WL1', 'WL2'}},
         dict())
    ]
    for test_case in TEST_CASES:
        (schedules, dim_dicts, relationships_df, num_groups,
         dim_names, dim_values, dim_name_to_dim_values, rel_metadata_info) =\
            test_case
        output_validation = OutputValidation(
            schedules, dim_dicts, relationships_df, num_groups,
            MOCK_COVERAGE_REPORTS[0], rel_metadata_info)
        assert output_validation.dim_names == dim_names, 'Incorrect list '\
            + f'of dimension names. Expected: {dim_names}, Actual: '\
            + f'{output_validation.dim_names}'
        assert output_validation.dim_values == dim_values, 'Incorrect set '\
            + f'of dimension values. Expected: {dim_values}, Actual: '\
            + f'{output_validation.dim_values}'
        assert output_validation.dim_name_to_dim_values ==\
            dim_name_to_dim_values, 'Incorrect mapping of dimension names to '\
            + f'of dimension values. Expected: {dim_name_to_dim_values}, '\
            + f'Actual: {output_validation.dim_values}'


def test_validate_format():
    # test case: tuple(schedules DataFrame, dimension dictionaries,
    # relationships DataFrame, boolean for expecting Exception)
    fail_df = deepcopy(MOCK_SCHEDULES[0])
    fail_df.drop(columns=['Group_Id'], inplace=True)
    TEST_CASES = [
        (MOCK_SCHEDULES[0], False),
        (fail_df, True
         # Exception because no Group_Id column is present in schedules
         )
    ]
    for test_case in TEST_CASES:
        sched_df, exception = test_case
        output_validation = OutputValidation(
            sched_df, MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0],
            100, MOCK_COVERAGE_REPORTS[0], {
                ('Hardware', 'HW1', 'Virtual_Machine', 'VM1'):
                {'One_To_Many': 2},
                ('Virtual_Machine', 'VM2', 'Hardware', 'HW2'):
                {'Many_To_One': 2}
            })
        try:
            output_validation._validate_format()
            check_exception(False, exception, test_case)
        except Exception:
            check_exception(True, exception, test_case)


def test_validate_group_tag():
    # test case: tuple(schedules DataFrame, boolean for expecting Exception)
    TEST_CASES = [
        (MOCK_SCHEDULES[0], False),
        (MOCK_SCHEDULES[0].drop(columns=['Group_Tag']), True)
    ]
    for test_case in TEST_CASES:
        sched_df, exception = test_case
        output_validation = OutputValidation(
            sched_df, MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0],
            100, MOCK_COVERAGE_REPORTS[0], {
                ('Hardware', 'HW1', 'Virtual_Machine', 'VM1'):
                {'One_To_Many': 2},
                ('Virtual_Machine', 'VM2', 'Hardware', 'HW2'):
                {'Many_To_One': 2}
            })
        try:
            output_validation._validate_group_tag()
            check_exception(False, exception, test_case)
        except Exception:
            check_exception(True, exception, test_case)


def test_validate_num_groups():
    # test case: tuple(schedules DataFrame, expected number of groups, boolean
    # for expecting Exception)
    TEST_CASES = [
        (MOCK_SCHEDULES[0], 3, False),
        (MOCK_SCHEDULES[0].iloc[1:3], 3, True
         # Exception because only 2 groups are present in schedules
         )
    ]
    for test_case in TEST_CASES:
        sched_df, exp_num_groups, exception = test_case
        output_validation = OutputValidation(
            sched_df, MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0],
            exp_num_groups, MOCK_COVERAGE_REPORTS[0], {
                ('Hardware', 'HW1', 'Virtual_Machine', 'VM1'):
                {'One_To_Many': 2},
                ('Virtual_Machine', 'VM2', 'Hardware', 'HW2'):
                {'Many_To_One': 2}
            })
        try:
            output_validation._validate_num_groups()
            check_exception(False, exception, test_case)
        except Exception:
            check_exception(True, exception, test_case)


def test_validate_dimension_values():
    # test case: tuple(schedules DataFrame, boolean for expecting Exception)
    TEST_CASES = [
        (MOCK_SCHEDULES[0], False),
        (MOCK_SCHEDULES[0].iloc[0:2], True
         # Exception because HW2, VM2, and WL2 are not covered in schedules
         )
    ]
    for test_case in TEST_CASES:
        sched_df, exception = test_case
        output_validation = OutputValidation(
            sched_df, MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0],
            3, MOCK_COVERAGE_REPORTS[0],  {
                ('Hardware', 'HW1', 'Virtual_Machine', 'VM1'):
                {'One_To_Many': 2},
                ('Virtual_Machine', 'VM2', 'Hardware', 'HW2'):
                {'Many_To_One': 2}
            })
        try:
            output_validation._validate_dimension_values()
            check_exception(False, exception, test_case)
        except Exception:
            check_exception(True, exception, test_case)


def test_validate_relationships():
    # test case: tuple(schedules DataFrame, boolean for expecting
    # Exception)
    fail_df = deepcopy(MOCK_SCHEDULES[0])
    fail_df['Virtual_Machine'] = ['VM1'] * len(MOCK_SCHEDULES[0])
    TEST_CASES = [
        (MOCK_SCHEDULES[0], False),
        (fail_df, True
         # Exception because VM1 and HW2/WL2 are not compatible
         )
    ]
    for test_case in TEST_CASES:
        sched_df, exception = test_case
        output_validation = OutputValidation(
            sched_df, MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], 3,
            MOCK_COVERAGE_REPORTS[0],
            {
                ('Hardware', 'HW1', 'Virtual_Machine', 'VM1'):
                {'One_To_Many': 2},
                ('Virtual_Machine', 'VM2', 'Hardware', 'HW2'):
                {'Many_To_One': 2}
            })
        try:
            output_validation._validate_relationships()
            check_exception(False, exception, test_case)
        except Exception:
            check_exception(True, exception, test_case)


def test_validate_relationship_metadata():
    # test case: tuple(schedules DataFrame, relationships DataFrame,
    # relationship metadata info, boolean for expecting Exception)
    TEST_CASES = [
        (MOCK_SCHEDULES[0], MOCK_RELATIONSHIPS_DFS[6],
         {
            ('Hardware', 'HW1', 'Virtual_Machine', 'VM1'): {'One_To_Many': 1},
            ('Virtual_Machine', 'VM2', 'Hardware', 'HW2'): {'Many_To_One': 1}
         }, False),
        (MOCK_SCHEDULES[1], MOCK_RELATIONSHIPS_DFS[0],
         {
            ('Hardware', 'HW1', 'Virtual_Machine', 'VM1'): {'One_To_Many': 2},
            ('Virtual_Machine', 'VM2', 'Hardware', 'HW2'): {'Many_To_One': 2}
         }, False),
        (MOCK_SCHEDULES[0], MOCK_RELATIONSHIPS_DFS[0],
         {
            ('Hardware', 'HW1', 'Virtual_Machine', 'VM1'): {'One_To_Many': 2},
            ('Virtual_Machine', 'VM2', 'Hardware', 'HW2'): {'Many_To_One': 2}
         }, True
         # Exception because there are not two VM1s on each HW1 and two VM2s on
         # each HW2
         ),
        (MOCK_SCHEDULES[1], MOCK_RELATIONSHIPS_DFS[6],
         {
            ('Hardware', 'HW1', 'Virtual_Machine', 'VM1'): {'One_To_Many': 1},
            ('Virtual_Machine', 'VM2', 'Hardware', 'HW2'): {'Many_To_One': 1}
         }, True
         # Exception because there is not only one VM1 on each HW1 and not only
         # one VM2 on each HW2
         )
    ]
    for test_case in TEST_CASES:
        sched_df, rel_df, rel_metadata_info, exception = test_case
        output_validation = OutputValidation(
            sched_df, MOCK_DIMENSION_DICTS[0:3], rel_df, 3,
            MOCK_COVERAGE_REPORTS[0], rel_metadata_info)
        try:
            output_validation._validate_relationship_metadata()
            check_exception(False, exception, test_case)
        except Exception:
            check_exception(True, exception, test_case)


def test_validate_scope():
    # test case: tuple(schedules, scope function, boolean for expecting
    # Exception)
    TEST_CASES = [
        (MOCK_SCHEDULES[0], None, False),
        (MOCK_SCHEDULES[1], pd.DataFrame(), False),
        (MOCK_SCHEDULES[0], pd.DataFrame({
            'Property': ['Hardware', 'Hardware', 'Virtual_Machine',
                         'Virtual_Machine', 'Workload', 'Workload'],
            'Value': ['HW1', 'HW2', 'VM1', 'VM2', 'WL1', 'WL2'],
            'Status': ['Include'] * 6
        }), False),
        (MOCK_SCHEDULES[1], pd.DataFrame({
            'Property': ['Hardware', 'Hardware', 'Virtual_Machine',
                         'Virtual_Machine', 'Workload', 'Workload'],
            'Value': ['HW1', 'HW2', 'VM1', 'VM2', 'WL1', 'WL2'],
            'Status': ['Include'] * 6
        }), False),
        (MOCK_SCHEDULES[0], MOCK_SCOPE_DFS[0], True
         # expect Exception because VM1 is in schedules but should have
         # been excluded
         ),
        (MOCK_SCHEDULES[1], MOCK_SCOPE_DFS[1], True
         # expect Exception because HW2, VM2, and WL2 are in schedules
         # but should not have been included
         ),
        (MOCK_SCHEDULES[0], pd.DataFrame({
            'Property': ['Hardware', 'Hardware', 'Virtual_Machine',
                         'Virtual_Machine', 'Workload', 'Workload'],
            'Value': ['HW3', 'HW4', 'VM3', 'VM4', 'WL3', 'WL4'],
            'Status': ['Exclude'] * 6
        }), False),
        (MOCK_SCHEDULES[0], pd.DataFrame({
            'Property': ['Hardware', 'Virtual_Machine','Workload'],
            'Value': ['HW3', 'VM3', 'WL3'],
            'Status': ['Exclude'] * 3
        }), False)
    ]
    for test_case in TEST_CASES:
        scheds_df, scope_df, exception = test_case
        output_validation = OutputValidation(
            scheds_df, MOCK_DIMENSION_DICTS[0:3], None, 3,
            MOCK_COVERAGE_REPORTS[0], None, scope_df)
        try:
            output_validation._validate_scope()
            check_exception(False, exception, test_case)
        except Exception:
            check_exception(True, exception, test_case)


def test_validate_coverage_report():
    # test case: (dimension dictionaries, coverage report, boolean for
    # expecting Exception)
    TEST_CASES = [
        (MOCK_DIMENSION_DICTS[0:3], MOCK_COVERAGE_REPORTS[0], False),
        (MOCK_DIMENSION_DICTS[0:3], {
            'Hardware': {
                'HW1': 2,
                'HW2': 1
            },
            'Virtual_Machine': {
                'VM1': 2,
                'VM2': 1
            },
            'Workload': {
                'WL1': 2,
                'WL2': 1
            }
        }, True
        # expect Exception since coverage report values for a specific
        # dimension do not sum to 1
        ),
        (MOCK_DIMENSION_DICTS[0:3], {
            'Hardware': {
                'HW1': 1,
            },
            'Virtual_Machine': {
                'VM1': 1,
            },
            'Workload': {
                'WL1': 1,
            }
        }, True
        # expect Exception since coverage report values do not cover all
        # dimension values
        ),
        (MOCK_DIMENSION_DICTS[0:3], {
            'Hardware': {
                'HW1': 2/3,
                'HW2': 1/3
            },
            'Virtual_Machine': {
                'VM1': 2/3,
                'VM2': 1/3
            }
        }, True
        # expect Exception since coverage report dimensions do not cover all
        # dimensions in dimension dictionaries
        )
    ]
    for test_case in TEST_CASES:
        dim_dicts, coverage_report, exception = test_case
        output_validation = OutputValidation(
            MOCK_SCHEDULES[0], dim_dicts, MOCK_RELATIONSHIPS_DFS[0], 3,
            coverage_report, {
                ('Hardware', 'HW1', 'Virtual_Machine', 'VM1'):
                {'One_To_Many': 2},
                ('Virtual_Machine', 'VM2', 'Hardware', 'HW2'):
                {'Many_To_One': 2}
            }, None)
        try:
            output_validation._validate_coverage_report()
            check_exception(False, exception, test_case)
        except Exception:
            check_exception(True, exception, test_case)
