'''
Напишите программу, которая получает целое число и возвращает
его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
'''

num = int(input("Введите целое число: "))

original_num = num
hex_digits = "0123456789abcdef"
hex_representation = ""

if num == 0:
    hex_representation = "0"
else:
    while num > 0:
        remainder = num % 16
        hex_representation = hex_digits[remainder] + hex_representation
        num //= 16

print(f'Результат преобразования: {hex_representation}')
print(f'Проверка с использованием hex: {hex(original_num)}')
