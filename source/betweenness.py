# betweenness.py

# Copyright © 2023, SAS Institute Inc., Cary, NC, USA.  All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
import networkx as nx

def betweenness(M):
    """ Betweenness Algorithm - uses networkx library: https://networkx.org/documentation/stable/reference/algorithms/centrality.html
    Parameters
    ----------
    M : numpy array
        adjacency matrix where M_i,j represents the link from 'j' to 'i', such that for all 'j'
        sum(i, M_i,j) = 1

    Returns
    -------
    numpy array
        a vector of betweenness scores for each vertex of the graph
    """
    G = nx.from_numpy_array(M, create_using=nx.DiGraph)
    bc = nx.betweenness_centrality(G)
    lst = list(bc.values())
    return np.array(lst)

def classify(v):
    """ classify for computed Betweenness scores
    Parameters
    ----------
    v : numpy array
        single row matrix of computed scores as output by Betweenness function

    Returns
    -------
    numpy array
        equivalent matrix with input ranks classified high or low (0 or 1)
        high = above zero
        low = equals zero

    """
    c = np.copy(v)
    for i in range(0,len(v)):
        if v[i] > 0:
            c[i] = 1
        else:
            c[i] = 0

    return c.astype(int)
