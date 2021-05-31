import unittest

from solutions.q2.app import factorize


class TestApp(unittest.TestCase):

    def test_app(self):
        self.assertEqual(factorize(8), 40320)


if __name__ == '__main__':
    unittest.main()