import unittest
from math_quiz import function_A, function_B, function_C


class TestMathGame(unittest.TestCase):
    
    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_A(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        # # Test if function_B returns one of the valid operators
        valid_operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random selections
            operator = function_B()
            self.assertIn(operator, valid_operators)

    def test_function_C(self):
             # Test cases for function_C, including addition, subtraction, and multiplication
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (10, 3, '-', '10 - 3', 7),
            (4, 6, '*', '4 * 6', 24),
            (9, 5, '+', '9 + 5', 14),
            (7, 4, '-', '7 - 4', 3),
            (3, 3, '*', '3 * 3', 9)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = function_C(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
