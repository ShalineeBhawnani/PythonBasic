# ******************************************************************************************************************
# @purpose :Demonstrate QuadraticEquestionTest.
# @file  :QuadraticTest.py
# @author :ShalineeBhawnani
# *******************************************************************************************************************
import unittest
from Quadratic import quadratic

#creating test case
class MyTestCase(unittest.TestCase):
    def test_Quadratic(self):

        #calling method & storing result
        result=quadratic(3,19,8)
        #comparing result with expected data
        self.assertListEqual(result,[-0.453529900650049,-5.879803432683285])

#to check whether the module is being imported or not
if __name__ == '__main__':
    unittest.main()
