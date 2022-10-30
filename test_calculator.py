from calculator import *
import unittest


class TestCalculator(unittest.TestCase):

    def test_get_result__addition_negative_input(self):
        self.assertEqual(get_result(-1.0, 2.0, 1), 1.0)
        self.assertEqual(get_result(3.0, -4.0, 1), -1.0)
        self.assertEqual(get_result(-5.0, -6.0, 1), -11.0)

    def test_get_result__subtraction_negative_input(self):
        self.assertEqual(get_result(-1.0, 2.0, 2), -3.0)
        self.assertEqual(get_result(3.0, -4.0, 2), 7.0)
        self.assertEqual(get_result(-5.0, -6.0, 2), 1.0)

    def test_get_result__multiply_negative_input(self):
        self.assertEqual(get_result(-1.0, 2.0, 3), -2.0)
        self.assertEqual(get_result(3.0, -4.0, 3), -12.0)
        self.assertEqual(get_result(-5.0, -6.0, 3), 30.0)

    def test_get_result__division_negative_input(self):
        self.assertEqual(get_result(-1.0, 2.0, 4), -0.5)
        self.assertEqual(get_result(3.0, -4.0, 4), -0.75)
        self.assertEqual(get_result(-5.0, -6.0, 4), 0.8333)

    def get_result__power_of_2(self):
        self.assertEqual(get_result(-1.0, None, 5), 1.0)
        self.assertEqual(get_result(3.0, None, 5), 9.0)
        self.assertEqual(get_result(-5.5, None, 5), 30.25)

    def test_get_result__integer_input(self):
        self.assertEqual(get_result(-3, 2, 1), -1.0)
        self.assertEqual(get_result(4, -3, 2), 7.0)
        self.assertEqual(get_result(-5, -4, 3), 20.0)
        self.assertEqual(get_result(6, 5, 4), 1.2)
        self.assertEqual(get_result(7, None, 5), 49.0)
        self.assertEqual(get_result(8, None, 6), 2.8284)

    def test_get_result__divide_by_zero(self):
        self.assertEqual(get_result(5.0, 0.0, 4), None)
        self.assertEqual(get_result(10, 0.0, 4), None)
        self.assertEqual(get_result(-2, 0.0, 4), None)
        
    def test_check_num_value(self):
        self.assertEqual(check_num_value(1), 1.0)
        self.assertEqual(check_num_value(2.0), 2.0)
        self.assertEqual(check_num_value('q'), None)


if __name__ == "__main__":
    unittest.main()
        