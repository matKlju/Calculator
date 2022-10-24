from calculator import *
import unittest


class TestCalculator(unittest.TestCase):
    # def test_get_result(self):
    #     self.assertEqual(get_result('a', 'f', '2'), TypeError)

    def test_get_result_addition_negative_input(self):
        self.assertEqual(get_result(-2.0, 1.0, 1), -1.0)

    def test_get_result_subtraction_negative_input(self):
        self.assertEqual(get_result(-2.0, -3.0, 2), 1.0)

    def test_get_result_multiply_negative_input(self):
        self.assertEqual(get_result(6.0, -2.0, 3), -12.0)
        self.assertEqual(get_result(-4, 22, 3), -88.0)

    def test_get_result_division_negative_input(self):
        self.assertEqual(get_result(-13.0, -2.0, 4), 6.5)
        # self.assertEqual(get_result(3.0, "", 5), 9.0)

    def test_get_result_integer_input(self):
        self.assertEqual(get_result(2, 5, 1), 7.0)

    def test_get_result_divide_by_zero(self):
        self.assertEqual(get_result(5.0, 0.0, 4), None)


if __name__ == "__main__":
    unittest.main()
        