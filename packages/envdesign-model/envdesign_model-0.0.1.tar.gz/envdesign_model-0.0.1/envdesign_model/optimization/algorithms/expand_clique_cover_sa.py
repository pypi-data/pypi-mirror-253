# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from envdesign_model.optimization.objective_functions.mean_squared_error\
    import DimensionMSE, RelationshipMSE, CombinationMSE
from envdesign_model.graph_algorithms.build_clique import build_clique
from envdesign_model.optimization.optimization_utils import sort_tuple
from optimizn.combinatorial.simulated_annealing import SimAnnealProblem
from copy import deepcopy
import random
from functools import reduce
from collections import defaultdict


class ExpandCliqueCoverSA(SimAnnealProblem):
    def __init__(self, graph, clique_cover, num_groups, objective_functions,
                 preserve_cc=True, get_new_clique_approach=0,
                 retries_limit=5, logger=None):
        self.graph = graph
        self.clique_cover = clique_cover
        self.num_groups = num_groups
        if len(self.clique_cover) > self.num_groups:
            raise Exception(
                f'Length of minimum clique cover ({len(self.clique_cover)}) '
                + f'exceeds number of groups ({self.num_groups})')
        self.objective_functions = objective_functions
        self.preserve_clique_cover = preserve_cc
        self.get_new_clique_approach = get_new_clique_approach
        self.retries_limit = retries_limit
        self.sol_cost_id = -1  # used for breaking ties when comparing
        # cost tuples (mse, sol_cost_id, dimension mse dict)
        self.vertices = set()
        for clique in self.clique_cover:
            for i in range(len(clique)):
                self.vertices.add(clique[i])
        self.params = {
            'clique_cover': self.clique_cover,
            'num_groups': num_groups,
            'objective_functions': objective_functions,
            'preserve_cc': preserve_cc
        }
        super().__init__(logger)        

    def get_candidate(self):
        init_sol = deepcopy(self.clique_cover)
        for _ in range(self.num_groups - len(init_sol)):
            init_sol.append(random.choice(self.clique_cover))
        return init_sol

    def _meets_coverage(self, sol):
        sol_vertices = set(reduce(lambda c1, c2: set(c1).union(set(c2)), sol,
                                  set()))
        return sol_vertices == self.vertices

    def _get_new_clique(self, clique, override=False):
        if override or self.get_new_clique_approach == 0:
            # pick a random clique from the clique cover, that is not the same
            # as the clique that was removed
            remaining_cliques = list(
                set(self.clique_cover).difference({clique}))
            return random.choice(remaining_cliques)
        elif self.get_new_clique_approach == 1:
            # remove and replace each vertex in the clique, return clique
            # formed by first successful replace, such that the resulting
            # clique is not identical to the one that was removed
            for i in range(len(clique)):
                # remove a vertex from clique
                removed_vert = {clique[i]}
                new_clique = list(clique[:i]) + list(clique[i + 1:])

                # replace with another compatible vertex
                compatible_vertices = None
                for vert in new_clique:
                    neighbors = set(self.graph.adj[vert].keys())
                    if compatible_vertices is None:
                        compatible_vertices = neighbors
                    else:
                        compatible_vertices.intersection_update(neighbors)
                compatible_vertices.difference_update(removed_vert)
                if len(compatible_vertices) != 0:
                    new_clique.append(random.choice(list(compatible_vertices)))
                    return sort_tuple(new_clique)
            
            # no clique found by removing/replacing a single vertex
            return None
        else:
            # for each vertex in the clique, find a clique that covers that
            # vertex that is not the same as the original clique that the
            # vertex was picked from
            for vert in clique:
                neighbors = set(self.graph.adj[vert].keys())
                other_verts = set(clique).difference({vert})
                for other_vert in other_verts:
                    new_clique = build_clique(
                        self.graph, len(clique), {vert}, {other_vert})
                    if new_clique is not None:
                        return sort_tuple(new_clique)
            return None

    def next_candidate(self, sol):
        # if the clique cover and the number of groups is equal, then the
        # solution is unchanged, since the clique cover must be preserved,
        # so return the copy of the solution
        if self.preserve_clique_cover and\
                len(self.clique_cover) > len(sol) - 1:
            return new_sol

        retries_count = 0
        while True:
            new_sol = deepcopy(sol)
            override = retries_count >= self.retries_limit
            if self.preserve_clique_cover:
                # remove a clique, while preserving the clique cover
                clique = new_sol.pop(random.randint(
                    len(self.clique_cover), len(new_sol) - 1))
            
                # add new clique to the clique cover
                new_clique = self._get_new_clique(clique, override)
                if new_clique is not None:
                    new_sol.append(new_clique)
                    break
            else:
                # remove any clique
                clique = new_sol.pop(random.randint(0, len(new_sol) - 1))

                # add new clique to the clique cover
                new_clique = self._get_new_clique(clique, override)
                if new_clique is not None:
                    new_sol.append(new_clique)
                    # check if new solution meets coverage constraint
                    if self._meets_coverage(new_sol):
                        break
            retries_count += 1
        return new_sol
            
    def cost(self, sol):
        # cost is weighted sum of objective functions
        cost = 0
        results = dict()
        if type(self.objective_functions) == CombinationMSE:
            true_vals = defaultdict(int)
            for clique in sol:
                true_vals[clique] += 1
            cost = self.objective_functions.compute(true_vals)
            results = cost
        else: 
            for key, obj_func in self.objective_functions.items():
                if type(obj_func) == DimensionMSE:
                    true_vals = defaultdict(int)
                    for clique in sol:
                        true_vals[clique[key]] += 1
                elif type(obj_func) == RelationshipMSE:
                    true_vals = defaultdict(int)
                    for clique in sol:
                        true_vals[(clique[key[0]], clique[key[1]])] += 1
                cost_val = obj_func.compute(true_vals)
                results[key] = cost_val
                cost += cost_val
        sol_cost_id = self.sol_cost_id + 1
        self.sol_cost_id += 1
        return cost, sol_cost_id, results

    def cost_delta(self, new_cost, current_cost):
        # get difference of total MSEs (across all dimensions)
        return new_cost[0] - current_cost[0]
