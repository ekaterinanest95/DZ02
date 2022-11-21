# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = input('Введите вещественное число: ')
sum_of_digits = 0
count = 0
for i in number:
    if (i == ',' or i == '.'):
        sum_of_digits = sum_of_digits + 0
    else:
        sum_of_digits = sum_of_digits + int(i)
print(sum_of_digits)




