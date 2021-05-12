import unittest
from parse_log_copy import minute, lecture, relever_valeur


class TestStringMethods(unittest.TestCase):

    def test_minute(self):
        self.assertEqual(minute(221,222), '0:01:00')
        self.assertNotAlmostEqual(minute(221,222), '0:02:00')

    def test_lecture(self):
        self.assertIsInstance(lecture('planning.log'), str)

    def test_relever_valeur(self):
        self.assertEqual(relever_valeur(),[100, 15, 20, 55, 60, 40, 20, 10, 60, 80, 30, 60, 20, 70, 30, 15, 90, 105, 15, 15, 30, 30])

if __name__ == '__main__':
    unittest.main()
