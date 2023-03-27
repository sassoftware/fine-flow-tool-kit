# fineflowevaluation.py

# Copyright © 2023, SAS Institute Inc., Cary, NC, USA.  All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import cognitiveslope as cs
import math

def evaluate(teamflow, sum=False, flow=False, imp=False, need=False, energy=True, resilience=False):
    """ Computes the FINE flow values using cognitive slope.
    Parameters
    ----------
    teamflow : dictionary
        dependency relationship dictionaly in the form: {"A":[("B","C"),("C","F")],"B":[("C","X")],"C":[]}

    Returns
    -------
    dictionary
        dictionary containing FINE flow values for the selected outputs
    """  
    return cs.findCognitiveSlope(teamflow, sum, flow, imp, need, energy, resilience)


def compute(flow=None, imps=None, need=None, energy=None):
    """ Implements the FINE flow relationships - requires at least two inputs to deliver the FINE set. 
    Parameters
    ----------
    flow: Value for flow (F)
    imps: Value for Impediments (I)
    need: Value for need (N)
    energy: Value enery/cognitive load (E)

    Returns
    -------
    dictionary
        dictionary containing the set of FINE flow values for the given inputs.
    """  
    if flow!=None and imps!=None:
        if need==None: need = flow * imps
        if energy==None: energy = (need**2)/imps

    if flow!=None and need!=None:
        if imps==None: imps = need/flow
        if energy==None: energy = need * flow

    if flow!=None and energy!=None:
        if imps==None: imps = energy/(flow**2)
        if need==None: need = energy/flow

    if imps!=None and need!=None:
        if flow==None: flow = need/imps
        if energy==None: energy = (need**2)/imps

    if imps!=None and energy!=None:
        if flow==None: flow = math.sqrt(energy/imps)
        if need==None: need = math.sqrt(energy*imps)

    if need!=None and energy!=None:
        if flow==None: flow = energy/need
        if imps==None: imps = (need**2)/energy

    if flow!=None and imps!=None and need!=None and energy!=None:
        result = {'flow'  : round(flow,4),
                  'imps'  : round(imps,4),
                  'need'  : round(need,4),
                  'energy': round(energy,4)}
    else:
        result = {'error' : 'Too few values, must have least two inputs'}
    
    return result

