# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import pandas as pd
from collections import defaultdict
from envdesign_model.output_postprocessing.output_postprocessing import\
    OutputPostProcessing
from tests.mock_data import MOCK_DIMENSION_DICTS, MOCK_RELATIONSHIPS_DFS,\
    MOCK_SCHEDULES, MOCK_COVERAGE_REPORTS


def test_convert_rel_md_type():
    # test case: relationship (dimension value 1, dimension 1, dimension value 2,
    # dimension 2), metadata type, expected relationship, expected metadata type
    TEST_CASES = [
        (('HW1', 'Hardware', 'VM1', 'Virtual_Machine'), 'One_To_Many', 
         ('HW1', 'Hardware', 'VM1', 'Virtual_Machine'), 'One_To_Many'), 
        (('VM1', 'Virtual_Machine', 'HW1', 'Hardware'), 'Many_To_One', 
         ('HW1', 'Hardware', 'VM1', 'Virtual_Machine'), 'One_To_Many'),
    ]
    for test_case in TEST_CASES:
        rel, md_type, exp_rel, exp_md_type = test_case
        output_postprocessing = OutputPostProcessing(
            MOCK_SCHEDULES[0], MOCK_DIMENSION_DICTS[0:3],
            MOCK_RELATIONSHIPS_DFS[0], 100, 'Node')
        new_rel, new_md_type = output_postprocessing._convert_rel_md_type(
            rel, md_type)
        assert new_rel == exp_rel, 'Incorrect result relationship. '\
            + f'Expected: {exp_rel}. Actual: {new_rel}'
        assert new_md_type == exp_md_type, 'Incorrect result metadata type. '\
            + f'Expected: {exp_md_type}. Actual: {new_md_type}'


def test_update_metadata():
    # test case: (prior relationship metadata, relationship tuple (dim1, val1,
    # dim2, val2), new metadata, expected updated relationship metadata)
    TEST_CASES = [
        ({
            ('Hardware', 'HW1', 'Virtual_Machine', 'VM1'): {
                'any_count': 2, 'metadata': {'One_To_Many': 2, 'X': 3},
            }
         },
         ('Virtual_Machine', 'VM1', 'Hardware', 'HW1'),
         {
            'any_count': 1, 'metadata': {'Many_To_One': 3}
         },
         {
            ('Hardware', 'HW1', 'Virtual_Machine', 'VM1'): {
                'any_count': 1, 'metadata': {'One_To_Many': 3, 'X': 3},
            }
         }
         # override metadata because of lower any_count
         # X is a random metadata type that should be present in updated
         # relationship metadata, since it is present in the new metadata
         ),
        ({
            ('Hardware', 'HW1', 'Virtual_Machine', 'VM1'): {
                'any_count': 1, 'metadata': {'One_To_Many': 2, 'X': 3},
            }
         },
         ('Virtual_Machine', 'VM1', 'Hardware', 'HW1'),
         {
            'any_count': 1, 'metadata': {'Many_To_One': 3}
         },
         {
            ('Hardware', 'HW1', 'Virtual_Machine', 'VM1'): {
                'any_count': 1, 'metadata': {'One_To_Many': 3, 'X': 3},
            }
         }
         # override metadata with max value
         # X is a random metadata type that should be present in updated
         # relationship metadata, since it is present in the new metadata
         ),
        ({
            ('Hardware', 'HW1', 'Virtual_Machine', 'VM1'): {
                'any_count': 1, 'metadata': {'One_To_Many': 2},
            }
         },
         ('Hardware', 'HW1', 'Virtual_Machine', 'VM1'),
         {
            'any_count': 1, 'metadata': {'One_To_Many': 1}
         },
         {
            ('Hardware', 'HW1', 'Virtual_Machine', 'VM1'): {
                'any_count': 1, 'metadata': {'One_To_Many': 2},
            }
         }
         # retain max value for metadata, when any_count is the same
         # X is a random metadata type that should be present in updated
         # relationship metadata, since it is present in the new metadata
         ),
        (dict(),
         ('Virtual_Machine', 'VM1', 'Hardware', 'HW1'),
         {
            'any_count': 1, 'metadata': {'Many_To_One': 3}
         },
         {
            ('Hardware', 'HW1', 'Virtual_Machine', 'VM1'): {
                'any_count': 1, 'metadata': {'One_To_Many': 3},
            }
         }
         # new metadata, for new relationship
         ),
        ({
            ('Hardware', 'HW1', 'Virtual_Machine', 'VM1'): {
                'any_count': 2, 'metadata': {'One_To_Many': 2},
            }
         },
         ('Virtual_Machine', 'VM2', 'Hardware', 'HW2'),
         {
            'any_count': 1, 'metadata': {'Many_To_One': 3}
         },
         {
            ('Hardware', 'HW1', 'Virtual_Machine', 'VM1'): {
                'any_count': 2, 'metadata': {'One_To_Many': 2},
            },
            ('Hardware', 'HW2', 'Virtual_Machine', 'VM2'): {
                'any_count': 1, 'metadata': {'One_To_Many': 3}
            }
         }
         # new metadata, for new relationship
         )
    ]
    for test_case in TEST_CASES:
        rel_metadata, new_rel, new_metadata, expected_rel_metadata = test_case
        output_postprocessing = OutputPostProcessing(
            MOCK_SCHEDULES[0], MOCK_DIMENSION_DICTS[0:3],
            MOCK_RELATIONSHIPS_DFS[0], 100, 'Node')
        output_postprocessing.rel_metadata = rel_metadata
        output_postprocessing._update_relationship_metadata(
            new_rel[0], new_rel[1], new_rel[2], new_rel[3], new_metadata)
        assert output_postprocessing.rel_metadata == expected_rel_metadata,\
            'Incorrect updated relationship metadata. Expected: '\
            + f'{expected_rel_metadata}, Actual: '\
            + f'{output_postprocessing.rel_metadata}'


