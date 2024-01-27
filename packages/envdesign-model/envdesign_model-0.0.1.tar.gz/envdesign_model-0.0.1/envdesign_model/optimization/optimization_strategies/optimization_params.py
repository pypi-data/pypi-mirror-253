# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from envdesign_model.optimization.objective_functions.mean_squared_error\
    import DimensionMSE, RelationshipMSE, CombinationMSE
from envdesign_model.optimization.optimization_utils import sort_tuple


MAX_ITERS = int(1e20) # very high bound for iterations so
# algorithms utilize all compute time within the time limit


class OptimizationParams():
    def __init__(self, input_validation, graph_algorithms):
        # get information from input validation instance 
        self.input_validation = input_validation
        self.num_groups = self.input_validation.num_groups

        # get information from graph validation instance 
        self.graph_algorithms = graph_algorithms
        self.graph = self.graph_algorithms.graph
        # clique cover, with vertices sorted in each clique
        sorted_clique_cover = list()
        for clique in self.graph_algorithms.clique_cover:
            sorted_clique_cover.append(sort_tuple(clique))
        self.clique_cover = sorted_clique_cover
        self.dimension_dicts = self.graph_algorithms.dimension_dicts
        self.relationships_df = self.graph_algorithms.relationships_df
        self.dim_val_int_to_dim_val = self.graph_algorithms.int_to_dim_value
        self.dim_val_to_dim_val_int = self.graph_algorithms.dim_value_to_int
        self.dim_name_to_dim_values = self.graph_algorithms\
            .dim_name_to_dim_values
        self.obj_func_specs = self.graph_algorithms.objective_function

        # map each dimension name to the dimension dictionary
        # map each dimension name to an integer (dimension integer)
        # and vice versa
        # map dimension value integer to dimension name
        dim_int = 0
        self.dim_int_to_dim_name = dict()
        self.dim_name_to_dim_int = dict()
        self.dim_name_to_dim_dict = dict()
        for dim_dict in self.dimension_dicts:
            self.dim_name_to_dim_dict[dim_dict['name']] = dim_dict
            self.dim_int_to_dim_name[dim_int] = dim_dict['name']
            self.dim_name_to_dim_int[dim_dict['name']] = dim_int
            dim_int += 1

        # build objective functions
        if self.obj_func_specs['type'] == 'dimension':
            self.objective_functions = dict()

            # get sum of weights, for weight normalization
            sum_weights = sum(list(map(lambda s: s['weight'],
                                    self.obj_func_specs['specifics'])))
            # to prevent divide by 0 errors
            weight_norm = 1 if sum_weights == 0 else sum_weights

            # build objective function for each specifics dictionary
            for spec in self.obj_func_specs['specifics']:
                dim_int = self.dim_name_to_dim_int[spec['name']]
                dim_dict = self.dim_name_to_dim_dict[spec['name']]
                if spec['objective_function'] == 'mse':
                    # get target values for each dimension value integer
                    # under the current dimension
                    target_values = dict()
                    for _, row in dim_dict['df'].iterrows():
                        dim_value_int = self.dim_val_to_dim_val_int[
                            row[dim_dict['value']]]
                        target_val = row[spec['metric']]
                        target_values[dim_value_int] = target_val

                    # build dimension-based MSE function, map to dimension
                    # integer
                    self.objective_functions[dim_int] = DimensionMSE(
                        target_values, spec['weight'] / weight_norm, True)
        elif self.obj_func_specs['type'] == 'relationship':
            self.objective_functions = dict()
            
            # get sum of weights, for weight normalization
            sum_weights = sum(list(map(lambda s: s['weight'],
                                    self.obj_func_specs['specifics'])))
            # to prevent divide by 0 errors
            weight_norm = 1 if sum_weights == 0 else sum_weights

            # build objective function for each specifics dictionary
            for spec in self.obj_func_specs['specifics']:
                dim1_int = self.dim_name_to_dim_int[spec['dimension1']]
                dim2_int = self.dim_name_to_dim_int[spec['dimension2']]
                metric = spec['metric']
                if spec['objective_function'] == 'mse':
                    # scope relationships DataFrame to relevant dimensions
                    scoped_relationships_df = self.relationships_df[
                        ((self.relationships_df['Dimension1'] ==
                            spec['dimension1'])
                            & (self.relationships_df['Dimension2'] ==
                                spec['dimension2']))
                        | ((self.relationships_df['Dimension1'] ==
                            spec['dimension2'])
                            & (self.relationships_df['Dimension2'] ==
                                spec['dimension1']))
                    ]

                    # determine target values for each relationship/pair of
                    # dimension values
                    target_val_dicts = dict()
                    for _, relationship in scoped_relationships_df.iterrows():
                        dimension1 = relationship['Dimension1']
                        value1 = relationship['Value1']
                        dimension2 = relationship['Dimension2']
                        value2 = relationship['Value2']
                        if value1 == '<ANY>' and value2 != '<ANY>':
                            for dim1_value in self.dim_name_to_dim_values[
                                    dimension1]:
                                dim_val1_int = self.dim_val_to_dim_val_int[
                                    dim1_value]
                                dim_val2_int = self.dim_val_to_dim_val_int[
                                    value2]
                                target_dict = {
                                    'target_val': relationship[metric],
                                    'any_count': 1
                                }
                                target_val_dicts = _update_target_val_dict(
                                    target_val_dicts, (dim_val1_int,
                                    dim_val2_int), target_dict)
                        elif value1 != '<ANY>' and value2 == '<ANY>':
                            for dim2_value in self.dim_name_to_dim_values[
                                    dimension2]:
                                dim_val1_int = self.dim_val_to_dim_val_int[
                                    value1]
                                dim_val2_int = self.dim_val_to_dim_val_int[
                                    dim2_value]
                                target_dict = {
                                    'target_val': relationship[metric],
                                    'any_count': 1
                                }
                                target_val_dicts = _update_target_val_dict(
                                    target_val_dicts, (dim_val1_int,
                                    dim_val2_int), target_dict)
                        elif value1 == '<ANY>' and value2 == '<ANY>':
                            for dim1_value in self.dim_name_to_dim_values[
                                    dimension1]:
                                for dim2_value in self.dim_val_to_dim_val_int[
                                        dimension2]:
                                    dim_val1_int = self.dim_val_to_dim_val_int[
                                        dim1_value]
                                    dim_val2_int = self.dim_val_to_dim_val_int[
                                        dim2_value]
                                    target_dict = {
                                        'target_val': relationship[metric],
                                        'any_count': 2
                                    }
                                    target_val_dicts = _update_target_val_dict(
                                        target_val_dicts, (dim_val1_int,
                                        dim_val2_int), target_dict)
                        else:
                            dim_val1_int = self.dim_val_to_dim_val_int[value1]
                            dim_val2_int = self.dim_val_to_dim_val_int[value2]
                            target_dict = {
                                'target_val': relationship[metric],
                                'any_count': 0
                            }
                            target_val_dicts = _update_target_val_dict(
                                target_val_dicts, (dim_val1_int, dim_val2_int),
                                target_dict)

                    # get resulting target values (without any_count values)
                    target_values = dict()
                    for dim_val_int_pair in target_val_dicts.keys():
                        new_dim_val_int_pair = sort_tuple(dim_val_int_pair)
                        target_values[new_dim_val_int_pair] = target_val_dicts[
                            dim_val_int_pair]['target_val']

                    # create objective function
                    dim_pair = sort_tuple((dim1_int, dim2_int))
                    self.objective_functions[dim_pair] =\
                        RelationshipMSE(
                        target_values, spec['weight'] / weight_norm, True)
        elif self.obj_func_specs['type'] == 'combination':
            spec = self.obj_func_specs['specifics'][0]
            combinations = spec['combinations']
            metric = spec['metric']
            if spec['objective_function'] == 'mse':
                target_val_dicts = dict()
                for combo_info in combinations:
                    metric_vals = list(filter(
                        lambda m: m['name'] == metric,
                        combo_info['metric_values']))
                    metric_val = max(list(map(
                        lambda mv: mv['value'], metric_vals)))
                    combo = combo_info['combination']
                    combo_tuples = _get_combination_tuples(
                        combo, self.dim_name_to_dim_values,
                        self.dim_val_to_dim_val_int)
                    any_count = len(
                        list(filter(lambda c: c['value'] == '<ANY>', combo)))
                    target_dict = {
                        'target_val': metric_val,
                        'any_count': any_count
                    }
                    for dim_val_ints in combo_tuples:
                        target_val_dicts = _update_target_val_dict(
                            target_val_dicts, dim_val_ints, target_dict)
                    
                # get resulting target values (without any_count values)
                target_values = dict()
                for dim_val_int_tuple in target_val_dicts.keys():
                    new_dim_val_int_tuple = sort_tuple(dim_val_int_tuple)
                    target_values[new_dim_val_int_tuple] = target_val_dicts[
                        dim_val_int_tuple]['target_val']
                
                # create objective function
                self.objective_functions = CombinationMSE(
                    target_values, True)


