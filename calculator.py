import math


def check_num_value(number):
    try:
        return float(number)
    except ValueError:
        return None


def get_result(num1, num2, operation):
    if operation == 1.0:
        result = num1 + num2
        return round(result, 4)

    if operation == 2.0:
        result = num1 - num2
        return round(result, 4)

    if operation == 3.0:
        result = num1 * num2
        return round(result, 4)

    if operation == 4.0:
        if num2 == 0.0:
            return None
        result = num1 / num2
        return round(result, 4)

    if operation == 5.0:
        result = num1 ** 2
        return round(result, 4)

    if operation == 6.0:
        result = round(math.sqrt(num1), 4)
        return round(result, 4)


def main():
    while True:
        operations = ['+', '-', '*', '/', '^2', 'sqrt']

        while True:
            num1 = input('\nNumber1:\t')
            num1 = check_num_value(num1)
            if not num1:
                print('\nOnly numbers!')
                continue
            else:
                break

        for i in enumerate(operations, 1):
            print(f'{i[0]}. {i[1]}')

        while True:
            operation = input('\nOperation:\t')
            operation = check_num_value(operation)
            if not operation:
                print('\nOnly numbers!')
                continue
            else:
                break

        if operation in [5.0, 6.0]:
            result = get_result(num1, None, operation)
            print(f'\nResult:\t{round(result, 4)}')
            continue

        while True:
            num2 = input('\nNumber2:\t')
            num2 = check_num_value(num2)
            if num2 == 0.0:
                print('Cannot divide by zero!')
                continue
            if not num2:
                print('\nOnly numbers!')
                continue
            else:
                break

        result = get_result(num1, num2, operation)
        print(f'\nResult:\t{result}')



if __name__ == "__main__":
    main()
