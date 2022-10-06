"""

To implement GUI

"""

import math


def new_numbers():
    try:
        num1 = int(input('Give the first number: '))
        num2 = int(input('Give the second number: '))
        return [num1, num2]

    except Exception:
        print("This input is invalid.")
        return new_numbers()


n1, n2 = new_numbers()

while True:
    try:
        action = int(input(f'\n(1) +\n(2) -\n(3) *\n(4) /\n'
                           f'(5) sin\n(6) cos\n'
                           f'(7) Change numbers\n(8) Quit\n'
                           f'Current numbers: {n1} {n2}\n'
                           f'Please select something (1-6): '))

    except ValueError:
        print("That was not a number!")
        action = 0

    if action == 1:
        print(f'Result: {n1 + n2}')
    elif action == 2:
        print(f'Result: {n1 - n2}')
    elif action == 3:
        print(f'Result: {n1 * n2}')
    elif action == 4:
        print(f'Result: {n1 / n2}')
    elif action == 5:
        print(f'Result: {math.sin(n1 / n2)}')
    elif action == 6:
        print(f'Result: {math.cos(n1 / n2)}')
    elif action == 7:
        n1, n2 = new_numbers()
    elif action == 8:
        print('Thank you!')
        exit()
