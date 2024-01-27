# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import pandas as pd
from copy import deepcopy
from uuid import uuid4 


class OutputPostProcessing:
    def __init__(self, schedules_df, dimension_dicts, relationships_df,
                 num_groups, group_tag):
        self.schedules_df = schedules_df
        self.dimension_dicts = dimension_dicts
        self.relationships_df = relationships_df
        self.num_groups = num_groups
        self.group_tag = group_tag
    
    def process(self):
        self._get_relationship_metadata_info()
        self._apply_relationship_metadata([
            self._apply_one_to_many,
        ])
        self._add_group_tag_col()
        self._generate_coverage_report()

    def _any_count(self, val1, val2):
        # counts the number of <ANY>s in the two dimension values in a 
        # relationship
        if val1 == '<ANY>' and val2 =='<ANY>':
            return 2
        elif val1 == '<ANY>' or val2 =='<ANY>':
            return 1
        else:
            return 0

    def _convert_rel_md_type(self, rel, md_type):
        # reconcile reflexive metadata types and relationships
        # (e.g. 'Many_To_One' is converted to 'One_To_Many')
        new_rel = rel
        new_md_type = md_type
        if md_type == 'Many_To_One':
            new_rel = (rel[2], rel[3], rel[0], rel[1])
            new_md_type = 'One_To_Many'
        return new_rel, new_md_type

    def _update_relationship_metadata(self, dim1, val1, dim2, val2, metadata):
        for md_type, md_value in metadata['metadata'].items():
            new_rel, new_md_type = self._convert_rel_md_type(
                (dim1, val1, dim2, val2), md_type)
            if new_rel not in self.rel_metadata.keys():
                self.rel_metadata[new_rel] = {
                    'metadata': {new_md_type: md_value},
                    'any_count': metadata['any_count']
                }
            else:
                any_count_prior = self.rel_metadata[new_rel]['any_count']
                any_count_rel = metadata['any_count']
                if any_count_rel == any_count_prior:
                    # if current and existing relationship metadata values come
                    # from relationships with same number of <ANY> values, take
                    # the max of the two values
                    self.rel_metadata[new_rel]['any_count'] = any_count_rel
                    if new_md_type in self.rel_metadata[new_rel][
                            'metadata'].keys():
                        self.rel_metadata[new_rel]['metadata'][new_md_type] =\
                            max(self.rel_metadata[new_rel]['metadata'][
                                new_md_type], md_value)
                    else:
                        self.rel_metadata[new_rel]['metadata'][new_md_type] =\
                            md_value
                elif any_count_rel < any_count_prior:
                    # if current relationship metadata value come from a
                    # relationship with less <ANY> values, override existing
                    # metadata value
                    self.rel_metadata[new_rel]['any_count'] = any_count_rel
                    self.rel_metadata[new_rel]['metadata'][new_md_type] =\
                        md_value

    def _get_relationship_metadata_info(self):
        # get list of dimension names and dimension values associated with
        # each dimension name
        self.dim_names = []
        self.dim_name_to_dim_vals = dict()
        for dim_dict in self.dimension_dicts:
            self.dim_names.append(dim_dict['name'])
            self.dim_name_to_dim_vals[dim_dict['name']] = list(
                dim_dict['df'][dim_dict['value']])
        
        # create relationship to metadata mappings
        self.rel_metadata = dict()
        for _, row in self.relationships_df.iterrows():
            # get dimension names and values
            dim1 = row['Dimension1']
            val1 = row['Value1']
            dim2 = row['Dimension2']
            val2 = row['Value2']
            # get number of <ANY> dimension values
            any_count_rel = self._any_count(val1, val2)
            
            # map metadata to relationships
            if val1 == '<ANY>' and val2 == '<ANY>':
                for dim_val1 in self.dim_name_to_dim_vals[dim1]:
                    for dim_val2 in self.dim_name_to_dim_vals[dim2]:
                        metadata = {
                            'any_count': any_count_rel,
                            'metadata': dict()
                        }
                        for md in row['RelationshipMetaData']:
                            metadata['metadata'][md['name']] = md['value']
                        self._update_relationship_metadata(
                            dim1, dim_val1, dim2, dim_val2, metadata)
            elif val1 == '<ANY>' and val2 != '<ANY>':
                for dim_val1 in self.dim_name_to_dim_vals[dim1]:
                    metadata = {
                        'any_count': any_count_rel,
                        'metadata': dict()
                    }
                    for md in row['RelationshipMetaData']:
                        metadata['metadata'][md['name']] = md['value']
                    self._update_relationship_metadata(
                        dim1, dim_val1, dim2, val2, metadata)
            elif val1 != '<ANY>' and val2 == '<ANY>':
                for dim_val2 in self.dim_name_to_dim_vals[dim2]:
                    metadata = {
                        'any_count': any_count_rel,
                        'metadata': dict()
                    }
                    for md in row['RelationshipMetaData']:
                        metadata['metadata'][md['name']] = md['value']
                    self._update_relationship_metadata(
                        dim1, val1, dim2, dim_val2, metadata)
            else:
                metadata = {
                    'any_count': any_count_rel,
                    'metadata': dict()
                }
                for md in row['RelationshipMetaData']:
                    metadata['metadata'][md['name']] = md['value']
                self._update_relationship_metadata(
                    dim1, val1, dim2, val2, metadata)
        
        # remove the any_count key from metadata
        for rel in self.rel_metadata.keys():
            self.rel_metadata[rel] = self.rel_metadata[rel]['metadata']   
    
    def _apply_relationship_metadata(self, apply_funcs):
        schedules_df = deepcopy(self.schedules_df)

        # for all dimension pairs, apply functions corresponding to each
        # metadata type
        for i in range(0, len(self.dim_names) - 1):
            for j in range(i, len(self.dim_names)):
                for dim1_idx, dim2_idx in [(i, j), (j, i)]:
                    dim1 = self.dim_names[dim1_idx]
                    dim2 = self.dim_names[dim2_idx]
                    new_schedules_df = pd.DataFrame()
                    for _, row in schedules_df.iterrows():
                        val1 = row[dim1]
                        val2 = row[dim2]
                        rel = (dim1, val1, dim2, val2)                        

                        # start from existing row, and then successively apply
                        # the functions corresponding to specific metadata
                        # type to produce additional rows
                        new_rows_df = pd.DataFrame([row]).reset_index(
                            drop=True)
                        if rel in self.rel_metadata.keys():
                            for apply_func in apply_funcs:
                                new_rows_df = apply_func(
                                    dim1, dim2, new_rows_df,
                                    self.rel_metadata[rel])
                            
                        # combine produced rows
                        new_schedules_df = pd.concat([
                            new_schedules_df, new_rows_df], axis=0,
                            ignore_index=True)
                    schedules_df = new_schedules_df
        self.schedules_df = schedules_df

    def _apply_one_to_many(self, dim1, dim2, sched_rows_df, metadata):
        if 'One_To_Many' not in metadata.keys():
            return sched_rows_df
        one_to_many_count = metadata['One_To_Many']
        new_rows_df = pd.DataFrame()
        # determine id columns to be updated
        for idx in range(len(self.dim_names)):
            if self.dim_names[idx] == dim1:
                dim1_idx = idx
        update_id_cols = list(map(lambda c: c + '_Id',
                                  self.dim_names[dim1_idx + 1:]))
        for _, row in sched_rows_df.iterrows():
            # duplicate rows and update ids
            new_rows = pd.DataFrame([row] * one_to_many_count).reset_index(
                drop=True)
            for i in range(1, one_to_many_count):
                for col in update_id_cols:
                    new_rows.at[i, col] = str(uuid4())
            new_rows_df = pd.concat([new_rows_df, new_rows], axis=0,
                                    ignore_index=True)
        return new_rows_df
    
    def _add_group_tag_col(self):
        self.schedules_df.insert(1, 'Group_Tag', self.group_tag)

    def _generate_coverage_report(self):
        coverage_report_rows = []
        for dim_dict in self.dimension_dicts:
            dim_name = dim_dict['name']
            dim_values = dim_dict['df'][dim_dict['value']].unique()
            for dim_value in dim_values:
                sub_df = self.schedules_df[
                    self.schedules_df[dim_name] == dim_value]
                dim_val_coverage = len(sub_df['Group_Id'].unique())\
                    / self.num_groups
                coverage_report_rows.append({
                    'Dimension': dim_name,
                    'Value': dim_value, 
                    'Prevalence': dim_val_coverage
                })
        self.coverage_report = pd.DataFrame(coverage_report_rows)