def test_get_relationship_metadata_info():
    # test case: (relationships DataFrame, expected relationship metadata)
    TEST_CASES = [
        (MOCK_RELATIONSHIPS_DFS[0], {
            ('Hardware', 'HW1', 'Virtual_Machine', 'VM1'): {'One_To_Many': 2},
            ('Hardware', 'HW2', 'Virtual_Machine', 'VM2'): {'One_To_Many': 2}
        }),
        (MOCK_RELATIONSHIPS_DFS[1], {
            ('Hardware', 'HW1', 'Virtual_Machine', 'VM1'): {'One_To_Many': 2},
            ('Hardware', 'HW2', 'Virtual_Machine', 'VM2'): {'One_To_Many': 2}
        }),
        (MOCK_RELATIONSHIPS_DFS[2], {
            ('Hardware', 'HW1', 'Virtual_Machine', 'VM1'): {'One_To_Many': 2},
            ('Hardware', 'HW2', 'Virtual_Machine', 'VM1', ): {'One_To_Many': 2},
            ('Hardware', 'HW1', 'Virtual_Machine', 'VM2'): {'One_To_Many': 2},
            ('Hardware', 'HW2', 'Virtual_Machine', 'VM2'): {'One_To_Many': 2},
        }),
        (MOCK_RELATIONSHIPS_DFS[3], {
            ('Hardware', 'HW1', 'Virtual_Machine', 'VM1'): {'One_To_Many': 2},
            ('Hardware', 'HW2', 'Virtual_Machine', 'VM1'): {'One_To_Many': 4},
            ('Hardware', 'HW2', 'Virtual_Machine', 'VM2'): {'One_To_Many': 2},
        }),
        (MOCK_RELATIONSHIPS_DFS[4], {
            ('Hardware', 'HW1', 'Virtual_Machine', 'VM2'): {'One_To_Many': 3},
            ('Hardware', 'HW1', 'Virtual_Machine', 'VM1'): {'One_To_Many': 3},
            ('Hardware', 'HW2', 'Virtual_Machine', 'VM2'): {'One_To_Many': 2},
        }),
        (MOCK_RELATIONSHIPS_DFS[5], {
            ('Hardware', 'HW1', 'Virtual_Machine', 'VM2'): {'One_To_Many': 3},
            ('Hardware', 'HW1', 'Virtual_Machine', 'VM1'): {'One_To_Many': 3},
            ('Hardware', 'HW2', 'Virtual_Machine', 'VM2'): {'One_To_Many': 2},
            ('Virtual_Machine', 'VM1', 'Workload', 'WL1'): {'One_To_Many': 2},
            ('Virtual_Machine', 'VM2', 'Workload', 'WL2'): {'One_To_Many': 3},
        }),
        (MOCK_RELATIONSHIPS_DFS[7], {
            ('Hardware', 'HW1', 'Virtual_Machine', 'VM2'): {'One_To_Many': 3},
            ('Hardware', 'HW1', 'Virtual_Machine', 'VM1'): {'One_To_Many': 3},
            ('Hardware', 'HW2', 'Virtual_Machine', 'VM2'): {'One_To_Many': 2},
        }),
        (MOCK_RELATIONSHIPS_DFS[8], {
            ('Hardware', 'HW1', 'Virtual_Machine', 'VM2'): {'One_To_Many': 2},
            ('Hardware', 'HW1', 'Virtual_Machine', 'VM1'): {'One_To_Many': 4},
            ('Hardware', 'HW2', 'Virtual_Machine', 'VM2'): {'One_To_Many': 2},
        })
    ]
    for test_case in TEST_CASES:
        rel_df, expected_rel_metadata = test_case
        output_postprocessing = OutputPostProcessing(
            MOCK_SCHEDULES[0], MOCK_DIMENSION_DICTS[0:3], rel_df, 100,
            'Node')
        output_postprocessing._get_relationship_metadata_info()
        assert output_postprocessing.rel_metadata == expected_rel_metadata,\
            'Incorrect relationship metadata mappings. Expected: '\
            + f'{expected_rel_metadata}. Actual: '\
            + f'{output_postprocessing.rel_metadata}'


