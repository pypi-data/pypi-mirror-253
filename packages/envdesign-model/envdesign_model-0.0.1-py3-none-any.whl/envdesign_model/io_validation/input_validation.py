# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import pandas as pd
from itertools import permutations
from envdesign_model.io_validation.io_validation_utils import (
    check_type, check_nan_vals, check_df_cols, check_min_length,
    check_dict_keys, check_duplicates)


VALID_RELATIONSHIP_METADATA_TYPES = {
    'One_To_Many': int, 'Many_To_One': int
}
VALID_OBJECTIVE_FUNCTION_TYPES = {
    'dimension', 'relationship', 'combination'
}
VALID_OBJECTIVE_FUNCTION_SPECIFICS = {
    'dimension': {'name', 'metric', 'objective_function', 'weight'},
    'relationship': {'dimension1', 'dimension2', 'metric',
                     'objective_function', 'weight'},
    'combination': {'combinations', 'metric', 'objective_function'}
}
VALID_OBJECTIVE_FUNCTIONS = {'mse'}
DEFAULT_METRIC_VALUES = {
    'Score': 1
}


class InputValidation:
    def __init__(self, dimension_dicts, relationships_df, num_groups,
                 objective_function, scope_df=None):
        self.dimension_dicts = dimension_dicts
        self.relationships_df = relationships_df
        self.num_groups = num_groups
        self.objective_function = objective_function
        self.scope_df = scope_df

    def process(self):
        self._validate_scope_df()
        self._validate_format_relationships_df()
        if self.dimension_dicts is not None and len(self.dimension_dicts) != 0:
            self._validate_dimension_dicts()
        else:
            self._infer_dimension_dicts()
            self._validate_dimension_dicts()
        self._scope_dim_dicts()
        self._create_dim_mappings()
        self._scope_relationships_df()
        self._validate_relationships_df()
        self._validate_num_groups()
        self._validate_objective_function()
        self._deduplicate_dim_vals()
    
    def _validate_scope_df(self):
        # check if scope DataFrame is None
        if self.scope_df is None:
            return
        
        # check type of scope DataFrame
        check_type(self.scope_df, pd.DataFrame)

        # check length of scope DataFrame
        if len(self.scope_df) == 0:
            return
        
        # check columns of scope DataFrame
        check_df_cols(self.scope_df, ['Property', 'Value', 'Status'])

        # check is scope DataFrame has null/NaN values
        check_nan_vals(self.scope_df)

        # check values in Status column
        status_vals = set(self.scope_df['Status'])
        allowed_vals = {'Include', 'Exclude'}
        invalid_vals = status_vals.difference(allowed_vals)
        assert len(invalid_vals) == 0, 'Invalid values present in '\
            + f'\'Status\' column of scope DataFrame: {invalid_vals}'
    
    def _validate_format_relationships_df(self):
        # check type of relationships DataFrame
        check_type(self.relationships_df, pd.DataFrame)

        # check NaN values
        check_nan_vals(self.relationships_df)

        # check column types of relationships DataFrame
        check_df_cols(
            self.relationships_df,
            string_type_cols=['Dimension1', 'Value1', 'Dimension2', 'Value2'],
            object_type_cols=['RelationshipMetaData'])
    
    def _validate_dimension_dicts(self):
        # check type of dimension dicts
        check_type(self.dimension_dicts, list)

        # check that there are at least two dimensions
        check_min_length(self.dimension_dicts, 2)

        # check each dimension dict, remove null/empty values
        for dim_dict in self.dimension_dicts:
            check_type(dim_dict, dict)
            check_type(dim_dict['name'], str)
            check_type(dim_dict['value'], str)
            check_type(dim_dict['df'], pd.DataFrame)
            # remove null/empty dimension values from dimension dictionaries
            for i in range(len(self.dimension_dicts)):
                dim_df = self.dimension_dicts[i]['df']
                dim_val_col = self.dimension_dicts[i]['value']
                self.dimension_dicts[i]['df'] = dim_df[
                    ~((dim_df[dim_val_col].isna())
                    | (dim_df[dim_val_col].eq('')))]
            check_min_length(dim_dict['df'], 1)
            check_df_cols(dim_dict['df'], string_type_cols=[dim_dict['value']])
    
    def _infer_dimension_dicts(self):
        # preserves order in which dimensions appear in relationships DataFrame
        dim_names = [] 
        dim_name_to_dim_values = dict()
        dim_name_to_dim_values_set = dict() # for fast lookup/duplicate check
        for _, row in self.relationships_df.iterrows():
            dim1 = row['Dimension1']
            val1 = row['Value1']
            dim2 = row['Dimension2']
            val2 = row['Value2']
            for dim, val in [(dim1, val1), (dim2, val2)]:
                if val == '<ANY>':
                    raise Exception(
                        f'Dimension value for dimension {dim} in '
                        + 'relationships DataFrame cannot be <ANY> '
                        + 'if no dimension dictionaries are provided')
                if dim not in dim_name_to_dim_values.keys():
                    dim_names.append(dim)
                    dim_name_to_dim_values[dim] = list()
                    dim_name_to_dim_values_set[dim] = set()
                if val not in dim_name_to_dim_values_set[dim]:
                    dim_name_to_dim_values[dim].append(val)
                    dim_name_to_dim_values_set[dim].add(val)

        # create dimension dictionaries from dimension names and values
        self.dimension_dicts = []
        for dim_name in dim_names:
            dim_values = dim_name_to_dim_values[dim_name]
            dim_dict = dict()
            dim_dict['name'] = dim_name
            dim_dict['value'] = dim_name
            df_dict = dict()
            df_dict[dim_name] = dim_values
            for metric, default_value in DEFAULT_METRIC_VALUES.items():
                df_dict[metric] = [default_value] * len(dim_values)
            dim_dict['df'] = pd.DataFrame(df_dict)
            self.dimension_dicts.append(dim_dict)
    
    def _scope_dim_dicts(self):
        scoped_dim_dicts = []
        for dim_dict in self.dimension_dicts:
            dim_name = dim_dict['name']
            dim_val_col = dim_dict['value']
            dim_df = dim_dict['df']

            # scope based on include/exclude status
            if self.scope_df is not None and len(self.scope_df) != 0:
                include_values = self.scope_df[
                    (self.scope_df['Property'] == dim_name)
                    & (self.scope_df['Status'] == 'Include')
                ]['Value']
                include_values = set(map(lambda v: v.lower(), include_values))
                exclude_values = self.scope_df[
                    (self.scope_df['Property'] == dim_name)
                    & (self.scope_df['Status'] == 'Exclude')
                ]['Value']
                exclude_values = set(map(lambda v: v.lower(), exclude_values))
                
                if len(include_values) != 0:
                    dim_df = dim_df[
                        dim_df[dim_val_col].str.lower().isin(include_values)]
                if len(exclude_values) != 0:
                    dim_df = dim_df[
                        ~dim_df[dim_val_col].str.lower().isin(exclude_values)]
            
            # check that dimension values DataFrame is not empty
            if len(dim_df) == 0:
                raise Exception(
                    f'Dimension values DataFrame for dimension {dim_name} '
                    + 'is empty after scoping dimension values.')
            
            # add scoped dimension dictionary
            scoped_dim_dict = {
                'name': dim_name,
                'value': dim_val_col,
                'df': dim_df.reset_index(drop=True)
            }
            scoped_dim_dicts.append(scoped_dim_dict)
        self.dimension_dicts = scoped_dim_dicts
    
    def _create_dim_mappings(self):
        self.dim_name_to_dim_values = dict()
        self.dim_name_to_dim_df = dict()
        for dim_dict in self.dimension_dicts:
            dim_values = dim_dict['df'][dim_dict['value']].values
            self.dim_name_to_dim_values[dim_dict['name']] = set(dim_values)
            self.dim_name_to_dim_df[dim_dict['name']] = dim_dict['df']
            for dim_val in dim_values:
                if dim_val == '<ANY>':
                    raise Exception('Dimension value cannot be <ANY>')
    
    def _scope_relationships_df(self):
        dim_name_to_dim_values = dict()
        for dim_dict in self.dimension_dicts:
            dim_name = dim_dict['name']
            dim_values = set(dim_dict['df'][dim_dict['value']])
            dim_name_to_dim_values[dim_name] = dim_values
        
        # only keep relationships with both dimension values
        # specified in dimension dictionaries
        self.relationships_df = self.relationships_df[
            (self.relationships_df['Dimension1'].isin(
                dim_name_to_dim_values.keys()))
            & (self.relationships_df['Dimension2'].isin(
                dim_name_to_dim_values.keys()))
        ]
        indices = []
        for idx, row in self.relationships_df.iterrows():
            dim1 = row['Dimension1']
            val1 = row['Value1']
            dim2 = row['Dimension2']
            val2 = row['Value2']
            check_vals = (
                (val1 == '<ANY>' and val2 == '<ANY>')
                or (val1 in dim_name_to_dim_values[dim1] and
                    val2 == '<ANY>')
                or (val1 == '<ANY>' and val2 in
                    dim_name_to_dim_values[dim2])
                or (val1 in dim_name_to_dim_values[dim1] and val2 in
                    dim_name_to_dim_values[dim2])
            )
            if check_vals:
                indices.append(idx)
        self.relationships_df = self.relationships_df.loc[indices]\
            .reset_index(drop=True)
    
    def _validate_relationships_df(self):
        # check relationships
        rel_dim_pairs = set()
        for _, relationship in self.relationships_df.iterrows():
            dimension1 = relationship['Dimension1']
            value1 = relationship['Value1']
            dimension2 = relationship['Dimension2']
            value2 = relationship['Value2']
            relationship_metadata = relationship['RelationshipMetaData']
            rel_dim_pairs.add((dimension1, dimension2))
            rel_dim_pairs.add((dimension2, dimension1))

            # check if dimensions are valid, and dimension values are present
            # in dimension DataFrames
            for dimension, value in [
                    (dimension1, value1), (dimension2, value2)]:
                if dimension not in self.dim_name_to_dim_values.keys():
                    raise Exception(f'Dimension {dimension} has no '
                                    + 'corresponding dimension dictionary')
                if value != '<ANY>' and value not in \
                        self.dim_name_to_dim_values[dimension]:
                    raise Exception(f'Dimension {dimension} DataFrame does '
                                    + f'not have value {value}')

            # check if dimension values are of same dimension
            if dimension1 == dimension2:
                raise Exception('Relationship cannot exist between dimension '
                                + f'values ({value1}, {value2}) of the same '
                                + f'dimension ({dimension1})')

            # check relationship metadata
            check_type(relationship_metadata, list)
            for metadata in relationship_metadata:
                check_dict_keys(metadata, {'name', 'value'})
                check_type(metadata['name'], str)
                if metadata['name'] not in\
                        VALID_RELATIONSHIP_METADATA_TYPES.keys():
                    raise Exception('Relationship metadata name '
                                    + f'{metadata["name"]} is invalid')
                check_type(
                    metadata['value'],
                    VALID_RELATIONSHIP_METADATA_TYPES[metadata['name']])
        
        # check relationship dimension pairs
        expected_dimension_pairs = set(permutations(
            self.dim_name_to_dim_values.keys(), 2))
        diff_dim_pairs = expected_dimension_pairs.difference(rel_dim_pairs)
        missing_dim_pairs = set()
        for dim1, dim2 in diff_dim_pairs:
            if (dim1, dim2) not in missing_dim_pairs and (dim2, dim1) not in\
                    missing_dim_pairs:
                missing_dim_pairs.add((dim1, dim2))
        if len(missing_dim_pairs) != 0:
            raise Exception(
                'Relationships DataFrame missing relationships between the '
                + f'following pairs of dimensions: {missing_dim_pairs}')
    
    def _validate_num_groups(self):
        if self.num_groups <= 0:
            raise Exception(f'Invalid value for num_groups ({self.num_groups})'
                            + ', number of groups must be greater than 0')
   
    def _validate_objective_function(self):
        # check type of objective function dictionary
        check_type(self.objective_function, dict)

        # check keys of objective function dictionary
        check_dict_keys(self.objective_function, {'type', 'specifics'})

        # check objective function type
        obj_func_type = self.objective_function['type']
        if obj_func_type not in\
                VALID_OBJECTIVE_FUNCTION_TYPES:
            raise Exception('Objective function type '
                            + f'{self.objective_function["type"]} is invalid.')

        # check objective function specifics
        specifics = self.objective_function['specifics']
        check_type(specifics, list)
        for specific in specifics:
            check_type(specific, dict)
            check_dict_keys(
                specific,
                VALID_OBJECTIVE_FUNCTION_SPECIFICS[obj_func_type])
            if specific['objective_function'] not in\
                    VALID_OBJECTIVE_FUNCTIONS:
                raise Exception(
                    f'Invalid objective function '
                    + f'({specific["objective_function"]}), expected one '
                    + f'of: {VALID_OBJECTIVE_FUNCTIONS}')
        if obj_func_type == 'dimension':
            for specific in specifics:
                if not isinstance(specific['weight'], int) and not\
                        isinstance(specific['weight'], float):
                    raise Exception(
                        'Invalid weight for objective function '
                        + f'specific ({specific["weight"]}), expected '
                        + 'numeric value (int or float)')
                if specific['name'] not in set(
                        self.dim_name_to_dim_values.keys()):
                    raise Exception(
                        'Objective function dimension '
                        + f'{specific["name"]} has no dimension '
                        + 'dictionary')
                dim_df = self.dim_name_to_dim_df[specific['name']]
                if specific['metric'] not in set(dim_df.columns):
                    raise Exception(
                        'Objective function metric '
                        + f'{specific["metric"]} for dimension '
                        + f'{specific["name"]} not present in '
                        + 'dimension dictionary')
                check_df_cols(dim_df, numeric_type_cols=[specific['metric']])
        elif obj_func_type == 'relationship':
            for specific in specifics:
                if not isinstance(specific['weight'], int) and not\
                        isinstance(specific['weight'], float):
                    raise Exception(
                        'Invalid weight for objective function '
                        + f'specific ({specific["weight"]}), expected '
                        + 'numeric value (int or float)')
                if specific['metric'] not in set(
                        self.relationships_df.columns):
                    raise Exception(
                        f'Objective function metric {specific["metric"]}'
                        + f'for dimensions {specific["dimension1"]} and '
                        + f'{specific["dimension2"]} not present in '
                        + 'relationships DataFrame')
                for dimension in [specific['dimension1'],
                                  specific['dimension2']]:
                    if dimension not in self.dim_name_to_dim_df.keys():
                        raise Exception(
                            f'Dimension {dimension} has no corresponding '\
                            + 'dimension dictionary/DataFrame')
                if specific['dimension1'] == specific['dimension2']:
                    raise Exception(
                        'Relationship-based objective function cannot be '\
                        + 'computed on one dimension: '
                        + f'{specific["dimension1"]}')
        elif obj_func_type == 'combination':
            for i in range(len(specifics)):
                specific = specifics[i]
                combinations = specific['combinations']
                metric = specific['metric']
                check_type(combinations, list)
                valid_combinations = []
                for combo_info in combinations:
                    combo = combo_info['combination']
                    metric_vals = combo_info['metric_values']

                    # check length of combination
                    if len(combo) != len(self.dimension_dicts):
                        raise Exception(
                            f'Combination {combo} must be the same length as '
                            + 'the list of dimension dictionaries')
                    
                    # check dict keys for each dimension value dict in
                    # combination
                    for dim_val in combo:
                        check_dict_keys(dim_val, {'dimension', 'value'})

                    # check that combination is across all dimensions             
                    combo_dim_names = set(map(lambda d: d['dimension'],
                                              combo))
                    dim_names = set(self.dim_name_to_dim_values.keys())
                    if combo_dim_names != dim_names:
                        raise Exception(
                            f'Combination has invalid dimensions. Expected: '
                            + f'{dim_names}. Actual: {combo_dim_names}')
                    
                    # only include combinations where each dimension value
                    # is valid
                    valid_combo = True
                    for dim_val in combo:
                        dimension = dim_val['dimension']
                        value = dim_val['value']
                        if value != '<ANY>' and value not in\
                                self.dim_name_to_dim_values[dimension]:
                            valid_combo=False
                            break
                    if valid_combo:
                        valid_combinations.append(combo_info)
                    
                    # check metric and metric values
                    check_type(metric_vals, list)
                    check_min_length(metric_vals, 1)
                    for metric_value in metric_vals:
                        check_type(metric_value, dict)
                        check_dict_keys(metric_value, {'name', 'value'})
                    metric_names = set(map(lambda m: m['name'], metric_vals))
                    if metric not in metric_names:
                        raise Exception(
                            f'Metric {metric} not specified in metric values '
                            + 'for combination-based objective function '
                            + f'specific {specific}')
                self.objective_function['specifics'][i]['combinations'] =\
                    valid_combinations
                combos = self.objective_function['specifics'][i][
                    'combinations']
                if len(combos) == 0:
                    raise Exception(
                        'Combination based objective function specifics '
                        + f'(list item {i}) contains no valid combinations '
                        + f'under the given scope data, dimension '
                        + f'dictionaries, and relationships')

        # check length and check for duplicates in objective function specifics
        if obj_func_type == 'dimension':
            dimensions = list(map(lambda s: s['name'], specifics))
            check_duplicates(dimensions)
            if len(dimensions) != len(self.dimension_dicts):
                raise Exception(
                    'Invalid number of dimension-based objective '
                    + f'functions. Expected: {len(self.dimension_dicts)}. '
                    + f'Actual: {len(dimensions)}')
        elif obj_func_type == 'relationship':
            dim_pairs = set()
            for specific in specifics:
                dim1 = specific['dimension1']
                dim2 = specific['dimension2']
                if (dim1, dim2) in dim_pairs or (dim2, dim1) in dim_pairs:
                    raise Exception('Duplicate dimension pairs found in '
                                    + 'specifics for relationship-based '
                                    + 'objective function')
                else:
                    dim_pairs.add((dim1, dim2))
            num_dims = len(self.dimension_dicts)
            if len(dim_pairs) != num_dims * (num_dims - 1) / 2:
                raise Exception(
                    'Invalid number of relationship-based objective '
                    + f'functions. Expected: {num_dims * (num_dims - 1)  /2}. '
                    + f'Actual: {len(dim_pairs)}')
        elif obj_func_type == 'combination':
            if len(specifics) != 1:
                raise Exception(
                    'Invalid length of specifics list for combination-based '
                    + 'objective function. Expected: 1, Actual: '
                    + f'{len(specifics)}'
                )
            check_min_length(specifics[0]['combinations'], 1)


    def _deduplicate_dim_vals(self):
        # for each dimension, deduplicate dimension values based on max
        # metric value (if objective function is dimension-based), otherwise
        # deduplicate by first occurrences
        if self.objective_function['type'] == 'dimension':
            dedup_dim_dicts = []
            for i in range(len(self.dimension_dicts)):
                # get metric column
                dim_name = self.dimension_dicts[i]['name']
                for spec in self.objective_function['specifics']:
                    if spec['name'] == dim_name:
                        metric_col = spec['metric']
                
                # replace null or empty values with 0
                self.dimension_dicts[i]['df'][metric_col].fillna(
                    0, inplace=True)
                self.dimension_dicts[i]['df'][metric_col].replace(
                    '', 0, inplace=True)
                self.dimension_dicts[i]['df'][metric_col] = pd.to_numeric(
                    self.dimension_dicts[i]['df'][metric_col])

                # get index of max metric value for each dimension value
                dim_df = self.dimension_dicts[i]['df']
                dim_val_col = self.dimension_dicts[i]['value']
                idxs = []
                for dim_val in dim_df[dim_val_col].unique():
                    sub_df = dim_df[dim_df[dim_val_col] == dim_val]
                    max_idx = sub_df[metric_col].idxmax()
                    idxs.append(max_idx)

                # deduplicate dimension values
                dedup_dim_dict = dict()
                for key in ['name', 'value']:
                    dedup_dim_dict[key] = self.dimension_dicts[i][key]
                dedup_dim_dict['df'] = dim_df.loc[idxs].reset_index(
                    drop=True)
                dedup_dim_dicts.append(dedup_dim_dict)
            self.dimension_dicts = dedup_dim_dicts
        else:
            dedup_dim_dicts = []
            for i in range(len(self.dimension_dicts)):
                # deduplicate dimension values
                dedup_dim_dict = dict()
                for key in ['name', 'value']:
                    dedup_dim_dict[key] = self.dimension_dicts[i][key]
                dedup_dim_dict['df'] = self.dimension_dicts[i]['df']\
                    .drop_duplicates(
                    subset=[self.dimension_dicts[i]['value']],
                    ignore_index=True)
                dedup_dim_dicts.append(dedup_dim_dict)
            self.dimension_dicts = dedup_dim_dicts
