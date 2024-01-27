# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import pandas as pd
from collections import defaultdict
from envdesign_model.io_validation.io_validation_utils import (
    check_type, check_nan_vals, check_df_cols)


class OutputValidation:
    def __init__(self, schedules_df, dimension_dicts, relationships_df,
                 num_groups, coverage_report, rel_metadata_info,
                 scope_df=None):
        self.dimension_dicts = dimension_dicts
        self.relationships_df = relationships_df
        self.num_groups = num_groups
        self.schedules_df = schedules_df
        self.rel_metadata_info = rel_metadata_info
        self.coverage_report = coverage_report
        self.scope_df = scope_df
        self.dim_name_to_dim_values = dict()
        self.dim_names = list()
        self.dim_values = set()
        for dim_dict in dimension_dicts:
            dim_name = dim_dict['name']
            dim_values = set(dim_dict['df'][dim_dict['value']].values)
            self.dim_names.append(dim_name)
            self.dim_values = self.dim_values.union(dim_values)
            self.dim_name_to_dim_values[dim_name] = dim_values

    def process(self):
        self._validate_format()
        self._validate_group_tag()
        self._validate_num_groups()
        self._validate_dimension_values()
        self._validate_relationships()
        self._validate_relationship_metadata()
        self._validate_scope()
        self._validate_coverage_report()
    
    def _validate_format(self):
        # check format
        check_type(self.schedules_df, pd.DataFrame)
        check_nan_vals(self.schedules_df)
        col_names = ['Group_Id', 'Group_Tag']
        for col_name in list(map(lambda d: d['name'], self.dimension_dicts)):
            col_names.append(col_name)
            col_names.append(col_name + '_Id')
        check_df_cols(self.schedules_df, string_type_cols=col_names)
    
    def _validate_group_tag(self):
        # check value of Group_Tag column
        if set(self.schedules_df['Group_Tag']) != {'Node'}:
            raise Exception('Group_Tag column must contain only one value, '
                            + '"Node"')
    
    def _validate_num_groups(self):
        # check number of groups
        group_ids = self.schedules_df['Group_Id'].unique()
        if len(group_ids) != self.num_groups:
            raise Exception('Incorrect number of groups. Expected: '
                            + f'{self.num_groups} Actual: {len(group_ids)}')

    def _validate_dimension_values(self):
        # check for coverage of dimension values
        filtered_columns = filter(lambda c: ('_Id' not in c) and\
                                  ('Group' not in c),
                                  self.schedules_df.columns)
        sched_dim_values = set()
        for col in filtered_columns:
            sched_dim_values = sched_dim_values.union(
                set(self.schedules_df[col].values))
        diff_values1 = self.dim_values.difference(sched_dim_values)
        if len(diff_values1) > 0:
            raise Exception('Dimension values not covered in schedule: '
                            + f'{diff_values1}')
        diff_values2 = sched_dim_values.difference(self.dim_values)
        if len(diff_values2) > 0:
            raise Exception('Dimension values present in schedule but not in '
                            + f'dimension dicts: {diff_values2}')

    def _validate_relationships(self):
        # check that each relationship in the schedule is present in the
        # relationships DataFrame
        dim_val_relationships = defaultdict(set)
        for _, relationship in self.relationships_df.iterrows():
            dimension1 = relationship['Dimension1']
            dimension2 = relationship['Dimension2']
            value1 = relationship['Value1']
            value2 = relationship['Value2']
            if value1 == '<ANY>' and value2 == '<ANY>':
                for dim1_value in self.dim_name_to_dim_values[dimension1]:
                    for dim2_value in self.dim_name_to_dim_values[dimension2]:
                        dim_val_relationships[dim1_value].add(dim2_value)
                        dim_val_relationships[dim2_value].add(dim1_value)
            elif value1 == '<ANY>' and value2 != '<ANY>':
                for dim1_value in self.dim_name_to_dim_values[dimension1]:
                    dim_val_relationships[dim1_value].add(value2)
                    dim_val_relationships[value2].add(dim1_value)
            elif value1 != '<ANY>' and value2 == '<ANY>':
                for dim2_value in self.dim_name_to_dim_values[dimension2]:
                    dim_val_relationships[value1].add(dim2_value)
                    dim_val_relationships[dim2_value].add(value1)
            else:
                dim_val_relationships[value1].add(value2)
                dim_val_relationships[value2].add(value1)
        for _, sched in self.schedules_df.iterrows():
            for i in range(len(self.dim_names) - 1):
                dim1_name = self.dim_names[i]
                dim1_value = sched[dim1_name]
                for j in range(i + 1, len(self.dim_names)):
                    dim2_name = self.dim_names[j]
                    dim2_value = sched[dim2_name]
                    if dim2_value not in dim_val_relationships[dim1_value]:
                        raise Exception('Relationship between dimension values'
                                        + f' {dim1_value} and {dim2_value} '
                                        + 'present in schedules but not '
                                        + 'specified in relationships '
                                        + 'DataFrame')
    
    def _validate_relationship_metadata(self):
        def _check_id_mappings(scheds_df, dim1, dim2, count):
            id_map = defaultdict(set)
            for _, row in scheds_df.iterrows():
                id_map[row[f'{dim1}_Id']].add(row[f'{dim2}_Id'])
            for dim1_id in id_map.keys():
                actual_count = len(id_map[dim1_id])
                if actual_count != count:
                    raise Exception(
                        f'{dim1}_Id value {dim1_id} expected to correspond'\
                        + f' to {count} {dim2}_Id values, actually '\
                        + f'corresponds to {actual_count} {dim2}_Id values')
                
        def _validate_metadata(scheds_df, rel_metadata, dim1, dim2):
            for metadata in rel_metadata:
                md_type = metadata['name']
                md_value = metadata['value']
                if md_type == 'One_To_Many':
                    _check_id_mappings(scheds_df, dim1, dim2, md_value)
                elif md_value == 'Many_To_One':
                    _check_id_mappings(scheds_df, dim2, dim1, md_value)
        
        # check that all relationship metadata values are adhered to
        for relationship, metadata in self.rel_metadata_info.items():
            dim1, val1, dim2, val2 = relationship
            sub_sched_df = self.schedules_df[
                (self.schedules_df[dim1] == val1)
                & (self.schedules_df[dim2] == val2)
            ]
            rel_metadata = []
            for metadata_type, metadata_value in metadata.items():
                rel_metadata.append(
                    {'name': metadata_type, 'value': metadata_value})
            _validate_metadata(sub_sched_df, rel_metadata, dim1, dim2)

    def _validate_scope(self):
        if self.scope_df is None or len(self.scope_df) == 0:
            return
        
        # check that the dimension values in the schedules adhere to
        # the scope data
        dim_names = set(map(lambda d: d['name'], self.dimension_dicts))
        for dim_name in dim_names:
            sched_dim_vals = set(self.schedules_df[dim_name])
            include_vals = set(self.scope_df[
                (self.scope_df['Property'] == dim_name)
                & (self.scope_df['Status'] == 'Include')
            ]['Value'])
            exclude_vals = set(self.scope_df[
                (self.scope_df['Property'] == dim_name)
                & (self.scope_df['Status'] == 'Exclude')
            ]['Value'])
            if len(include_vals) != 0:
                invalid_vals = sched_dim_vals.difference(include_vals)
                if len(invalid_vals) != 0:
                    raise Exception('The following values '\
                    + f'for dimension {dim_name} should not have been '\
                    + f'included in the schedules: {invalid_vals}')
            if len(exclude_vals) != 0:
                invalid_vals = sched_dim_vals.intersection(exclude_vals)
                if len(invalid_vals) != 0:
                    raise Exception('The following values '\
                    + f'for dimension {dim_name} should have been excluded '\
                    + f'from the schedules: {invalid_vals}')

    def _validate_coverage_report(self):
        # make sure that all dimensions are included in coverage report
        dim_names = set(map(lambda d: d['name'], self.dimension_dicts))
        covered_dims = set(self.coverage_report['Dimension'].unique())
        if dim_names != covered_dims:
            raise Exception('Incorrect dimension coverage in '\
            + f'coverage report. Expected: {dim_names}, Actual: {covered_dims}'
            )

        # for each dimension, check that all dimension values are included
        # in coverage report, and sums of coverage values sum to 1
        for dim_dict in self.dimension_dicts:
            dim_name = dim_dict['name']
            dim_values = set(dim_dict['df'][dim_dict['value']])
            covered_dim_values = set(
                self.coverage_report[
                    self.coverage_report['Dimension'] == dim_name]['Value'])
            if dim_values != covered_dim_values:
                raise Exception('Incorrect dimension '\
                + 'value coverage in coverage report for dimension '\
                + f'{dim_name}. Expected: {dim_values}. Actual: '\
                + f'{covered_dim_values}')
            sum_coverage_vals = sum(
                self.coverage_report[
                    self.coverage_report['Dimension'] == dim_name]
                    ['Prevalence'])
            if sum_coverage_vals - 1 > 1e-8:
                raise Exception('Incorrect sum of coverage values '\
                + f'for dimension {dim_name}. Expected: 1. Actual: '\
                + f'{sum_coverage_vals}')
