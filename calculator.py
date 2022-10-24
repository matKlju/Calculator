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
        result = round(f_number + sec_number, 2)
        return result
    if operation == 2:
        result = round(f_number - sec_number, 2)
        return result
    if operation == 3:
        result = round(f_number * sec_number, 2)
        return result
    if operation == 4:
        if sec_number == 0.0:
            print("Cannot divide by zero!")
            return None
        result = round(f_number / sec_number, 2)
        return result
    if operation == 5:
        result = round(f_number**2, 2)
        return result
    if operation == 6:
        result = round(math.sqrt(f_number), 2)
        return result


def main():
    while True:
        f_number = get_num_check_type()
        operation = get_operations()
        sec_number = get_num_check_type(operation)
        result = get_result(f_number, sec_number, operation)
        print(round(result, 2))


if __name__ == "__main__":
    main()
