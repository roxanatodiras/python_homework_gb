'''

Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
'''

from collections import Counter

list1 = [1, 2, 3, 4, 5, 6, 1, 2, 7, 7, 7]
dict2 = Counter(list1)


list2 = []
for k, v in dict2.items():
    if v == 2:
        list2.append(k)
print(list2)