def test_apply_relationship_metadata():
    # test case: (dimension dictionaries, relationships DataFrame, schedules
    # DataFrame)
    TEST_CASES = [
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], MOCK_SCHEDULES[0]),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[1], MOCK_SCHEDULES[0]),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[2], MOCK_SCHEDULES[0]),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[3], MOCK_SCHEDULES[0]),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[4], MOCK_SCHEDULES[0]),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[5], MOCK_SCHEDULES[0])
    ]
    for test_case in TEST_CASES:
        dim_dicts, rel_df, sched_df = test_case
        output_postprocessing = OutputPostProcessing(sched_df, dim_dicts,
                                                     rel_df, 100, 'Node')
        output_postprocessing._get_relationship_metadata_info()
        output_postprocessing._apply_relationship_metadata(
            [output_postprocessing._apply_one_to_many])
        dim_names = list(filter(lambda c: '_Id' not in c, sched_df.columns))
        dim_pairs = []
        for i in range(len(dim_names) - 1):
            for j in range(i + 1, len(dim_names)):
                dim_pairs.append((dim_names[i], dim_names[j]))
                dim_pairs.append((dim_names[j], dim_names[i]))
        for _, row1 in sched_df.iterrows():
            for dim1, dim2 in dim_pairs:
                rel = (dim1, row1[dim1], dim2, row1[dim2])
                if rel not in output_postprocessing.rel_metadata.keys():
                    continue
                metadata = output_postprocessing.rel_metadata[rel]
                sub_scheds_df = output_postprocessing.schedules_df[
                    (output_postprocessing.schedules_df[dim1] == row1[dim1])
                    & (output_postprocessing.schedules_df[dim2] == row1[dim2])
                ]
                if 'One_To_Many' in metadata.keys():
                    one_to_many_count = metadata['One_To_Many']
                    id_map = defaultdict(set)
                    for _, row2 in sub_scheds_df.iterrows():
                        id_map[row2[f'{dim1}_Id']].add(row2[f'{dim2}_Id'])
                    for dim1_id in id_map.keys():
                        assert len(id_map[dim1_id]) == one_to_many_count,\
                            f'Incorrect number of {dim2}_Id values associated'\
                            + f' with {dim1}_Id {dim1_id}: {id_map[dim1_id]}.'\
                            + f' Expected: {one_to_many_count}, Actual: '\
                            + f'{len(id_map[dim1_id])}'


