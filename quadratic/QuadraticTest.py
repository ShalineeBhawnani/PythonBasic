# ******************************************************************************************************************
# @purpose :Demonstrate QuadraticEquestionTest.
# @file  :QuadraticTest.py
# @author :ShalineeBhawnani
# *******************************************************************************************************************
import unittest
from Quadratic import quadratic


class MyTestCase(unittest.TestCase):
    def test_Quadratic(self):
        result=quadratic(3,19,8)
        self.assertListEqual(result,[-0.453529900650049,-5.879803432683285])


if __name__ == '__main__':
    unittest.main()
