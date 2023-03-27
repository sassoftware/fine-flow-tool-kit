# test_BakersUnlimited.py

# Copyright © 2023, SAS Institute Inc., Cary, NC, USA.  All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import unittest
import teamtopology as tt
import fineflowevaluation as fine
import flowratio as fr


class TestBakersUnlimited(unittest.TestCase):

    def setUp(self):

        #Team flow for Bakers Unlimited Example
        self.BU_TeamFlow = {'StoreRO':  ['CRM', 'QE', 'DataEC'],
                            'OnlineRO': ['CRM', 'UX', 'QE', 'DataEC'],
                            'CRM':      ['DataEC', 'CloudES'],
                            'UX':       [],
                            'QE':       [],
                            'DataEC':   ['QE', 'CloudES'],
                            'CloudES':  ['QE']
        }

        #Team flow for Bakers Unlimited Example with interactions
        self.BU_TeamFlowWithInteractions = {'StoreRO':  [('CRM', 'C'), ('QE', 'F'), ('DataEC', 'X')],
                                            'OnlineRO': [('CRM', 'C'), ('UX', 'F'), ('QE', 'F'), ('DataEC', 'X')],
                                            'CRM':      [('DataEC', 'X'), ('CloudES', 'X')],
                                            'UX':       [],
                                            'QE':       [],
                                            'DataEC':   [('QE', 'F'), ('CloudES', 'X')],
                                            'CloudES':  [('QE', 'F')]
        }

        #Team flow for Bakers Unlimited Example focused on Value Stream Map for OnlineRO 
        self.BU_TeamFlowOnlineRO = {'OnlineRO': [('UX', 'F'), ('QE', 'F'), ('DataEC', 'X')],
                                    'UX':       [],
                                    'QE':       [],
                                    'DataEC':   [('QE', 'F'), ('CloudES', 'X')],
                                    'CloudES':  [('QE', 'F')]
        }


        #Team flow for Bakers Unlimited Example focused on Value Stream Map for OnlineRO with QE team using x-as-a-service
        self.BU_TeamFlowOnlineROWithQEX = {'OnlineRO':    [('UX', 'F'), ('QE', 'X'), ('DataEC', 'X')],
                                           'UX':          [],
                                           'QE':          [],
                                           'DataEC':      [('QE', 'X'), ('CloudES', 'X')],
                                           'CloudES':     [('QE', 'X')]
        }

        #Team flow for Bakers Unlimited Example with interactions with QE team using x-as-a-service
        self.BU_TeamFlowWithInteractionsWithQEX = {'StoreRO':  [('CRM', 'C'), ('QE', 'X'), ('DataEC', 'X')],
                                                   'OnlineRO': [('CRM', 'C'), ('UX', 'F'), ('QE', 'X'), ('DataEC', 'X')],
                                                   'CRM':      [('DataEC', 'X'), ('CloudES', 'X')],
                                                   'UX':       [],
                                                   'QE':       [],
                                                   'DataEC':   [('QE', 'X'), ('CloudES', 'X')],
                                                   'CloudES':  [('QE', 'X')]
        }

        #Team flow for Bakers Unlimited Example with interactions
        self.BU_TeamFlowWithEmbeddedQE =   {'StoreRO':     [('CRM', 'C'), ('QE', 'F'), ('DataEC', 'X')],
                                            'OnlineRO':    [('CRM', 'C'), ('UX', 'F'), ('OnlineRO_QE', 'F'), ('DataEC', 'X')],
                                            'OnlineRO_QE': [('QE', 'C')],
                                            'CRM':         [('DataEC', 'X'), ('CloudES', 'X')],
                                            'UX':          [],
                                            'QE':          [],
                                            'DataEC':      [('QE', 'F'), ('CloudES', 'X')],
                                            'CloudES':     [('QE', 'F')]
        }

        #Team flow for Bakers Unlimited Example with interactions
        self.BU_TeamFlowWithEmbeddedQE_AllF =   {'StoreRO': [('CRM', 'C'), ('QE', 'F'), ('DataEC', 'X')],
                                            'OnlineRO':    [('CRM', 'C'), ('UX', 'F'), ('OnlineRO_QE', 'F'), ('DataEC', 'X')],
                                            'OnlineRO_QE': [('QE', 'F')],
                                            'CRM':         [('DataEC', 'X'), ('CloudES', 'X')],
                                            'UX':          [],
                                            'QE':          [],
                                            'DataEC':      [('QE', 'F'), ('CloudES', 'X')],
                                            'CloudES':     [('QE', 'F')]
        }


    def test_whenGivenBUTeamFlowThenTopologyIsAsExpected(self):

        ttopology = tt.findTopology(self.BU_TeamFlow)

        expected = {'StoreRO':  ['SA'],
                    'OnlineRO': ['SA'],
                    'CRM':      ['CS'],
                    'UX':       ['EN'],
                    'QE':       ['EN'],
                    'DataEC':   ['PF'],
                    'CloudES':  ['PF']
                    }

        if ttopology != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', ttopology)

        assert ttopology == expected


    def test_whenGivenBUExampleThenValuesAreAsExpected(self):

        ttopology = fine.evaluate(self.BU_TeamFlowWithInteractions, flow=True, imp=True, need=True, energy=True, resilience=True)

                                #flow    #imps   #need   #energy #resilience
        expected = {'StoreRO':  [3.2313, 0.0599, 0.1934, 0.625,  5 ],
                    'OnlineRO': [3.2953, 0.0599, 0.1973, 0.65,   5 ],
                    'CRM':      [1.7555, 0.1622, 0.2848, 0.5,    8 ],
                    'UX':       [2.3723, 0.1111, 0.2635, 0.625,  5 ],
                    'QE':       [0.7029, 0.8097, 0.5691, 0.4,    10],
                    'DataEC':   [1.534, 0.301, 0.4617, 0.7083,   4 ],
                    'CloudES':  [1.3348, 0.456, 0.6087, 0.8125,  3 ]}

        if ttopology != expected:
            print('\n01: Unexpected result! \nExpected:', expected, '\nInstead :', ttopology)

        assert ttopology == expected


    def test_whenGivenBUExampleWithCappedEnergyThenFlowDecreasesAsExpected(self):

        flowEntropy = fr.computeEntropy(bad=1, good=10, batchSize=1, cycles=10, imps=0.0599, energy=0.625, fixedFlow=True, energyMax=1)

        expected = {'ratio': 0.1,
                     1: {'flow': 3.2302, 'imps': 0.0599, 'need': 0.1935, 'energy': 0.625},
                     2: {'flow': 3.2302, 'imps': 0.0659, 'need': 0.2129, 'energy': 0.6876},
                     3: {'flow': 3.2302, 'imps': 0.0725, 'need': 0.2342, 'energy': 0.7565},
                     4: {'flow': 3.2301, 'imps': 0.0798, 'need': 0.2578, 'energy': 0.8326},
                     5: {'flow': 3.2302, 'imps': 0.0878, 'need': 0.2836, 'energy': 0.9161},
                     6: {'flow': 3.2174, 'imps': 0.0966, 'need': 0.3108, 'energy': 1},
                     7: {'flow': 3.0671, 'imps': 0.1063, 'need': 0.326,  'energy': 1},
                     8: {'flow': 2.9248, 'imps': 0.1169, 'need': 0.3419, 'energy': 1},
                     9: {'flow': 2.7886, 'imps': 0.1286, 'need': 0.3586, 'energy': 1},
                    10: {'flow': 2.6584, 'imps': 0.1415, 'need': 0.3762, 'energy': 1}}

        if flowEntropy != expected:
            print('\n07: Unexpected result! \nExpected:', expected, '\nInstead :', flowEntropy)

        assert flowEntropy == expected


    def test_whenGivenOnlineROExampleFlowAndInteractionsThenValuesAreAsExpected(self):

        ttopology = fine.evaluate(self.BU_TeamFlowOnlineRO, flow=True, imp=True, need=True, energy=True, resilience=True)

                                 #flow    #imps   #need   #energy #resilience
        expected = {'OnlineRO':  [2.5985, 0.1018, 0.2646, 0.6875, 4],
                    'UX':        [1.69,   0.2188, 0.3698, 0.625,  5],
                    'QE':        [0.7063, 0.8769, 0.6194, 0.4375, 9],
                    'DataEC':    [1.7724, 0.2188, 0.3879, 0.6875, 4],
                    'CloudES':   [1.5355, 0.3534, 0.5427, 0.8333, 2]}

        if ttopology != expected:
            print('\n02: Unexpected result! \nExpected:', expected, '\nInstead :', ttopology)

        assert ttopology == expected


    def test_whenGivenOnlineROExampleWithQEXThenValuesAreAsExpected(self):

        ttopology = fine.evaluate(self.BU_TeamFlowOnlineROWithQEX, flow=True, imp=True, need=True, energy=True, resilience=True)

                                #flow    #imps   #need   #energy #resilience 
        expected = {'OnlineRO': [2.3504, 0.1018, 0.2393, 0.5625, 7],
                    'UX':       [1.69,   0.2188, 0.3698, 0.625,  5],
                    'QE':       [0.9626, 0.8769, 0.8441, 0.8125, 3],
                    'DataEC':   [1.6032, 0.2188, 0.3509, 0.5625, 7],
                    'CloudES':  [1.3734, 0.3534, 0.4854, 0.6667, 5]}

        if ttopology != expected:
            print('\n03: Unexpected result! \nExpected:', expected, '\nInstead :', ttopology)

        assert ttopology == expected


    def test_whenGivenBUExampleWithQEXThenValuesAreAsExpected(self):

        ttopology = fine.evaluate(self.BU_TeamFlowWithInteractionsWithQEX, flow=True, imp=True, need=True, energy=True, resilience=True)

                                #flow    #imps   #need   #energy #resilience
        expected = {'StoreRO':  [2.8902, 0.0599, 0.173,  0.5,    8],
                    'OnlineRO': [3.0312, 0.0599, 0.1814, 0.55,   7],
                    'CRM':      [1.7555, 0.1622, 0.2848, 0.5,    8],
                    'UX':       [2.3723, 0.1111, 0.2635, 0.625,  5],
                    'QE':       [0.994,  0.8097, 0.8048, 0.8,    3],
                    'DataEC':   [1.441,  0.301,  0.4337, 0.625,  5],
                    'CloudES':  [1.2278, 0.456,  0.5599, 0.6875, 4]}

        if ttopology != expected:
            print('\n04: Unexpected result! \nExpected:', expected, '\nInstead :', ttopology)

        assert ttopology == expected


    def test_whenGivenBUExampleWithEmbededQEThenValuesAreAsExpected(self):

        ttopology = fine.evaluate(self.BU_TeamFlowWithEmbeddedQE, flow=True, imp=True, need=True, energy=True, resilience=True)

                                   #flow    #imps   #need   #energy #resilience
        expected = {'StoreRO':     [3.3698, 0.055,  0.1855, 0.625,  5],
                    'OnlineRO':    [3.4366, 0.055,  0.1891, 0.65,   5],
                    'OnlineRO_QE': [2.3773, 0.1032, 0.2454, 0.5833, 6],
                    'CRM':         [1.8173, 0.1514, 0.2751, 0.5,    8],
                    'UX':          [2.4607, 0.1032, 0.254,  0.625,  5],
                    'QE':          [0.739,  0.8239, 0.6089, 0.45,   9],
                    'DataEC':      [1.5795, 0.2839, 0.4485, 0.7083, 4],
                    'CloudES':     [1.3649, 0.4361, 0.5953, 0.8125, 3]}

        if ttopology != expected:
            print('\n05: Unexpected result! \nExpected:', expected, '\nInstead :', ttopology)

        assert ttopology == expected


    def test_whenGivenBUExampleWithEmbededQE_AllFThenValuesAreAsExpected(self):

        ttopology = fine.evaluate(self.BU_TeamFlowWithEmbeddedQE_AllF, flow=True, imp=True, need=True, energy=True, resilience=True)

                                   #flow    #imps   #need   #energy #resilience
        expected = {'StoreRO':     [3.3698, 0.055,  0.1855, 0.625,  5 ],
                    'OnlineRO':    [3.4366, 0.055,  0.1891, 0.65,   5 ],
                    'OnlineRO_QE': [2.5414, 0.1032, 0.2623, 0.6667, 5 ],
                    'CRM':         [1.8173, 0.1514, 0.2751, 0.5,    8 ],
                    'UX':          [2.4607, 0.1032, 0.254,  0.625,  5 ],
                    'QE':          [0.6968, 0.8239, 0.5741, 0.4,    10],
                    'DataEC':      [1.5795, 0.2839, 0.4485, 0.7083, 4 ],
                    'CloudES':     [1.3649, 0.4361, 0.5953, 0.8125, 3 ]}

        if ttopology != expected:
            print('\n06: Unexpected result! \nExpected:', expected, '\nInstead :', ttopology)

        assert ttopology == expected


    def test_whenGivenFlowMetricsForOnlineROTeamWithCappedEnergyThenFlowDecreasesAsExpected(self):

        flowEntropy = fr.computeEntropy(bad=1, good=10, batchSize=1, cycles=10, imps=0.055, energy=0.65, fixedFlow=True, energyMax=1)

        expected = {'ratio': 0.1,
                    1:  {'flow': 3.4378, 'imps': 0.055,  'need': 0.1891, 'energy': 0.65},
                    2:  {'flow': 3.4378, 'imps': 0.0605, 'need': 0.208,  'energy': 0.715},
                    3:  {'flow': 3.4377, 'imps': 0.0665, 'need': 0.2286, 'energy': 0.7859},
                    4:  {'flow': 3.4378, 'imps': 0.0732, 'need': 0.2516, 'energy': 0.8651},
                    5:  {'flow': 3.4378, 'imps': 0.0805, 'need': 0.2767, 'energy': 0.9514},
                    6:  {'flow': 3.3596, 'imps': 0.0886, 'need': 0.2977, 'energy': 1},
                    7:  {'flow': 3.2026, 'imps': 0.0975, 'need': 0.3122, 'energy': 1},
                    8:  {'flow': 3.0528, 'imps': 0.1073, 'need': 0.3276, 'energy': 1},
                    9:  {'flow': 2.9111, 'imps': 0.118,  'need': 0.3435, 'energy': 1},
                    10: {'flow': 2.7756, 'imps': 0.1298, 'need': 0.3603, 'energy': 1}}

        if flowEntropy != expected:
            print('\n07: Unexpected result! \nExpected:', expected, '\nInstead :', flowEntropy)

        assert flowEntropy == expected

if __name__ == '__main__':
    unittest.main()