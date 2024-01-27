# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.


def build_clique(graph, clique_size, init_clique, exclude_vertices=set(),
                 covered_vertices=None):
    # initial clique cannot be None or empty
    if init_clique is None or len(init_clique) == 0:
        raise Exception('Initial clique cannot be None or empty')

    # initial clique cannot be larger than clique size
    if len(init_clique) > clique_size:
        raise Exception(
            f'Initial clique {init_clique} has size {len(init_clique)}, '
            + f'must have size less than or equal to {clique_size}')
    
    # initial clique cannot have overlap with exclude vertices set
    overlap = init_clique.intersection(exclude_vertices)
    if len(overlap) != 0:
        raise Exception(
            'Initial clique contains vertices in exclude vertices set '
            + f'({overlap})')

    # determine which vertices share edges with all vertices in the
    # initial clique
    allowed_vertices = None
    for vert in init_clique:
        neighbors = set(graph.adj[vert].keys())
        if allowed_vertices is None:
            allowed_vertices = neighbors
        else:
            allowed_vertices.intersection_update(neighbors)
    allowed_vertices.difference_update(exclude_vertices)

    # build clique to the desired size
    return _build_clique(graph, clique_size, init_clique,
                         allowed_vertices, covered_vertices)


def _build_clique(graph, clique_size, clique, allowed_vertices,
                  covered_vertices=None):
    '''
    This algorithm is adapted from a modified version of the Bron-Kerbosch
    algorithm (Tomita) presented in source (1).

    Source:

    (1)
    Title: Review of the Bron-Kerbosch algorithm and variations
    Author: Alessio Conte
    URL: https://www.dcs.gla.ac.uk/~pat/jchoco/clique/enumeration/tex/report.pdf
    Date published: May 5, 2013
    Date accessed: November 30, 2023
    '''

    # check if clique has been formed or if forming a clique is impossible
    if len(clique) == clique_size:
        return clique
    elif len(clique) + len(allowed_vertices) < clique_size:
        return None
    
    # remove neighbors of vertex with most neighbors in the set of allowed
    # vertices (pivot vertex), to reduce computational branches
    pivot_vertex_allowed_neighbors = None
    for vertex in allowed_vertices:
        neighbors = set(graph.adj[vertex].keys()).intersection(
            allowed_vertices)
        if pivot_vertex_allowed_neighbors is None or len(neighbors) < len(
                pivot_vertex_allowed_neighbors):
            pivot_vertex_allowed_neighbors = neighbors
    reduced_allowed_vertices = allowed_vertices.difference(
        pivot_vertex_allowed_neighbors)
    
    # consider neighbors that have not been covered by cliques yet before
    # those that have already been covered by cliques
    if covered_vertices is not None:
        reduced_allowed_uncovered_vertices = list(
            reduced_allowed_vertices.difference(
            covered_vertices))
        reduced_allowed_covered_vertices = list(
            reduced_allowed_vertices.intersection(
            covered_vertices))
        reduced_allowed_vertices_ordered = reduced_allowed_uncovered_vertices\
            + reduced_allowed_covered_vertices
    else:
        reduced_allowed_vertices_ordered = list(reduced_allowed_vertices)

    # continue building clique
    for vertex in reduced_allowed_vertices_ordered:
        complete_clique = _build_clique(
            graph, clique_size, clique.union({vertex}),
            allowed_vertices.intersection(set(graph.adj[vertex].keys())),
            covered_vertices)
        if complete_clique is not None:
            return complete_clique
    
    # no complete clique found
    return None
