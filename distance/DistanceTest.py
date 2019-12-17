# ******************************************************************************************************************
# @purpose :Demonstrate DistanceTest.
# @file  :DistanceTest.py
# @author :ShalineeBhawnani
# *******************************************************************************************************************
import unittest
import math
from Distance import calculateDistance

#creating class for unit test
class MyTestCase(unittest.TestCase):
    def test_distance(self):

        #calling method & storing result
        result = calculateDistance(1,2,3,4)

        #comparing result with expected data
        self.assertEqual(result,2.8284271247461903)

        #calling method & storing result
        result = calculateDistance(5,2,3,5)

        #comparing result with expected data
        self.assertEqual(result,3.605551275463989)

        #calling method & storing result
        result = calculateDistance(4,5,2,4)

        #comparing result with expected data
        self.assertEqual(result,2.23606797749979)


if __name__ == '__main__':
    unittest.main()
