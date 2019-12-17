# ******************************************************************************************************************
# @purpose :Demonstrate DistanceTest.
# @file  :DistanceTest.py
# @author :ShalineeBhawnani
# *******************************************************************************************************************
import unittest
import math
from Distance import calculateDistance

class MyTestCase(unittest.TestCase):
    def test_distance(self):
        result = calculateDistance(1,2,3,4)
        self.assertEqual(result,2.8284271247461903)

        result = calculateDistance(5,2,3,5)
        self.assertEqual(result,3.605551275463989)

        result = calculateDistance(4,5,2,4)
        self.assertEqual(result,2.23606797749979)


if __name__ == '__main__':
    unittest.main()
