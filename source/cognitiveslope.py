# cognitiveslope.py

# Copyright © 2023, SAS Institute Inc., Cary, NC, USA.  All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
import pagerank as pr
import flowratio as fr
import math

def findCognitiveSlope(teamflow, sum=False, flow=False, imp=False, need=False, energy=True, resilience=False):
    """ Computes the cognitive slope for each node of a given graph.
    Parameters
    ----------
    teamflow : dictionary
        dependency relationship dictionaly in the form: {"A":[("B","C"),("C","F")],"B":[("C","X")],"C":[]}

    Returns
    -------
    dictionary
        dictionary containing congnitive slope value for each team
    """  

    t = dictToArrayTwoSided(teamflow)
    p = pr.pagerank(dictToArray(teamflow, adjMatrix=True), 100, 0.8, normalize=True)

    names = list(teamflow.keys())
    result = {}

    #slopesAve = np.average(t, axis=0)
    slopesSum = np.sum(t, axis=0)
    nonZeroCount = np.count_nonzero(t, axis=0)
    slopesAve = slopesSum / nonZeroCount

    for x in range(0,len(names)):

      #Uses the FINE flow circle equations

        s = slopesSum[x] #slope sum
        e = slopesAve[x] #energy (cog slope average)
        i = p[x] #impedements (page rank)
        f = math.sqrt(e/i) #flow
        n = math.sqrt(e*i) #need
        r = fr.computeResilience(bad=1, good=10, batchSize=1, imps=i, energy=e) #resilience (flowRatio = 0.1)

        tout = list()
        if flow == True:
          tout.append(round(f, 4))
        if imp == True:
          tout.append(round(i, 4))
        if need == True:
          tout.append(round(n, 4))
        if energy == True:
          tout.append(round(e, 4))
        if sum == True:
          tout.append(round(s, 4))
        if resilience == True:
          tout.append(r)

        result[names[x]] = tout

    return result


def dictToArray(d, adjMatrix=False):
    """ converts a dictionary to numpy array representing cognitive slope matrix
    Parameters
    ----------
    d : dictionary
        dependency relationship dictionaly in the form: {"A":[("B","C"),("C","F")],"B":[("C","X")],"C":[]}
    adjMatrix: boolean
        output simple adjacency matrix instead of cognitive slope matrix

    Returns
    -------
    numpy array
        adjancy matrix that can be used as input to findCognitiveSlope function
    """
    matrix = []
    for row_key, row_vals in d.items():
        
        newrow = []
        for col_key in d.keys():

            weight = 0.0
            if row_key == col_key and adjMatrix == False:
              weight = 1.0
            else:
              for pair in row_vals:
                if col_key in pair:
                  if adjMatrix:
                    weight = 1.0
                  elif "X" in pair:
                    weight = 0.75
                  elif "C" in pair:
                    weight = 0.5
                  elif "F" in pair:
                    weight = 0.25

            newrow.append(weight)

        matrix.append(newrow)       
    
    return np.array(matrix)


def dictToArrayTwoSided(d):
  m1 = []
  m2 = []
  
  for row_key, row_vals in d.items():
    r1 = []
    r2 = []
    
    for col_key in d.keys():
      weight = 0.0
      if row_key == col_key:
        weight = 1.0
      else:
        for pair in row_vals:
          if col_key in pair:
            if "X" in pair:
              weight = 0.75
            elif "C" in pair:
              weight = 0.5
            elif "F" in pair:
              weight = 0.25
      
      r1.append(weight)
      if weight>0.0:
        r2.append(1-weight)
      else:
        r2.append(0.0)
    
    m1.append(r1)
    m2.append(r2)
  
  arr1 = np.array(m1)
  arr2 = np.array(m2).transpose()
  
  return np.add(arr1, arr2)

  
  


