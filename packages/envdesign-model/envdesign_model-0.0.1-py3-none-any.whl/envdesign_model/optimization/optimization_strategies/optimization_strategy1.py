# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from envdesign_model.optimization.optimization_strategies\
    .optimization_strategy import OptimizationStrategy
from envdesign_model.optimization.algorithms.expand_clique_cover_sa import\
    ExpandCliqueCoverSA
from envdesign_model.optimization.optimization_strategies.optimization_params\
    import MAX_ITERS
from envdesign_model.optimization.optimization_strategies\
    .optimization_strategy_utils import get_schedules_from_cliques,\
        process_cost
from optimizn.combinatorial.opt_problem import load_latest_pckl


class OptimizationStrategy1(OptimizationStrategy):
    '''
    Get a coverage schedule using branch and bound, then expand the
    coverage schedule to the desired numebr of nodes using simulated
    annealing
    '''
    def __init__(self, opt_params, preserve_cc=True,
                 get_new_clique_approach=0, logger=None):
        self.opt_params = opt_params
        self.graph = opt_params.graph
        self.clique_cover = opt_params.clique_cover
        self.num_groups = opt_params.num_groups
        self.obj_funcs = opt_params.objective_functions
        # boolean flag for whether clique cover is immutable in simulated
        # annealing algorithm
        self.preserve_cc = preserve_cc
        # integer representing desired approach for getting a new clique
        # in simulated annealing algorithm
        self.get_new_clique_approach = get_new_clique_approach
        super().__init__(opt_params, logger)

    def process(self, time=90, cont_train=False):
        self._expand_coverage_schedule(time, cont_train)
        self.schedules_df = get_schedules_from_cliques(
            self.opt_params, self.expand_cc_sa_sol)
        self.schedules_cost = process_cost(
            self.opt_params, self.expand_cc_sa_cost)

    def _expand_coverage_schedule(self, sa_time, cont_train):
        self.expand_cc_sa = ExpandCliqueCoverSA(
            self.graph, self.clique_cover, self.num_groups, self.obj_funcs,
            self.preserve_cc, self.get_new_clique_approach, 5, self.logger)
        if cont_train:
            self.logger.info('Continuous training enabled')
            class_name = self.expand_cc_sa.__class__.__name__
            prior_params = load_latest_pckl(
                path1=f'Data/{class_name}/DailyObj')
            if self.expand_cc_sa.params == prior_params:
                self.logger.info(
                    f'OptimizationStrategy1: {class_name} params '\
                    + 'match, continuous training')
                self.expand_cc_sa = load_latest_pckl(
                    path1=f'Data/{class_name}/DailyOpt')
            else:
                self.logger.info(
                    f'OptimizationStrategy1: {class_name} params '\
                    + 'do not match, no continuous training')
            self.logger.info('Prior params:', prior_params)
            self.logger.info('Current params:', self.expand_cc_sa.params)
        else:
            self.logger.info('Continuous training disabled')
        self.expand_cc_sa.anneal(n_iter=MAX_ITERS, time_limit=sa_time)
        if cont_train:
            self.expand_cc_sa.persist()
        self.expand_cc_sa_sol = self.expand_cc_sa.best_solution
        self.expand_cc_sa_cost = self.expand_cc_sa.best_cost
