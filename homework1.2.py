'''
Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
Используйте правило для проверки: “Число является простым, 
сли делится нацело только на единицу и на себя”. 
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
'''

START_NUM = 2
STOP_NUM = 100000
num1 = int(input(f'Please input a number from {START_NUM} to {STOP_NUM}: '))

if num1 >= START_NUM or num1 <= STOP_NUM:
    if (num1 % 2 == 0 and num1 != 2) or (num1 % 3 == 0 and num1 != 3) or (num1 % 5 == 0 and num1 != 5):
        print('the number is composite')
    else:
        print('the number is prime')
else:
    print('the number inserted is out of the range')