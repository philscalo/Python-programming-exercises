import unittest

from solutions.q3.app import square_dict

class TestApp(unittest.TestCase):

    def test_square_dict(self):
        self.assertEqual(square_dict(3), {1: 1, 2: 4, 3: 9})


if __name__ == '__main__':
    unittest.main()