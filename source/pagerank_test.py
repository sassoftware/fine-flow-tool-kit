# pagerank_test.py

# Copyright © 2023, SAS Institute Inc., Cary, NC, USA.  All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import unittest
import numpy as np
import pagerank as pr

class TestPageRank(unittest.TestCase):

    def test_whenGivenGenericTeamToplogyThenRanksAreAsExpected(self):
        TT = np.array([[0,1,1,1],
                       [0,0,0,0],
                       [0,1,0,1],
                       [0,1,0,0]])

        v = pr.pagerank(TT, 100, 0.8)
        
        expected = np.array([0.00430928,0.03607688,0.0087505,0.01776775])
        assert np.allclose(v, expected)

    def test_whenGivenGenericTeamToplogyThenRanksAreAsExpectedWithNormalize(self):
        TT = np.array([[0,1,1,1],
                       [0,0,0,0],
                       [0,1,0,1],
                       [0,1,0,0]])

        v = pr.pagerank(TT, 100, 0.8, normalize=True)
        
        expected = np.array([0.10413698, 0.87182534, 0.21146251, 0.42937125])
        assert np.allclose(v, expected)

    def test_whenGivenLargerExampleTeamToplogyThenRanksAreAsExpected(self):
        TT = np.array([[0, 0, 1, 0, 1, 1, 0],
                       [0, 0, 1, 1, 1, 1, 0],
                       [0, 0, 0, 0, 0, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 1],
                       [0, 0, 0, 0, 1, 0, 0]])

        v = pr.pagerank(TT, 100, 0.8)
        
        expected = np.array([0.01505679, 0.01505679, 0.04081108, 0.02793393, 0.20366906, 0.07571414, 0.11471273])
        assert np.allclose(v, expected)


    def test_whenGivenGenericTeamToplogyClassifyIsAsExpected(self):
        v = np.array([0.00430928,0.03607688,0.0087505,0.01776775])

        hilo = pr.classify(v)

        expected = np.array([0,1,0,1])
        assert np.array_equal(hilo, expected)

    def test_whenGivenLargerExampleThenClassifyIsAsExpected(self):
        v = np.array([0.01505679, 0.01505679, 0.04081108, 0.02793393, 0.20366906, 0.07571414, 0.11471273])

        hilo = pr.classify(v)

        expected = np.array([0,0,0,0,1,1,1])
        assert np.array_equal(hilo, expected)

    def test_whenGivenSimpleTwoNodeDictionaryThenAdjMatrixIsAsExpected(self):
        d = {"A":["B"],"B":[]}

        v = pr.dictToArray(d)

        expected = np.array([[0,1],[0,0]])
        assert np.array_equal(v, expected)

    def test_whenGivenGivenGenericTeamToplogyDictionaryThenAdjMatrixIsAsExpected(self):
        tt = {"SA":["EN", "CS","PF"],
              "EN":[],
              "CS":["EN","PF"],
              "PF":["EN"]
        }

        v = pr.dictToArray(tt)

        expected = np.array([[0,1,1,1],
                             [0,0,0,0],
                             [0,1,0,1],
                             [0,1,0,0]])

        assert np.array_equal(v, expected)

if __name__ == '__main__':
    unittest.main()