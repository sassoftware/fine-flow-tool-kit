# flowratio.py

# Copyright © 2023, SAS Institute Inc., Cary, NC, USA.  All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import math
import fineflowevaluation as fine

def computeRatio(bad=0, good=1, batchSize=1):
    """ Computes flow ratio
    Parameters
    ----------
    bad: Number of units of bad flow
    good: Number of units of good flow
    batchSize: Number of units in each batch

    Returns
    -------
    float
        Computed value for flow ratio rounded to 4 decimal places
    """  
    if good!=0:
        ratio = bad/good
    else:
        ratio = math.nan

    if batchSize!=1:
        probGoodBatch = computeProbGood(bad,good)**batchSize
        ratio = (1-probGoodBatch)/probGoodBatch

    return round(ratio, 4)


def computeProbBad(bad=0, good=1):
    """ Computes the probablity of bad flow
    Parameters
    ----------
    bad: Number of units of bad flow
    good: Number of units of good flow

    Returns
    -------
    float
        Computed value for probability of bad flow rounded to 4 decimal places
    """  
    totalFlow = good+bad
    probBad = bad/totalFlow

    return round(probBad, 4)


def computeProbGood(bad=0, good=1):
    """ Computes the probablity of good flow
    Parameters
    ----------
    bad: Number of units of bad flow
    good: Number of units of good flow

    Returns
    -------
    float
        Computed value for probability of good flow rounded to 4 decimal places
    """  
    totalFlow = good+bad
    probGood = good/totalFlow

    return round(probGood, 4)
   

def computeEntropy(bad, good, batchSize, cycles, imps, energy, fixedFlow=False, energyMax=None, drop=False):
    """ Computes flow entropy
    Parameters
    ----------
    bad: Number of units of bad flow
    good: Number of units of good flow
    batchSize: Number of units in each batch
    cycles: Number of cycles over which to compute the results
    imps: Starting value of impedements (I)
    energy: Starting value for energy/cognitive load (E)
    fixedFlow: Boolean that controls of flow should be maintained
    energyMax: Value of maximum energy if capped
    drop: Boolean that controls if flow drop should be output

    Returns
    -------
    dictionary
        Computed flow entropy results for the selected number of cycles
    """
    ratio = computeRatio(bad, good, batchSize)
    result = {}
    result['ratio'] = ratio

    f = fine.compute(imps=imps, energy=energy)['flow']
    i = imps
    e = energy

    fstart = f
    fend = f

    for x in range(1, cycles+1):
        if fixedFlow:
            fineValues = fine.compute(flow=f, imps=i)
            if energyMax!=None:
                e = fineValues['energy']
                if e > energyMax: e = energyMax
                fineValues = fine.compute(imps=i, energy=e)
        else:
            fineValues = fine.compute(imps=i, energy=e)

        result[x] = fineValues
        fend = fineValues['flow']

        i = round((1+ratio)*i, 4)

        if drop:
            result['drop'] = round((fstart-fend)/fstart, 2)
    
    return result


def computeResilience(bad, good, batchSize, imps, energy, energyMax=1):
    """ Computes flow resilience (number of cycles before flow entropy begins)
    Parameters
    ----------
    bad: Number of units of bad flow
    good: Number of units of good flow
    batchSize: Number of units in each batch
    imps: Starting value of impedements (I)
    energy: Starting value for energy/cognitive load (E)
    energyMax: Value of maximum energy if capped

    Returns
    -------
    integer
        Computed resilience for the given inputs
    """    
    ratio = computeRatio(bad, good, batchSize)
    resilience = 0
    i = imps
    f = fine.compute(imps=imps, energy=energy)['flow']

    while resilience<999999999:
        fineValues = fine.compute(flow=f, imps=i)
        if fineValues['energy'] > energyMax: break
        i = (1+ratio)*i
        resilience += 1

    return resilience

    
