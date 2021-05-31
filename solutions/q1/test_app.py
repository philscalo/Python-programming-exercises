import unittest
from solutions.q1.app import sevn_not_five


class TestApp(unittest.TestCase):

    def test_app_seven(self):
        self.assertEqual(sevn_not_five(0, 7), '7')


    def test_app_thirty_five(self):
        self.assertEqual(sevn_not_five(0, 35), '7, 14, 21, 28')


    def test_app_iincludes_42(self):
        self.assertIn('42', sevn_not_five(0, 42))


if __name__ == '__main__':
    unittest.main()