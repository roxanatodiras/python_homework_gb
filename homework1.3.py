'''
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
Программа должна подсказывать “больше” или “меньше” после каждой попытки. 
Для генерации случайного числа используйте код:
from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)
'''

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)
COUNT = 10


for i in range(COUNT):
    num_inp = int(input(f'try {i + 1} of {COUNT} - guess the randomized number from {LOWER_LIMIT} to {UPPER_LIMIT}: '))
    if num_inp > num:
        print('try a smaller number')
    elif num_inp < num:
        print('try a bigger number')
    else:
        print('you guessed the number')
        break
    i += 1
    print()