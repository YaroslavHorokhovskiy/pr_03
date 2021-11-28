"""5. Write a Python Program to reverse a number. For example, if user enters
123 as input then 321 is printed as output.
"""

number = int(input('Введіть будь-яке ціле число: '))

reversed_number = 0

while number > 0:
  remainder = number % 10
  reversed_number = reversed_number * 10 + remainder
  number = number // 10

print(f'Перевернуте число: {reversed_number}')
