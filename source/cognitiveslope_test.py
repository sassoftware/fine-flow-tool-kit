# cognitiveslope_test.py

# Copyright © 2023, SAS Institute Inc., Cary, NC, USA.  All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import unittest
import numpy as np
import teamtopology as tt
import cognitiveslope as cs

class TestCognitiveSlope(unittest.TestCase):

    def setUp(self):

        #Generic flow of value between team topologies with interactions
        self.genericTeamFlowAndInteractions = {'StreamAligned': [('Enabling', 'F'),('ComplicatedSubSystem', 'C'), ('Platform', 'X')],
                                               'Enabling': [],
                                               'ComplicatedSubSystem': [('Enabling', 'F'), ('Platform','X')],
                                               'Platform': [('Enabling', 'F')]
        }

        #Team flow for Bakers Unlimited Example
        self.exampleTeamFlow = {'StoreRO':  [('CRM', 'C'), ('QE', 'F'), ('DataEC', 'X')],
                                'OnlineRO': [('CRM', 'C'), ('UX', 'F'), ('QE', 'F'), ('DataEC', 'X')],
                                'CRM':      [('DataEC', 'X'), ('CloudES', 'X')],
                                'UX':       [],
                                'QE':       [],
                                'DataEC':   [('QE', 'F'), ('CloudES', 'X')],
                                'CloudES':  [('QE', 'F')]
        }

        #Team flow for Bakers Unlimited Example focused on Value Stream Map for OnlineRO 
        self.exampleTeamFlowOnlineRO = {'OnlineRO': [('UX', 'F'), ('QE', 'F'), ('DataEC', 'X')],
                                       'UX':       [],
                                       'QE':       [],
                                       'DataEC':   [('QE', 'F'), ('CloudES', 'X')],
                                       'CloudES':  [('QE', 'F')]
        }

    def test_whenGivenGenericTeamFlowAndInteractionsThenWeightedArrayIsAsExpected(self):

        weightedArray = cs.dictToArray(self.genericTeamFlowAndInteractions)

        expected = np.array([[1.0, 0.25, 0.5, 0.75],
                             [0.0, 1.0,  0.0, 0.0 ],
                             [0.0, 0.25, 1.0, 0.75],
                             [0.0, 0.25, 0.0, 1.0 ]])

        if not np.array_equal(weightedArray, expected):
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', weightedArray)

        assert np.array_equal(weightedArray, expected)


    def test_whenGivenGenericTeamFlowAndInteractionsThenTwoSidedWeightedArrayIsAsExpected(self):

        weightedArray = cs.dictToArrayTwoSided(self.genericTeamFlowAndInteractions)

        expected = np.array([[1.0,  0.25, 0.5,  0.75],
                             [0.75, 1.0,  0.75, 0.75 ],
                             [0.5,  0.25, 1.0,  0.75],
                             [0.25, 0.25, 0.25, 1.0 ]])

        if not np.array_equal(weightedArray, expected):
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', weightedArray)

        assert np.array_equal(weightedArray, expected)


    def test_whenGivenGivenGenericTeamToplogyWithInteractionsThenAdjMatrixIsAsExpected(self):

        v = cs.dictToArray(self.genericTeamFlowAndInteractions, adjMatrix=True)

        expected = np.array([[0,1,1,1],
                             [0,0,0,0],
                             [0,1,0,1],
                             [0,1,0,0]])

        if not np.array_equal(v, expected):
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', v)

        assert np.array_equal(v, expected)


    def test_whenGivenGenericTeamFlowAndInteractionsThenValuesAreAsExpected(self):

        ttopology = cs.findCognitiveSlope(self.genericTeamFlowAndInteractions, flow=True, imp=True, need=True, energy=True, sum=True)

                                            #flow    #imps   #need   #energy #sum
        expected = {'StreamAligned':        [2.4498, 0.1041, 0.2551, 0.625,  2.5],
                    'Enabling':             [0.7084, 0.8718, 0.6176, 0.4375, 1.75],
                    'ComplicatedSubSystem': [1.7192, 0.2115, 0.3635, 0.625,  2.5],
                    'Platform':             [1.3756, 0.4294, 0.5906, 0.8125, 3.25]}

        if ttopology != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', ttopology)

        assert ttopology == expected


    def test_whenGivenExampleFlowAndInteractionsThenValuesAreAsExpected(self):

        ttopology = cs.findCognitiveSlope(self.exampleTeamFlow, flow=True, imp=True, need=True, energy=True, sum=True)

                                #flow    #imps   #need   #energy #sum
        expected = {'StoreRO':  [3.2313, 0.0599, 0.1934, 0.625,  2.5],
                    'OnlineRO': [3.2953, 0.0599, 0.1973, 0.65,   3.25],
                    'CRM':      [1.7555, 0.1622, 0.2848, 0.5,    2.5],
                    'UX':       [2.3723, 0.1111, 0.2635, 0.625,  1.25],
                    'QE':       [0.7029, 0.8097, 0.5691, 0.4,    2.0],
                    'DataEC':   [1.534,  0.301,  0.4617, 0.7083, 4.25],
                    'CloudES':  [1.3348, 0.456,  0.6087, 0.8125, 3.25]
                    }

        if ttopology != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', ttopology)

        assert ttopology == expected


    def test_whenGivenStoreROExampleFlowAndInteractionsThenValuesAreAsExpected(self):

        ttopology = cs.findCognitiveSlope(self.exampleTeamFlowOnlineRO, flow=True, imp=True, need=True, energy=True)

                                 #flow   #imps   #need   #energy 
        expected = {'OnlineRO': [2.5985, 0.1018, 0.2646, 0.6875],
                    'UX':       [1.69,   0.2188, 0.3698, 0.625 ],
                    'QE':       [0.7063, 0.8769, 0.6194, 0.4375],
                    'DataEC':   [1.7724, 0.2188, 0.3879, 0.6875],
                    'CloudES':  [1.5355, 0.3534, 0.5427, 0.8333]
                    }

        if ttopology != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', ttopology)

        assert ttopology == expected

if __name__ == '__main__':
    unittest.main()