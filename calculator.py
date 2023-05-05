"""
Calculator program with basic operations:
    Addition (+)
    Subtraction (-)
    Multiplication (*)
    Division (/)
    Exponentiation (**)

To add:
    Square root (√)
    Modulo (%)
    Logarithm (log)
    Trigonometric functions (sin, cos, tan)

"""
import sys
import logging
# pylint: disable=logging-fstring-interpolation

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s\n\t%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.StreamHandler()])

def calculation(num1, operand, num2):
    """Calculate result of expression"""
    if operand == '/' and num2 == 0:
        logging.error('Cannot divide by zero!')

    if operand == '+':
        return round(num1 + num2, 6)

    if operand == '-':
        return round(num1 - num2, 6)

    if operand in ('*', 'x', 'X'):
        return round(num1 * num2, 6)

    if operand == '/':
        return round(num1 / num2, 6)

    if operand in ('**', '^'):
        return round(num1 ** num2, 6)

    return 0

def operator_validation():
    """Validate supported operator"""
    operators = ('+', '-', '*', 'x', '/', '^', '**')
    while True:
        operator = input("Operation (q to quit): ")
        if operator not in operators:
            logging.warning(f'{operator} not supported!')
            continue
        if operator in ('q', 'quit'):
            return None

        return operator

def input_float_validation():
    """User input validation"""
    max_float = sys.float_info.max
    while True:
        try:
            number = input('Number (q to quit): ')
            if number.lower() in ('q', 'quit'):
                return None
            number = float(number)
            if abs(number) > max_float:
                logging.warning("Value outside reasonable range.")
                continue
            return number

        except (ValueError, TypeError):
            logging.warning("Only float numbers")

def main():
    """main function"""
    while True:
        first_number = input_float_validation()
        operation = operator_validation()
        second_number = input_float_validation()
        result = calculation(first_number, operation, second_number)
        logging.info(result)

if __name__ == "__main__":
    main()
