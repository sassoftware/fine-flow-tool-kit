# flowratio_test.py

# Copyright © 2023, SAS Institute Inc., Cary, NC, USA.  All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import unittest
import fineflowevaluation as fine
import flowratio as fr

class TestFineFlowEvaluation(unittest.TestCase):

    def setUp(self):

        #Generic flow of value between team topologies with interactions
        self.genericTeamFlowAndInteractions = {'StreamAligned': [('Enabling', 'F'),('ComplicatedSubSystem', 'C'), ('Platform', 'X')],
                                               'Enabling': [],
                                               'ComplicatedSubSystem': [('Enabling', 'F'), ('Platform','X')],
                                               'Platform': [('Enabling', 'F')]
        }


    def test_whenGivenGenericTeamFlowAndInteractionsThenFINEValuesAreAsExpected(self):

        ttopology = fine.evaluate(self.genericTeamFlowAndInteractions, flow=True, imp=True, need=True, energy=True, resilience=True)

                                            #flow    #imps   #need   #energy #resilience
        expected = {'StreamAligned':        [2.4498, 0.1041, 0.2551, 0.625,  5],
                    'Enabling':             [0.7084, 0.8718, 0.6176, 0.4375, 9],
                    'ComplicatedSubSystem': [1.7192, 0.2115, 0.3635, 0.625,  5],
                    'Platform':             [1.3756, 0.4294, 0.5906, 0.8125, 3]}

        if ttopology != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', ttopology)

        assert ttopology == expected


    def test_whenGivenBadAndGoodFlowThenComputedFlowRatioIsAsExpected(self):

        flowratio = fr.computeRatio(bad=1,good=10)
        expected = 0.1

        if flowratio != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', flowratio)

        assert flowratio == expected


    def test_whenGivenBadAndGoodFlowThenComputedProbabilityOfBadFlowIsAsExpected(self):
        probBad = fr.computeProbBad(bad=1, good=10)
        expected = 0.0909

        if probBad != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', probBad)

        assert probBad == expected


    def test_whenGivenBadAndGoodFlowThenComputedProbabilityOfGoodFlowIsAsExpected(self):
        probGood = fr.computeProbGood(bad=1, good=10)
        expected = 0.9091

        if probGood != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', probGood)

        assert probGood == expected


    def test_whenGivenBadAndGoodFlowWithBatchSizeThenComputedFlowRatioIsAsExpected(self):

        flowratio = fr.computeRatio(bad=15,good=85,batchSize=2)
        expected = 0.3841

        if flowratio != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', flowratio)

        assert flowratio == expected


    def test_whenGivenFlowMetricsThenFlowEntropyIsAsExpected(self):

        flowEntropy = fr.computeEntropy(bad=15, good=85, batchSize=1, cycles=5, imps=0.1041, energy=0.625)

        expected = {'ratio': 0.1765,
                    1: {'flow': 2.4503, 'imps': 0.1041, 'need': 0.2551, 'energy': 0.625},
                    2: {'flow': 2.2588, 'imps': 0.1225, 'need': 0.2767, 'energy': 0.625},
                    3: {'flow': 2.0826, 'imps': 0.1441, 'need': 0.3001, 'energy': 0.625},
                    4: {'flow': 1.9202, 'imps': 0.1695, 'need': 0.3255, 'energy': 0.625},
                    5: {'flow': 1.7704, 'imps': 0.1994, 'need': 0.353,  'energy': 0.625}}

        if flowEntropy != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', flowEntropy)

        assert flowEntropy == expected


    def test_whenGivenFlowMetricsWithBatch4ThenFlowEntropyIsAsExpected(self):

        flowEntropy = fr.computeEntropy(bad=15, good=85, batchSize=4, cycles=5, imps=0.1041, energy=0.625)
        
        expected = {'ratio': 0.9157,
                    1: {'flow': 2.4503, 'imps': 0.1041, 'need': 0.2551, 'energy': 0.625},
                    2: {'flow': 1.7704, 'imps': 0.1994, 'need': 0.353,  'energy': 0.625},
                    3: {'flow': 1.2791, 'imps': 0.382,  'need': 0.4886, 'energy': 0.625},
                    4: {'flow': 0.9242, 'imps': 0.7318, 'need': 0.6763, 'energy': 0.625},
                    5: {'flow': 0.6677, 'imps': 1.4019, 'need': 0.936,  'energy': 0.625}}

        if flowEntropy != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', flowEntropy)

        assert flowEntropy == expected


    def test_whenGivenFlowMetricsAndFixedFlowThenenergyIncreasesAsExpected(self):

        flowEntropy = fr.computeEntropy(bad=15, good=85, batchSize=1, cycles=5, imps=0.1041, energy=0.625, fixedFlow=True)

        expected = {'ratio': 0.1765,
                    1: {'flow': 2.4503, 'imps': 0.1041, 'need': 0.2551, 'energy': 0.625},
                    2: {'flow': 2.4503, 'imps': 0.1225, 'need': 0.3002, 'energy': 0.7355},
                    3: {'flow': 2.4503, 'imps': 0.1441, 'need': 0.3531, 'energy': 0.8652},
                    4: {'flow': 2.4503, 'imps': 0.1695, 'need': 0.4153, 'energy': 1.0177},
                    5: {'flow': 2.4503, 'imps': 0.1994, 'need': 0.4886, 'energy': 1.1972}}

        if flowEntropy != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', flowEntropy)

        assert flowEntropy == expected


    def test_whenGivenFlowMetricsWithCappedEnergyThenFlowDecreasesAsExpected(self):

        flowEntropy = fr.computeEntropy(bad=15, good=85, batchSize=1, cycles=5, imps=0.1041, energy=0.625, fixedFlow=True, energyMax=1)

        expected = {'ratio': 0.1765,
                     1: {'flow': 2.4503, 'imps': 0.1041, 'need': 0.2551, 'energy': 0.625 },
                     2: {'flow': 2.4503, 'imps': 0.1225, 'need': 0.3002, 'energy': 0.7355},
                     3: {'flow': 2.4503, 'imps': 0.1441, 'need': 0.3531, 'energy': 0.8652},
                     4: {'flow': 2.4289, 'imps': 0.1695, 'need': 0.4117, 'energy': 1     },
                     5: {'flow': 2.2394, 'imps': 0.1994, 'need': 0.4465, 'energy': 1     }}

        if flowEntropy != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', flowEntropy)

        assert flowEntropy == expected


    def test_whenGivenFlowMetricsForEnablingTeamAndBatch4WithCappedEnergyThenFlowDecreasesAsExpected(self):

        flowEntropy = fr.computeEntropy(bad=15, good=85, batchSize=4, cycles=10, imps=0.8718, energy=0.4375, fixedFlow=True, energyMax=1)

        expected = {'ratio': 0.9157,
                     1:  {'flow': 0.7084, 'imps': 0.8718,   'need': 0.6176,  'energy': 0.4375},
                     2:  {'flow': 0.7084, 'imps': 1.6701,   'need': 1.1831,  'energy': 0.8381},
                     3:  {'flow': 0.5591, 'imps': 3.1994,   'need': 1.7887,  'energy': 1},
                     4:  {'flow': 0.4039, 'imps': 6.1291,   'need': 2.4757,  'energy': 1},
                     5:  {'flow': 0.2918, 'imps': 11.7415,  'need': 3.4266,  'energy': 1},
                     6:  {'flow': 0.2109, 'imps': 22.4932,  'need': 4.7427,  'energy': 1},
                     7:  {'flow': 0.1523, 'imps': 43.0902,  'need': 6.5643,  'energy': 1},
                     8:  {'flow': 0.1101, 'imps': 82.5479,  'need': 9.0856,  'energy': 1},
                     9:  {'flow': 0.0795, 'imps': 158.137,  'need': 12.5753, 'energy': 1},
                     10: {'flow': 0.0575, 'imps': 302.9431, 'need': 17.4053, 'energy': 1}}

        if flowEntropy != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', flowEntropy)

        assert flowEntropy == expected


    def test_whenGivenFlowMetricsForEnablingTeamAndBatch1WithCappedEnergyThenFlowDecreasesAsExpected(self):

        flowEntropy = fr.computeEntropy(bad=15, good=85, batchSize=1, cycles=10, imps=0.8718, energy=0.4375, fixedFlow=True, energyMax=1)

        expected = {'ratio': 0.1765,
                    1:  {'flow': 0.7084, 'imps': 0.8718, 'need': 0.6176, 'energy': 0.4375},
                    2:  {'flow': 0.7084, 'imps': 1.0257, 'need': 0.7266, 'energy': 0.5147},
                    3:  {'flow': 0.7084, 'imps': 1.2067, 'need': 0.8549, 'energy': 0.6056},
                    4:  {'flow': 0.7084, 'imps': 1.4197, 'need': 1.0057, 'energy': 0.7124},
                    5:  {'flow': 0.7084, 'imps': 1.6703, 'need': 1.1832, 'energy': 0.8382},
                    6:  {'flow': 0.7084, 'imps': 1.9651, 'need': 1.392,  'energy': 0.9861},
                    7:  {'flow': 0.6577, 'imps': 2.3119, 'need': 1.5205, 'energy': 1},
                    8:  {'flow': 0.6063, 'imps': 2.72,   'need': 1.6492, 'energy': 1},
                    9:  {'flow': 0.559,  'imps': 3.2001, 'need': 1.7889, 'energy': 1},
                    10: {'flow': 0.5154, 'imps': 3.7649, 'need': 1.9403, 'energy': 1}}

        if flowEntropy != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', flowEntropy)

        assert flowEntropy == expected


    def test_whenGivenFlowMetricsForEnablingTeamAndBatch1WithCappedEnergyThenFlowDecreasesAsExpectedWithComputedDrop(self):

        flowEntropy = fr.computeEntropy(bad=15, good=85, batchSize=1, cycles=10, imps=0.8718, energy=0.4375, fixedFlow=True, energyMax=1, drop=True)

        expected = {'ratio': 0.1765, 'drop': 0.27,
                    1:  {'flow': 0.7084, 'imps': 0.8718, 'need': 0.6176, 'energy': 0.4375}, 
                    2:  {'flow': 0.7084, 'imps': 1.0257, 'need': 0.7266, 'energy': 0.5147},
                    3:  {'flow': 0.7084, 'imps': 1.2067, 'need': 0.8549, 'energy': 0.6056},
                    4:  {'flow': 0.7084, 'imps': 1.4197, 'need': 1.0057, 'energy': 0.7124},
                    5:  {'flow': 0.7084, 'imps': 1.6703, 'need': 1.1832, 'energy': 0.8382},
                    6:  {'flow': 0.7084, 'imps': 1.9651, 'need': 1.392,  'energy': 0.9861},
                    7:  {'flow': 0.6577, 'imps': 2.3119, 'need': 1.5205, 'energy': 1},
                    8:  {'flow': 0.6063, 'imps': 2.72,   'need': 1.6492, 'energy': 1},
                    9:  {'flow': 0.559,  'imps': 3.2001, 'need': 1.7889, 'energy': 1},
                    10: {'flow': 0.5154, 'imps': 3.7649, 'need': 1.9403, 'energy': 1}}

        if flowEntropy != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', flowEntropy)

        assert flowEntropy == expected


    def test_whenGivenFlowMetricsForEnablingTeamAndBatch1ThenResilienceIsAsExpected(self):

        resilience = fr.computeResilience(bad=15, good=85, batchSize=1, imps=0.8718, energy=0.4375)

        expected = 6
        if resilience != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', resilience)

        assert resilience == expected


    def test_whenGivenFlowMetricsForEnablingTeamAndBatch4ThenResilienceIsAsExpected(self):

        resilience = fr.computeResilience(bad=15, good=85, batchSize=4, imps=0.8718, energy=0.4375)

        expected = 2
        if resilience != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', resilience)

        assert resilience == expected


if __name__ == '__main__':
    unittest.main()
