# betweenness_test.py

# Copyright © 2023, SAS Institute Inc., Cary, NC, USA.  All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import unittest
import numpy as np
import betweenness as bt

class TestBetweenness(unittest.TestCase):

    def test_whenGivenGenericTeamToplogyThenBetweennessIsASExpected(self):
        TT = np.array([[0,1,1,1],
                       [0,0,0,0],
                       [0,1,0,1],
                       [0,1,0,0]])

        v = bt.betweenness(TT)
        
        expected = np.array([0.0,0.0,0.0,0.0])
        assert np.allclose(v, expected)

    def test_whenGivenLargerExampleTeamToplogyThenBetweennessIsAsExpected(self):
        TT = np.array([[0, 0, 1, 0, 1, 1, 0],
                       [0, 0, 1, 1, 1, 1, 0],
                       [0, 0, 0, 0, 0, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 1],
                       [0, 0, 0, 0, 1, 0, 0]])

        v = bt.betweenness(TT)
        
        expected = np.array([0, 0, 0.03333333, 0, 0, 0.05, 0.01666667])
        assert np.allclose(v, expected)

    def test_whenGivenGenericTeamToplogyClassifyIsAsExpected(self):
        v = np.array([0, 0, 0, 0])

        hilo = bt.classify(v)

        expected = np.array([0,0,0,0])
        assert np.array_equal(hilo, expected)

    def test_whenGivenLargerExampleThenClassifyIsAsExpected(self):
        v = np.array([0, 0, 0.03333333, 0, 0, 0.05, 0.01666667])

        hilo = bt.classify(v)

        expected = np.array([0,0,1,0,0,1,1])
        assert np.array_equal(hilo, expected)

if __name__ == '__main__':
    unittest.main()