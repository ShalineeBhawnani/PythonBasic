import unittest
from LeapYear import leap_year


class MyTestCase(unittest.TestCase):
    def test_LeapYear(self):
        self.assertEqual(leap_year(2000), True)
        self.assertEqual(leap_year(1919), False)
        self.assertEqual(leap_year(1232), True)
        self.assertEqual(leap_year(1929), False)
        self.assertEqual(leap_year(1219), False)
        self.assertEqual(leap_year(1900), False)


if __name__ == '__main__':
    unittest.main()
