# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

from graphing.graph import Graph
from functools import reduce
from copy import deepcopy
import warnings
from envdesign_model.graph_algorithms.build_clique import build_clique


# creating a custom warnings class(es) makes it easier to catch specific
# warnings, if needed in the future
class UncoverableDimensionValuesWarning(Warning):
    def __init__(self, message):
        self.message = message


class GraphAlgorithms:
    def __init__(self, dimension_dicts, relationships_df, num_groups,
                 objective_function, scope_df=None, max_dim_size=100):
        self.dimension_dicts = dimension_dicts
        self.relationships_df = relationships_df
        self.num_groups = num_groups
        self.objective_function = objective_function
        self.clique_size = len(self.dimension_dicts)
        self.scope_df = scope_df
        self.max_dim_size = max_dim_size

    def process(self):
        self._create_dim_mappings()
        self._create_graph()
        self._scope_to_compatible()
        self._remove_uncoverable_vertices()
        self._get_clique_cover()
        self._validate_graph()

    def _create_dim_mappings(self):
        self.dim_name_to_dim_values = dict()
        self.dim_value_to_int = dict()
        self.int_to_dim_value = dict()
        self.dim_name_to_ints = dict()
        self.int_to_dim_name = dict()
        val_int = 0
        for dim_dict in self.dimension_dicts:
            dim_values = dim_dict['df'][dim_dict['value']].values
            dim_name = dim_dict['name']
            self.dim_name_to_dim_values[dim_name] = set(dim_values)
            self.dim_name_to_ints[dim_name] = set()
            for dim_val in dim_values:
                if dim_val == '<ANY>':
                    raise Exception('Dimension value cannot be <ANY>')
                self.dim_value_to_int[dim_val] = val_int
                self.int_to_dim_value[val_int] = dim_val
                self.dim_name_to_ints[dim_name].add(val_int)
                self.int_to_dim_name[val_int] = dim_name
                val_int += 1

    def _create_graph(self):
        # get graph edges, create graph from relationships dataframe
        # and dimension value mappings
        edges = set()
        for _, relationship in self.relationships_df.iterrows():
            dimension1 = relationship['Dimension1']
            value1 = relationship['Value1']
            dimension2 = relationship['Dimension2']
            value2 = relationship['Value2']
            if value1 == '<ANY>' and value2 != '<ANY>':
                for dim1_value in self.dim_name_to_dim_values[dimension1]:
                    dim1_int = self.dim_value_to_int[dim1_value]
                    dim2_int = self.dim_value_to_int[value2]
                    edges.add((dim1_int, dim2_int))
                    edges.add((dim2_int, dim1_int))
            elif value1 != '<ANY>' and value2 == '<ANY>':
                for dim2_value in self.dim_name_to_dim_values[dimension2]:
                    dim1_int = self.dim_value_to_int[value1]
                    dim2_int = self.dim_value_to_int[dim2_value]
                    edges.add((dim1_int, dim2_int))
                    edges.add((dim2_int, dim1_int))
            elif value1 == '<ANY>' and value2 == '<ANY>':
                for dim1_value in self.dim_name_to_dim_values[dimension1]:
                    for dim2_value in self.dim_name_to_dim_values[
                            dimension2]:
                        dim1_int = self.dim_value_to_int[dim1_value]
                        dim2_int = self.dim_value_to_int[dim2_value]
                        edges.add((dim1_int, dim2_int))
                        edges.add((dim2_int, dim1_int))
            else:
                dim1_int = self.dim_value_to_int[value1]
                dim2_int = self.dim_value_to_int[value2]
                edges.add((dim1_int, dim2_int))
                edges.add((dim2_int, dim1_int))
        self.graph = Graph(edges)
    
    def _scope_to_compatible(self):
        if self.scope_df is None or len(self.scope_df) == 0:
            return
        
        # get vertices corresponding to scope function
        vertices = set(self.graph.vert_props.keys())
        scope_values = set(
            self.scope_df[self.scope_df['Status'] == 'Include']['Value'])
        scope_vertices = set()
        for vertex in vertices:
            dim_value = self.int_to_dim_value[vertex]
            if dim_value in scope_values:
                scope_vertices.add(vertex)
        if len(scope_vertices) == 0:
            return
        
        # get non-scope vertices that do not have edges to scope vertices
        remove_verts = set()
        for vertex in vertices.difference(scope_vertices):
            neighbors = set(self.graph.adj[vertex].keys())
            scope_neighbors = neighbors.intersection(scope_vertices)
            if len(scope_neighbors) == 0:
                remove_verts.add(vertex)

        # remove corresponding dimension values
        vals_to_remove = set(map(lambda v: self.int_to_dim_value[v],
                                 remove_verts))
        self._remove_dim_values(vals_to_remove)
    
    def _remove_uncoverable_vertices(self):
        # remove the vertices that do not have edges connecting them to
        # all the other dimensions in the graph
        removed_scope_vals = dict()
        if self.scope_df is None or len(self.scope_df) == 0:
            scope_vals = set()
        else:
            scope_vals = set(
                self.scope_df[self.scope_df['Status'] == 'Include']['Value'])
        keep_removing = True
        while keep_removing:
            vertices = set(self.graph.vert_props.keys())
            dim_names = set(map(lambda d: d['name'], self.dimension_dicts))
            vals_to_remove = set()
            for vert in vertices:
                dim_name = self.int_to_dim_name[vert]
                neighbors = set(self.graph.adj[vert].keys())
                for other_dim in dim_names:
                    if other_dim == dim_name:
                        continue
                    other_dim_verts = self.dim_name_to_ints[other_dim]
                    neighbors_in_dim = neighbors.intersection(other_dim_verts)
                    edge_to_dim_present = False
                    for neighbor in neighbors_in_dim:
                        if neighbor in other_dim_verts:
                            edge_to_dim_present = True
                            break
                    if not edge_to_dim_present:
                        dim_val = self.int_to_dim_value[vert]
                        vals_to_remove.add(dim_val)
                        if dim_val in scope_vals:
                            removed_scope_vals[dim_val] = other_dim
                        break
            if len(vals_to_remove) == 0:
                keep_removing = False
            else:
                self._remove_dim_values(vals_to_remove)
        if len(removed_scope_vals) != 0:
            raise Exception(
                'The following scope values do not have any relationships '
                + 'with at least one dimension (key: scope value, value: '
                + 'dimension it has no relationships with): '
                + f'{removed_scope_vals}')

    def _clique_cover_vertices(self, vertices, limit_clique_cover_size=False):
        # generate a clique to cover each vertex, if it has not already
        # been covered
        for vertex in vertices:
            # check if clique cover size limit was reached
            if limit_clique_cover_size and len(self.clique_cover) >=\
                    self.num_groups:
                break

            # check if vertex has already been covered
            if vertex in self.clique_covered_vertices:
                continue
            
            # build a clique of the desired size that covers the vertex
            clique = build_clique(
                self.graph, self.clique_size, {vertex},
                covered_vertices=self.clique_covered_vertices)
            if clique is not None:
                self.clique_cover.append(clique)
                self.clique_covered_vertices =\
                    self.clique_covered_vertices.union(clique)

    def _get_clique_cover(self):
        # initialize sets of vertices, covered vertices, and cliques
        vertices = set(self.graph.vert_props.keys())
        self.clique_covered_vertices = set()
        self.clique_cover = list()

        # generate clique covers
        if self.scope_df is None or len(self.scope_df) == 0:
            self._clique_cover_vertices(vertices)
        else:
            # separate vertices that are in scope data and vertices that are
            # not in scope data
            scope_values = set(
                self.scope_df[self.scope_df['Status'] == 'Include']['Value'])
            scope_vertices = set()
            non_scope_vertices = set()
            for vertex in vertices:
                dim_value = self.int_to_dim_value[vertex]
                if dim_value in scope_values:
                    scope_vertices.add(vertex)
                else:
                    non_scope_vertices.add(vertex)
            
            # get clique cover for scope vertices
            self._clique_cover_vertices(scope_vertices)

            # restrict dimension value size while retaining clique cover
            # vertices
            dim_vals_to_remove = set()
            for dim_dict in self.dimension_dicts:
                dim_df = dim_dict['df']
                dim_vals = set(dim_df[dim_dict['value']])

                # get dimension values in dimension that are in clique cover
                dim_cc_vals = set(
                    filter(lambda v: self.dim_value_to_int[v] in
                           self.clique_covered_vertices, dim_vals))
                
                # get top remaining dimension values by score
                rem_dim_vals = set(dim_df[
                    ~dim_df[dim_dict['value']].isin(dim_cc_vals)].nlargest(
                    self.max_dim_size - len(dim_cc_vals), 'Score')
                    [dim_dict['value']])

                # add dimension values not in union of above 2 sets to
                # dim_vals_to_remove
                retain_dim_vals = dim_cc_vals.union(rem_dim_vals)
                dim_vals_to_remove = dim_vals_to_remove.union(
                    set(filter(lambda v: v not in retain_dim_vals, dim_vals)))

            # remove dimension values
            self._remove_dim_values(dim_vals_to_remove)

            # get clique cover for vertices not covered by clique cover
            non_cc_verts = set()
            for dim_dict in self.dimension_dicts:
                dim_vals = set(dim_dict['df'][dim_dict['value']])
                dim_val_ints = set(map(
                    lambda v: self.dim_value_to_int[v], dim_vals))
                non_cc_verts = non_cc_verts.union(
                    dim_val_ints.difference(self.clique_covered_vertices))
            self._clique_cover_vertices(
                non_cc_verts, limit_clique_cover_size=True)
    
    def _remove_dim_values(self, vals_to_remove):
        # get integers corresponding to dimension values to remove
        val_ints_to_remove = set(map(lambda v: self.dim_value_to_int[v],
                                     vals_to_remove))

        # remove uncoverable vertices not in scope data from graph
        self.graph.remove_vertices(val_ints_to_remove)

        # remove uncoverable vertices not in scope data from dimension dicts
        processed_dim_dicts = []
        for dim_dict in self.dimension_dicts:
            processed_dim_dict = deepcopy(dim_dict)
            processed_dim_dict['df'] = processed_dim_dict['df'][
                (~processed_dim_dict['df'][processed_dim_dict['value']]
                 .isin(vals_to_remove))
            ]
            processed_dim_dicts.append(processed_dim_dict)
        self.dimension_dicts = processed_dim_dicts

        # remove uncoverable vertices not in scope data from relationships
        # DataFrame
        self.relationships_df = self.relationships_df[
            (~self.relationships_df['Value1'].isin(vals_to_remove))
            & (~self.relationships_df['Value2'].isin(vals_to_remove))
        ]

        # remove uncoverable vertices not in scope data from dimension name to
        # dimension values mapping
        filtered_dim_name_to_dim_vals = dict()
        for dim_name, dim_vals in self.dim_name_to_dim_values.items():
            filtered_dim_name_to_dim_vals[dim_name] = set(
                filter(lambda v: v not in vals_to_remove, dim_vals))
        self.dim_name_to_dim_values = filtered_dim_name_to_dim_vals

        # remove uncoverable vertices not in scope data from dimension value to
        # dimension value integer mapping
        filtered_dim_val_to_int = dict()
        for dim_val, dim_int in self.dim_value_to_int.items():
            if dim_val not in vals_to_remove and dim_int not in\
                    val_ints_to_remove:
                filtered_dim_val_to_int[dim_val] = dim_int
        self.dim_value_to_int = filtered_dim_val_to_int

        # remove uncoverable vertices not in scope data from dimension value
        # integer to dimension value mapping
        filtered_int_to_dim_val = dict()
        for dim_int, dim_val in self.int_to_dim_value.items():
            if dim_val not in vals_to_remove and dim_int not in\
                    val_ints_to_remove:
                filtered_int_to_dim_val[dim_int] = dim_val
        self.int_to_dim_value = filtered_int_to_dim_val

        # if objective function is combination based, remove combinations that
        # contain uncoverable vertices not in scope data
        if self.objective_function['type'] == 'combination':
            for i in range(len(self.objective_function['specifics'])):
                spec = self.objective_function['specifics'][i]
                combinations = spec['combinations']
                valid_combinations = []
                for combo_info in combinations:                    
                    # check that each dimension value is valid
                    valid_combo = True
                    for dim_val in combo_info['combination']:
                        dimension = dim_val['dimension']
                        value = dim_val['value']
                        if value != '<ANY>' and value not in\
                                self.dim_name_to_dim_values[dimension]:
                            valid_combo=False
                            break
                    if valid_combo:
                        valid_combinations.append(combo_info)
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

    def _validate_graph(self):
        # check that clique cover is not empty
        if len(self.clique_cover) == 0:
            raise Exception(
                'All dimension values are uncoverable under the given '
                + 'scope data, dimension dictionaries, and relationships')
        
        # check that length of clique cover does not exceed number of groups
        if len(self.clique_cover) > self.num_groups:
            raise Exception(
                f'Length of minimum clique cover ({len(self.clique_cover)}) '
                + f'exceeds number of groups ({self.num_groups})')

        # check if vertices are covered by cliques
        # if scope data is provided, only check if there are dimension
        # values in scope data that are not covered, otherwise check
        # all dimension values
        vertices = set(
            reduce(lambda s, e: s.union({e[0], e[1]}), self.graph.edges,
                   set()))
        uncoverable_dim_value_ints = vertices.difference(
            self.clique_covered_vertices)
        uncoverable_dim_values = set(map(lambda i: self.int_to_dim_value[i],
                                         uncoverable_dim_value_ints))
        if self.scope_df is not None and len(self.scope_df) != 0:
            scope_values = set(
                self.scope_df[self.scope_df['Status'] == 'Include']
                ['Value'])
            uncoverable_scope_values = uncoverable_dim_values.intersection(
                scope_values)
            if len(uncoverable_scope_values) > 0:
                raise Exception(
                    'The following dimension values (in scope data) cannot be '
                    + 'covered under the given relationships: '
                    + f'{uncoverable_scope_values}')
        else:
            if len(uncoverable_dim_values) > 0:
                warnings.warn('The following dimension values cannot be '
                    + 'covered under the given relationships: '
                    + f'{uncoverable_dim_values}',
                    UncoverableDimensionValuesWarning)
        
        # remove uncoverable dimension values
        self._remove_dim_values(uncoverable_dim_values)