def test_apply_one_to_many():
    # test case: (dimension name 1, dimension name 2, schedule rows DataFrame,
    # metadata)
    TEST_CASES = [
        (
            'Hardware', 'Virtual_Machine',
            pd.DataFrame({
                'Hardware': ['HW1'],
                'Hardware_Id': ['1'],
                'Virtual_Machine': ['VM1'],
                'Virtual_Machine_Id': ['2'],
                'Workload': ['WL1'],
                'Workload_Id': ['3']
            }),
            {
                'One_To_Many': 2
            }
        ),
        (
            'Hardware', 'Virtual_Machine',
            pd.DataFrame({
                'Hardware': ['HW1', 'HW2'],
                'Hardware_Id': ['1', '2'],
                'Virtual_Machine': ['VM1', 'VM2'],
                'Virtual_Machine_Id': ['3', '4'],
                'Workload': ['WL1', 'WL2'],
                'Workload_Id': ['5', '6']
            }),
            {
                'One_To_Many': 2
            }
        )
    ]
    for test_case in TEST_CASES:
        dim1, dim2, sched_rows_df, metadata = test_case
        output_postprocessing = OutputPostProcessing(
            MOCK_SCHEDULES[0], MOCK_DIMENSION_DICTS[0:3],
            MOCK_RELATIONSHIPS_DFS[0], 100, 'Node')
        output_postprocessing._get_relationship_metadata_info()
        one_to_many_count = metadata['One_To_Many']
        new_rows_df = output_postprocessing._apply_one_to_many(
            dim1, dim2, sched_rows_df, metadata)
        # determine which id columns should have updated values
        for idx in range(len(output_postprocessing.dim_names)):
            if output_postprocessing.dim_names[idx] == dim1:
                dim1_idx = idx
        updated_id_cols = set(
            map(lambda c: c + '_Id',
                output_postprocessing.dim_names[dim1_idx + 1:]))
        for idx, row in sched_rows_df.iterrows():
            new_row = new_rows_df.iloc[idx * one_to_many_count]
            assert (row == new_row).all(),\
                'Original schedule row was not preserved in new schedules.'\
                + f'Original schedule row: {row}, new schedule row: {new_row}'
            for i in range(1, one_to_many_count):
                new_row = new_rows_df.iloc[idx * one_to_many_count + i]
                for col in new_row.index:
                    if col in updated_id_cols:
                        assert row[col] != new_row[col],\
                            f'{col} values of original schedule row and new '\
                            + 'schedule row match. Original schedule value: '\
                            + f'{row[col]}, new schedule value: {new_row[col]}'
                    else:
                        assert row[col] == new_row[col],\
                            f'{col} values of original schedule row and new '\
                            + 'schedule row do not match. Original schedule '\
                            + f'value: {row[col]}, new schedule value: '\
                            + f'{new_row[col]}'


def test_add_group_tag_col():
    # test case: (dimension dictionaries, relationships DataFrame, schedules
    # DataFrame)
    TEST_CASES = [
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[0], MOCK_SCHEDULES[0]),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[1], MOCK_SCHEDULES[0]),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[2], MOCK_SCHEDULES[0]),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[3], MOCK_SCHEDULES[0]),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[4], MOCK_SCHEDULES[0]),
        (MOCK_DIMENSION_DICTS[0:3], MOCK_RELATIONSHIPS_DFS[5], MOCK_SCHEDULES[0])
    ]
    GROUP_TAG = 'Node'
    for test_case in TEST_CASES:
        dim_dicts, rel_df, scheds_df = test_case
        scheds_df.drop(columns=['Group_Tag'], inplace=True)
        output_postprocessing = OutputPostProcessing(
            scheds_df, dim_dicts, rel_df, 100, GROUP_TAG)
        output_postprocessing._add_group_tag_col()
        cols = list(output_postprocessing.schedules_df.columns)
        assert cols[1] == 'Group_Tag', 'Group_Tag not present as second column '\
            + 'in schedules DataFrame'
        assert set(output_postprocessing.schedules_df['Group_Tag']) ==\
            {'Node'}, f'Group_Tag column must contain only one value, '\
            + f'"{GROUP_TAG}"'


def test_generate_coverage_report():
    # test case: (dimension dictionaries, number of groups, schedules
    # DataFrame, expected coverage report)
    TEST_CASES = [
        (MOCK_DIMENSION_DICTS[0:3], 3, MOCK_SCHEDULES[0],
         MOCK_COVERAGE_REPORTS[0]),
        (MOCK_DIMENSION_DICTS[0:3], 3, MOCK_SCHEDULES[1],
         MOCK_COVERAGE_REPORTS[0])
    ]
    for test_case in TEST_CASES:
        dim_dicts, num_groups, scheds, expected_coverage_report = test_case
        output_postprocessing = OutputPostProcessing(
            scheds, dim_dicts, MOCK_RELATIONSHIPS_DFS[0], num_groups,
            group_tag='Node')
        output_postprocessing._generate_coverage_report()
        actual_coverage_report = output_postprocessing.coverage_report
        assert actual_coverage_report.equals(expected_coverage_report),\
            'Incorrect coverage report generated. Expected: '\
            + f'{expected_coverage_report}, Actual: '\
            + f'{actual_coverage_report}'
