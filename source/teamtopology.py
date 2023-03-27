# teamtopology.py

# Copyright © 2023, SAS Institute Inc., Cary, NC, USA.  All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

from unittest import case
import numpy as np
import pagerank as pr
import betweenness as bt

def findTopology(teamflow, classifiers=False, centralities=False, extended=True):
    """ Team Topology Finder - performs team topology analysis from flow of value between teams
    
    Parameters
    ----------
    teamflow : dictionary
        desciption of value flow between teams in the form:

        {'teamA': ['teamB','teamC'],
         'teamB': [],
         'teamC': ['TeamB']}

        in the above example: teamA gets value from teamB and teamC
                              teamB gets no value from the other teams (must be included)
                              teamC gets value only from teamC

    classifiers : True/False
        include classifier values in the output
    
    centralities: True/False
        include centrality scores for betweenness and page rank in the output

    extended: True/False
        perform extended checks for classifications of SA and EN teams by final examination of vertex degree (inbound/outbound edges)

    Returns
    -------
    dictionary
        a dictionary containing the team topology analysis in the form:

        {'team_1':  [<betweenness>, <pageRank>, <betweenness_classifier>, <pageRank_classifier>, 'team_type'],
          ...,
         'team_n':  [<betweenness>, <pageRank>, <betweenness_classifier>, <pageRank_classifier>, 'team_type']}

        Notes:
            betweenness and pageRank (optional) are floating point numbers
            classifiers (optional) are 0 or 1
            team_type is one of: SA, EN, CS or PF.

    """
    t = pr.dictToArray(teamflow)
    
    betweenness = bt.betweenness(t)
    pagerank = pr.pagerank(t, d=0.8, normalize=True)
    classified_betweenness = bt.classify(betweenness)
    classified_pagerank = pr.classify(pagerank)
    
    names = list(teamflow.keys())
    result = {}

    for i in range(0,len(names)):
        tout = list()

        #select team type from classification quadrant
        type = ("SA","EN","CS","PF")[classified_betweenness[i]*2 + classified_pagerank[i]]

        #unless disabled, perform extended degree checks for SA teams
        if extended and type == "SA":
            #convert to EN if no outbound edges present (degree_out = 0)
            if np.sum(t, axis=1)[i] == 0:
                type = "EN"
                classified_pagerank[i] = 1

            #convert to CS if both inbound and outbound edges present (degree in/out > 0)
            if np.sum(t, axis=1)[i] > 0 and np.sum(t, axis=0)[i] > 0:
                type = "CS"
                classified_betweenness[i] = 1
        
        #unless disabled, perform extended degree checks for EN teams
        if extended and type == "EN":
            #convert to PF if one or more outbount edge present (degree out > 0)
            if np.sum(t, axis=1)[i] > 0:
                type = "PF"
                classified_betweenness[i] = 1

        #if requested, output centralities
        if centralities:
            tout.append(round(betweenness[i], 4))
            tout.append(round(pagerank[i], 4))    

        #if requested, output classifiers
        if classifiers:
            tout.append(classified_betweenness[i])
            tout.append(classified_pagerank[i])

        tout.append(type)

        result[names[i]] = tout

    return result
