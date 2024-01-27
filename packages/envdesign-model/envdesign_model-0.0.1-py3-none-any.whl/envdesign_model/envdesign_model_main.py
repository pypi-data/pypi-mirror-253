# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from envdesign_model.io_validation.input_validation import InputValidation
from envdesign_model.graph_algorithms.graph_algorithms import GraphAlgorithms
from envdesign_model.output_postprocessing.output_postprocessing import\
    OutputPostProcessing
from envdesign_model.io_validation.output_validation import OutputValidation
from envdesign_model.optimization.optimization_strategies.optimization_params\
    import OptimizationParams
from envdesign_model.optimization.optimization_strategies\
    .optimization_strategy1 import OptimizationStrategy1
import time
from envdesign_model.utils import get_logger


def run_envdesign_model(dimension_dicts, relationships_df,
                        num_groups, objective_function, scope_df=None,
                        max_dim_size=100, opt_strategy=1.3, opt_time_limit=90,
                        group_tag='Node', cont_train=False, logger=None):
    # get logger if not provided
    if logger is None:
        logger = get_logger()

    # input validation
    logger.info('Starting input validation...')
    input_val_start = time.time()
    input_validation = InputValidation(
        dimension_dicts, relationships_df, num_groups, objective_function,
        scope_df)
    input_validation.process()
    processed_dimension_dicts = input_validation.dimension_dicts
    processed_relationships_df = input_validation.relationships_df
    processed_objective_function = input_validation.objective_function
    input_val_end = time.time()
    input_val_time = (input_val_end - input_val_start) / 60
    logger.info(f'Input validation completed: {input_val_time} minute(s)')

    # graph algorithms
    logger.info('Starting graph algorithms...')
    graph_alg_start = time.time()
    graph_algorithms = GraphAlgorithms(
        processed_dimension_dicts, processed_relationships_df, num_groups,
        processed_objective_function, scope_df, max_dim_size)
    graph_algorithms.process()
    processed_dimension_dicts = graph_algorithms.dimension_dicts
    processed_relationships_df = graph_algorithms.relationships_df
    graph_alg_end = time.time()
    graph_alg_time = (graph_alg_end - graph_alg_start) / 60
    logger.info(f'Graph algorithms completed: {graph_alg_time} minute(s)')

    # optimization
    logger.info('Starting optimization...')
    opt_start = time.time()
    opt_params = OptimizationParams(input_validation, graph_algorithms)
    if opt_strategy == 1.1:
        opt_strategy = OptimizationStrategy1(
            opt_params, preserve_cc=False, get_new_clique_approach=0,
            logger=logger)
    elif opt_strategy == 1.2:
        opt_strategy = OptimizationStrategy1(
            opt_params, preserve_cc=True, get_new_clique_approach=0,
            logger=logger)
    elif opt_strategy == 1.3:
        opt_strategy = OptimizationStrategy1(
            opt_params, preserve_cc=False, get_new_clique_approach=1,
            logger=logger)
    elif opt_strategy == 1.4:
        opt_strategy = OptimizationStrategy1(
            opt_params, preserve_cc=True, get_new_clique_approach=1,
            logger=logger)
    elif opt_strategy == 1.5:
        opt_strategy = OptimizationStrategy1(
            opt_params, preserve_cc=False, get_new_clique_approach=2,
            logger=logger)
    elif opt_strategy == 1.6:
        opt_strategy = OptimizationStrategy1(
            opt_params, preserve_cc=True, get_new_clique_approach=2,
            logger=logger)
    else:
        raise Exception(
            f'Invalid optimization strategy choice: {opt_strategy}')
    opt_strategy.process(opt_time_limit, cont_train)
    schedules = opt_strategy.schedules_df
    cost = opt_strategy.schedules_cost
    total_cost = cost[0]
    specific_costs = cost[2]
    opt_end = time.time()
    opt_alg_time = (opt_end - opt_start) / 60
    logger.info(f'Optimization completed: {opt_alg_time} minute(s)')

    # output postprocessing
    logger.info('Starting output processing...')
    output_proc_start = time.time()
    output_postprocessing = OutputPostProcessing(
        schedules, processed_dimension_dicts, processed_relationships_df,
        num_groups, group_tag)
    output_postprocessing.process()
    schedules = output_postprocessing.schedules_df
    rel_metadata_info = output_postprocessing.rel_metadata
    coverage_report = output_postprocessing.coverage_report
    output_proc_end = time.time()
    output_proc_time = (output_proc_end - output_proc_start) / 60
    logger.info(
        f'Output postprocessing completed: {output_proc_time} minute(s)')

    # validate output
    logger.info('Starting output validation...')
    output_val_start = time.time()
    output_validation = OutputValidation(
        schedules, processed_dimension_dicts, processed_relationships_df,
        num_groups, coverage_report, rel_metadata_info, scope_df)
    output_validation.process()
    output_val_end = time.time()
    output_val_time = (output_val_end - output_val_start) / 60
    logger.info(f'Output validation completed: {output_val_time} minute(s)')    

    # return schedules
    return schedules, (total_cost, specific_costs), coverage_report