def _get_combination_tuples(combination, dim_name_to_dim_values,
                            dim_val_to_dim_val_int):
    # format combination information in a dictionary
    combo_dict = dict()
    for dim_val in combination:
        combo_dict[dim_val['dimension']] = dim_val['value']
    
    # get combinations by expanding <ANY> values
    dim_names = list(dim_name_to_dim_values.keys())
    combos_list = [[]] 
    for dim_name in dim_names:
        if combo_dict[dim_name] == '<ANY>':
            dim_vals = dim_name_to_dim_values[dim_name]
        else:
            dim_vals = [combo_dict[dim_name]]
        
        new_combos_list = []
        for combo in combos_list:
            for dim_val in dim_vals:
                dim_val_int = dim_val_to_dim_val_int[dim_val]
                new_combos_list.append(combo + [dim_val_int])
        combos_list = new_combos_list
    combos_list = list(map(lambda c: tuple(c), combos_list))
    return combos_list


def _update_target_val_dict(target_val_dicts, dim_val_ints,
                            target_dict):
    # update target value based on any_count value
    dim_val_int_key = sort_tuple(dim_val_ints)
    if dim_val_int_key in target_val_dicts.keys():
        orig_target_val_dict = target_val_dicts[dim_val_int_key]
        orig_target_val = orig_target_val_dict['target_val']
        new_target_val = target_dict['target_val']
        orig_any_count = orig_target_val_dict['any_count']
        new_any_count = target_dict['any_count']
        if new_any_count < orig_any_count:
            target_val_dicts[dim_val_int_key] = target_dict
        elif new_any_count == orig_any_count:
            target_val_dicts[dim_val_int_key]['target_val'] =\
                max(orig_target_val, new_target_val)
    else:
        target_val_dicts[dim_val_int_key] = target_dict
    return target_val_dicts
