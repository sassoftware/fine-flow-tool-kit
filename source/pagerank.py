# pagerank.py

# Copyright © 2023, SAS Institute Inc., Cary, NC, USA.  All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np

def pagerank(M, num_iterations: int = 100, d: float = 0.85, normalize: bool = False):
    """ PageRank Algorithm - adapted from https://en.wikipedia.org/wiki/PageRank#Python
    Parameters
    ----------
    M : numpy array
        adjacency matrix where M_i,j represents the link from 'j' to 'i', such that for all 'j'
        sum(i, M_i,j) = 1
    num_iterations : int, optional
        number of iterations, by default 100
    d : float, optional
        damping factor, by default 0.85

    Returns
    -------
    numpy array
        a vector of ranks such that v_i is the i-th rank from [0, 1],
        v sums to 1

    """
    N = M.shape[1]
    v = np.ones(N) / N
    v_next = v
    M_hat = (d * M + (1 - d) / N)

    for i in range(num_iterations):
        v = v @ M_hat

        #Convergence check - average error of all ranks
        if np.abs(np.average(v - v_next)) < 0.005:
            break
        v_next = v
    
        if i == num_iterations:
           print("WARNING: Convergence not met!")

    if normalize:
        n = np.linalg.norm(v)
        v = v/n

    return v

def classify(v):
    """ classify for computed PageRanks
    Parameters
    ----------
    v : numpy array
        single row matrix of computed ranks as output by PageRank function

    Returns
    -------
    numpy array
        equivalent matrix with input ranks classified high or low (0 or 1)
        high = equal or above 10% higher than median
        low = below 10% higher than median

    """
    c = np.copy(v)
    for i in range(0,len(v)):
        if v[i] < np.median(v)*1.1:
            c[i] = 0
        else:
            c[i] = 1

    return c.astype(int)


def dictToArray(d):
    """ converts a dictionary to numpy array using list comprehension
    Parameters
    ----------
    d : dictionary
        dependency relationship dictionaly in the form: {"A":["B","C"],"B":["C"]}

    Returns
    -------
    numpy array
        adjancy matrix that can be used as input to PageRank function
    """
    vals = d.keys()
    dic = {k: [1 if x in v else 0 for x in vals] for k, v in d.items()}
    lst = list(dic.values())
    return np.array(lst)
