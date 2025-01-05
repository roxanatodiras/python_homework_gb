'''
Напишите программу, которая принимает
две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions
'''
from fractions import Fraction

a = int(input('please enter the first numerator: '))
b = int(input('please enter the first denominator: '))

c = int(input('please enter the second numerator: '))
d = int(input('please enter the second denominator: '))

f1 = Fraction(a, b)
f2 = Fraction(c, d)


print(f'{f1} + {f2} = {f1 + f2}')
print(f'{f1} * {f2} = {f1 * f2}')