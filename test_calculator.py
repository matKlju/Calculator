from calculator import *
import unittest


class TestCalculator(unittest.TestCase):
    # def test_get_result(self):
    #     self.assertEqual(get_result('a', 'f', '2'), TypeError)

    def test_get_result_negative(self):
        self.assertEqual(get_result(-2, 1, 1), -1)
        self.assertEqual(get_result(-2, -3, 1), -5)

    def test_get_result_divide_by_zero(self):
        self.assertEqual(get_result(-2, 0, 4), None)


if __name__ == "__main__":
    unittest.main()
        