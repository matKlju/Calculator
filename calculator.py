import math

operations = ['+', '-', '*', '/', '^2', 'sqrt']


def get_num_check_type(operation=0):
    # only float numbers
    if operation > 4:
        # to stop second number after exponent or sqrt operation
        return None
    while True:
        try:
            number = float(input('\nNumber:\t'))
            return number
        except TypeError:
            print('Only float numbers')
            continue


def get_operations():
    while True:
        for i in enumerate(operations, 1):
            print(f'{i[0]}. {i[1]}')

        try:
            operation = abs(int(input('Choose operation number: ')))
            if operation > 6:
                print('Choose number between 1 - 6')
                continue
            return operation
        except ValueError:
            print('Only integers!\n')
            continue


def get_result(f_number, sec_number, operation):
    if operation == 1:
        addition = round(f_number + sec_number, 2)
        return addition
    if operation == 2:
        subtraction = round(f_number - sec_number, 2)
        return subtraction
    if operation == 3:
        multiplication = round(f_number * sec_number, 2)
        return multiplication
    if operation == 4:
        if sec_number == 0.0:
            # print("Cannot divide by zero!")
            return None
        division = round(f_number / sec_number, 2)
        return division
    if operation == 5:
        exponentiation = round(f_number**2, 2)
        return exponentiation
    if operation == 6:
        square_root = round(math.sqrt(f_number), 2)
        return square_root


def main():
    while True:
        f_number = get_num_check_type()
        operation = get_operations()
        sec_number = get_num_check_type(operation)
        result = get_result(f_number, sec_number, operation)
        print(round(result, 2))


if __name__ == "__main__":
    main()
