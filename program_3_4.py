"""4. Write a Python program to add all the numbers entered by a user
until user enters 0.
"""
total = 0
while True:
    print(f'Поточна сума: {total}')
    number = int(input('Введіть будь-яке число (або нуль для виходу): '))
    if number == 0:
        break
    total += number
