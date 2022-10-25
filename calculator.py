import math

operations = ['+', '-', '*', '/', '^2', 'sqrt']


def check_value_type(number, operation=0):
    try:
        return float(number)
    except AttributeError:
        return False

    # # only float numbers
    # if operation > 4:
    #     # to stop second number after exponent or sqrt operation
    #     return None
    # while True:
    #     try:
    #         number = float(input('\nNumber:\t'))
    #         return number
    #     except ValueError:
    #         print('Only float numbers')
    #         continue
    # pass


def get_operations():
    # while True:
    #     for i in enumerate(operations, 1):
    #         print(f'{i[0]}. {i[1]}')
    #
    #     try:
    #         operation = abs(int(input('Choose operation: ')))
    #         if operation > 6:
    #             print('Choose number between 1 - 6')
    #             continue
    #         return operation
    #     except ValueError:
    #         print('Only float numbers!\n')
    #         continue
    pass


def get_result(f_number, sec_number, operation):
    if operation == 1:
        result = f_number + sec_number
        return result
    if operation == 2:
        result = f_number - sec_number
        return result
    if operation == 3:
        result = f_number * sec_number
        return result
    if operation == 4:
        if sec_number == 0.0:
            print("Cannot divide by zero!")
            return None
        result = f_number / sec_number
        return result
    if operation == 5:
        result = f_number**2
        return result
    if operation == 6:
        result = round(math.sqrt(f_number))
        return result


def main():
    while True:
        if check_value_type(f_number := input('\nNumber:\t')):
            pass
        elif check_value_type(operation := input('Choose operation: ')):
            pass
        elif check_value_type(sec_number := input('\nNumber:\t')):
            pass
        else:
            print('Only integers and ')
            continue

        result = get_result(f_number, sec_number, operation)
        print(f'Result: {round(result, 2)}')


if __name__ == "__main__":
    main()
