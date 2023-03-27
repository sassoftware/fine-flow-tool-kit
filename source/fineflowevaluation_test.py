# fineflowevaluation_test.py

# Copyright © 2023, SAS Institute Inc., Cary, NC, USA.  All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import unittest
import fineflowevaluation as fine

class TestFineFlowEvaluation(unittest.TestCase):

    def setUp(self):

        #Generic flow of value between team topologies with interactions
        self.genericTeamFlowAndInteractions = {'StreamAligned': [('Enabling', 'F'),('ComplicatedSubSystem', 'C'), ('Platform', 'X')],
                                               'Enabling': [],
                                               'ComplicatedSubSystem': [('Enabling', 'F'), ('Platform','X')],
                                               'Platform': [('Enabling', 'F')]
        }

    def test_whenGivenGenericTeamFlowAndInteractionsThenFINEValuesAreAsExpected(self):

        ttopology = fine.evaluate(self.genericTeamFlowAndInteractions, flow=True, imp=True, need=True, energy=True)

                                            #flow    #imps   #need   #energy
        expected = {'StreamAligned':        [2.4498, 0.1041, 0.2551, 0.625  ],
                    'Enabling':             [0.7084, 0.8718, 0.6176, 0.4375 ],
                    'ComplicatedSubSystem': [1.7192, 0.2115, 0.3635, 0.625  ],
                    'Platform':             [1.3756, 0.4294, 0.5906, 0.8125 ]}

        if ttopology != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', ttopology)

        assert ttopology == expected


    def test_whenGivenGenericTeamFlowAndInteractionsThenFINEValuesWithResilienceAreAsExpected(self):

        ttopology = fine.evaluate(self.genericTeamFlowAndInteractions, flow=True, imp=True, need=True, energy=True, resilience=True)

                                            #flow    #imps   #need   #energy #resilience
        expected = {'StreamAligned':        [2.4498, 0.1041, 0.2551, 0.625,  5], 
                    'Enabling':             [0.7084, 0.8718, 0.6176, 0.4375, 9],
                    'ComplicatedSubSystem': [1.7192, 0.2115, 0.3635, 0.625,  5],
                    'Platform':             [1.3756, 0.4294, 0.5906, 0.8125, 3]}

        if ttopology != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', ttopology)

        assert ttopology == expected


    def test_whenGivenValuesForFlowAndImpsThenNeedAndEnergyComputed(self):
        
        finevalues = fine.compute(flow=2.4498, imps=0.1041)

        expected = {'flow'  : 2.4498,
                    'imps'  : 0.1041,
                    'need'  : 0.255,
                    'energy': 0.6248}

        if finevalues != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', finevalues)
        
        assert finevalues == expected
        assert expected['flow'] == 2.4498


    def test_whenGivenLessThanTwoValuesThenError(self):

        finevalues = fine.compute(flow=1.2345)

        expected = {'error' : 'Too few values, must have least two inputs'}

        if finevalues != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', finevalues)
        
        assert finevalues == expected


    def test_whenGivenValuesForFlowAndNeedThenImpsAndEnergyComputed(self):

        finevalues = fine.compute(flow=2.4498, need=0.255)

        expected = {'flow'  : 2.4498,
                    'imps'  : 0.1041,
                    'need'  : 0.255,
                    'energy': 0.6247}

        if finevalues != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', finevalues)
        
        assert finevalues == expected


    def test_whenGivenValuesForFlowAndEnergyThenImpsAndNeedComputed(self):

        finevalues = fine.compute(flow=2.4498, energy=0.6247)

        expected = {'flow'  : 2.4498,
                    'imps'  : 0.1041,
                    'need'  : 0.255,
                    'energy': 0.6247}

        if finevalues != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', finevalues)
        
        assert finevalues == expected


    def test_whenGivenValuesForImpsAndNeedThenFlowAndEnergyComputed(self):

        finevalues = fine.compute(imps=0.1041, need=0.255)

        expected = {'flow'  : 2.4496,
                    'imps'  : 0.1041,
                    'need'  : 0.255,
                    'energy': 0.6246}

        if finevalues != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', finevalues)
        
        assert finevalues == expected


    def test_whenGivenValuesForImpsAndEnergyThenFlowAndNeedComputed(self):

        finevalues = fine.compute(imps=0.1041, energy=0.6247)

        expected = {'flow'  : 2.4497,
                    'imps'  : 0.1041,
                    'need'  : 0.255,
                    'energy': 0.6247}

        if finevalues != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', finevalues)
        
        assert finevalues == expected


    def test_whenGivenValuesForNeedAndEnergyThenFlowAndImpsComputed(self):

        finevalues = fine.compute(need=0.255, energy=0.6247)

        expected = {'flow'  : 2.4498,
                    'imps'  : 0.1041,
                    'need'  : 0.255,
                    'energy': 0.6247}

        if finevalues != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', finevalues)
        
        assert finevalues == expected


    def test_whenAllValuesGivenThenAllAreComputed(self):
        
        finevalues = fine.compute(flow=2.4498, imps=0.1041, need=0.255, energy=0.6248)

        expected = {'flow'  : 2.4498,
                    'imps'  : 0.1041,
                    'need'  : 0.255,
                    'energy': 0.6248}

        if finevalues != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', finevalues)
        
        assert finevalues == expected

if __name__ == '__main__':
    unittest.main()