# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import pandas as pd
from uuid import uuid4
from envdesign_model.optimization.objective_functions.mean_squared_error\
    import DimensionMSE, RelationshipMSE


def get_schedules_from_cliques(opt_params, sol_cliques):
    # produce ordering of column names
    dim_names = list(map(lambda d: d['name'],
                         opt_params.input_validation.dimension_dicts))
    col_names = ['Group_Id']
    for dim_name in dim_names:
        col_names.append(dim_name)
        col_names.append(dim_name + '_Id')
    
    # get schedules from cliques
    schedules_data = []
    for clique in sol_cliques:
        schedule_row = dict()
        schedule_row['Group_Id'] = str(uuid4())
        for dim_int in range(len(clique)):
            dim_name = opt_params.dim_int_to_dim_name[dim_int]
            dim_value = opt_params.dim_val_int_to_dim_val[clique[dim_int]]
            schedule_row[dim_name] = dim_value
            schedule_row[dim_name + '_Id'] = str(uuid4())
        schedules_data.append(schedule_row)
    schedules = pd.DataFrame(schedules_data)
    schedules = schedules[col_names]
    return schedules


def process_cost(opt_params, cost):
    # get objective function type
    obj_func_type = type(opt_params.objective_functions)
    if obj_func_type == dict:
        key = list(opt_params.objective_functions.keys())[0]
        obj_func_type = type(opt_params.objective_functions[key])

    # translate keys of cost results based on objective function type
    processed_cost = cost
    if obj_func_type == DimensionMSE:
        processed_cost_results = dict()
        cost_results = cost[2]
        for dim_int in cost_results.keys():
            dim = opt_params.dim_int_to_dim_name[dim_int]
            processed_cost_results[dim] = cost_results[dim_int]
        processed_cost = tuple(list(cost[:-1]) + [processed_cost_results])
    elif obj_func_type == RelationshipMSE:
        processed_cost_results = dict()
        cost_results = cost[2]
        for dim_ints in cost_results.keys():
            dim_int1, dim_int2 = dim_ints
            dim1 = opt_params.dim_int_to_dim_name[dim_int1]
            dim2 = opt_params.dim_int_to_dim_name[dim_int2]
            processed_cost_results[(dim1, dim2)] = cost_results[dim_ints]
        processed_cost = tuple(list(cost[:-1]) + [processed_cost_results])

    # return processed cost results
    return processed_cost