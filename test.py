import unittest
import example


class TestCase(unittest.TestCase):

    def test_add_1(self):
        self.assertEqual(example.addition(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(example.subtract(2, 1), 1)

    def test_multiply(self):
        self.assertEqual(example.multiply(2, 2), 4)


if __name__ == '__main__':
    unittest.main()
