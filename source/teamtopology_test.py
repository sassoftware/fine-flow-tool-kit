# teamtopology_test.py

# Copyright © 2023, SAS Institute Inc., Cary, NC, USA.  All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import unittest
import teamtopology as tt

class TestTeamTopology(unittest.TestCase):

    def setUp(self):

        #Generic flow of value between team topologies
        self.genericTeamFlow = {'StreamAligned': ['Enabling','ComplicatedSubSystem', 'Platform'],
                                'Enabling': [],
                                'ComplicatedSubSystem': ['Enabling', 'Platform'],
                                'Platform': ['Enabling']
        }

         #Flow of value between team topologies for a non-general case
        self.nonGeneralCase = {'StreamAligned': ['Enabling','ComplicatedSubSystem'],
                               'Enabling': [],
                               'ComplicatedSubSystem': ['Enabling', 'Platform'],
                               'Platform': ['Enabling']
        }
        
        #Team flow for Bakers Unlimited Example
        self.exampleTeamFlow = {'StoreRO':  ['CRM', 'QE', 'DataEC'],
                                'OnlineRO': ['CRM', 'UX', 'QE', 'DataEC'],
                                'CRM':      ['DataEC', 'CloudES'],
                                'UX':       [],
                                'QE':       [],
                                'DataEC':   ['QE', 'CloudES'],
                                'CloudES':  ['QE']
        }


    def test_whenGivenGenericTeamFlowThenTopologyIsAsExpected(self):

        ttopology = tt.findTopology(self.genericTeamFlow)

        expected = {'StreamAligned':        ['SA'],
                    'Enabling':             ['EN'],
                    'ComplicatedSubSystem': ['CS'],
                    'Platform':             ['PF']
                    }

        if ttopology != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', ttopology)

        assert ttopology == expected


    def test_whenGivenGenericTeamFlowAndNotUsingExtendedAlgorithmThenTopologyIsAsExpected(self):

        ttopology = tt.findTopology(self.genericTeamFlow, extended=False)

        expected = {'StreamAligned':        ['SA'],
                    'Enabling':             ['EN'],
                    'ComplicatedSubSystem': ['SA'],
                    'Platform':             ['EN']
                    }

        if ttopology != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', ttopology)

        assert ttopology == expected


    def test_whenGivenGenericTeamFlowThenTopologyIsAsExpectedWithCentralitesAndClassifiers(self):

        ttopology = tt.findTopology(self.genericTeamFlow, centralities=True, classifiers=True)

        expected = {'StreamAligned':        [0.0, 0.1041, 0, 0, 'SA'],
                    'Enabling':             [0.0, 0.8718, 0, 1, 'EN'],
                    'ComplicatedSubSystem': [0.0, 0.2115, 1, 0, 'CS'],
                    'Platform':             [0.0, 0.4294, 1, 1, 'PF']
                    }

        if ttopology != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', ttopology)

        assert ttopology == expected


    def test_whenNonGeneralCaseThenTopologyIsAsExpectedWithCentralitesAndClassifiers(self):

        ttopology = tt.findTopology(self.nonGeneralCase, centralities=True, classifiers=True)

        expected = {'StreamAligned':        [0.0,    0.1106, 0, 0, 'SA'],
                    'Enabling':             [0.0,    0.8938, 0, 1, 'EN'],
                    'ComplicatedSubSystem': [0.1667, 0.2326, 1, 0, 'CS'],
                    'Platform':             [0.0,    0.3671, 1, 1, 'PF']
                    }

        if ttopology != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', ttopology)

        assert ttopology == expected


    def test_whenGivenExampleTeamFlowThenTopologyIsAsExpected(self):

        ttopology = tt.findTopology(self.exampleTeamFlow)

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


    def test_whenGivenExampleTeamFlowThenTopologyIsAsExpectedWithClassifiers(self):

        ttopology = tt.findTopology(self.exampleTeamFlow, classifiers=True)

        expected = {'StoreRO':  [0, 0, 'SA'],
                    'OnlineRO': [0, 0, 'SA'],
                    'CRM':      [1, 0, 'CS'],
                    'UX':       [0, 1, 'EN'],
                    'QE':       [0, 1, 'EN'],
                    'DataEC':   [1, 1, 'PF'],
                    'CloudES':  [1, 1, 'PF']
                    }

        if ttopology != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', ttopology)

        assert ttopology == expected


    def test_whenGivenExampleTeamFlowThenTopologyIsAsExpectedWithCentralities(self):

        ttopology = tt.findTopology(self.exampleTeamFlow, centralities=True)

        expected = {'StoreRO':  [0.0,    0.0599, 'SA'],
                    'OnlineRO': [0.0,    0.0599, 'SA'],
                    'CRM':      [0.0333, 0.1622, 'CS'],
                    'UX':       [0.0,    0.1111, 'EN'],
                    'QE':       [0.0,    0.8097, 'EN'],
                    'DataEC':   [0.05,   0.301,  'PF'],
                    'CloudES':  [0.0167, 0.456,  'PF']
                    }

        if ttopology != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', ttopology)

        assert ttopology == expected


    def test_whenGivenExampleTeamFlowThenTopologyIsAsExpectedWithCentralitiesAndClassifiers(self):

        ttopology = tt.findTopology(self.exampleTeamFlow, centralities=True, classifiers=True)

        expected = {'StoreRO':  [0.0,    0.0599, 0, 0, 'SA'],
                    'OnlineRO': [0.0,    0.0599, 0, 0, 'SA'],
                    'CRM':      [0.0333, 0.1622, 1, 0, 'CS'],
                    'UX':       [0.0,    0.1111, 0, 1, 'EN'],
                    'QE':       [0.0,    0.8097, 0, 1, 'EN'],
                    'DataEC':   [0.05,   0.301,  1, 1, 'PF'],
                    'CloudES':  [0.0167, 0.456,  1, 1, 'PF']
                    }

        if ttopology != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', ttopology)

        assert ttopology == expected

    def test_whenGivenExampleTeamFlowThenTopologyIsAsExpectedWithExtendedChecksOff(self):

        ttopology = tt.findTopology(self.exampleTeamFlow, centralities=True, classifiers=True, extended=False)

        expected = {'StoreRO':  [0.0,    0.0599, 0, 0, 'SA'],
                    'OnlineRO': [0.0,    0.0599, 0, 0, 'SA'],
                    'CRM':      [0.0333, 0.1622, 1, 0, 'CS'],
                    'UX':       [0.0,    0.1111, 0, 0, 'SA'],
                    'QE':       [0.0,    0.8097, 0, 1, 'EN'],
                    'DataEC':   [0.05,   0.301,  1, 1, 'PF'],
                    'CloudES':  [0.0167, 0.456,  1, 1, 'PF']
                    }

        if ttopology != expected:
            print('\nUnexpected result! \nExpected:', expected, '\nInstead :', ttopology)

        assert ttopology == expected

if __name__ == '__main__':
    unittest.main()
