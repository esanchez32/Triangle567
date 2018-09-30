# -*- coding: utf-8 -*-
"""
Updated Sep 8, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: Elena Sanchez
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testInvalidTriangle(self):
        self.assertEqual(classifyTriangle(205, 6, 7), 'InvalidInput', '205, 6, 7 is Invalid')

    def testInvalidInput(self):
        self.assertEqual(classifyTriangle(-5, 4, 8), 'InvalidInput', '-5, 4, 8 is Invalid')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(15, 8, 4), 'NotATriangle', '15, 8, 4 is Not a Triangle')

    def testScalene(self):
        self.assertEqual(classifyTriangle(3, 5, 6), 'Scalene', '3, 5, 6 is a Scalene Triangle')

    def testIsosceles(self):
        self.assertEqual(classifyTriangle(3, 3, 6), 'Isosceles', '3, 3, 6 is an Isosceles Triangle')


if TestTriangles == ():
    print('Running unit tests')
    unittest.TestTriangles()

