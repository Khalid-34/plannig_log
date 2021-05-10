import unittest
from parse_log_copy import minute, lecture


class TestStringMethods(unittest.TestCase):

    def test_minute(self):
        self.assertEqual(minute(221,222), '0:01:00')
        self.assertNotAlmostEqual(minute(221,222), '0:02:00')

    def test_lecture(self):
        self.assertIsInstance(lecture('planning.log'), str)

if __name__ == '__main__':
    unittest.main()
