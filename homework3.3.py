'''
Создайте словарь со списком вещей для похода в качестве ключа и их массой в
качестве значения. Определите какие вещи влезут в рюкзак передав его
максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.
'''

# Примеры входных данных
items_weight = {'apple': 0.1,
                'banana': 0.2,
                'orange': 0.3,
                'grape': 0.4,
                'kiwi': 0.5,
                'watermelon': 0.6,
                'pear': 0.7,
                'peach': 0.8,
                'plum': 0.9,
                'melon': 1.0,
                'pen': 0.05,
                'book': 0.15,
                'toy': 0.03,
                'penny': 0.001,
                'ball': 0.02,
                'knife': 0.01,
    }

backpack_capacity = float(input('please enter the capacity of the backpack: '))

items_to_backpack = []
total_weight = 0

for k, v in items_weight.items():

    if total_weight + v > backpack_capacity:
        break
    else:
        items_to_backpack.append(k)
        total_weight += v
        print(total_weight)


print(items_to_backpack)

