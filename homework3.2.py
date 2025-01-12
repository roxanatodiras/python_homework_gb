'''
В большой текстовой строке подсчитать количество встречаемых слов и
вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку.
'''


text1 = input('Please enter your text: ')

# Переводим текст в нижний регистр\
text1 = text1.lower()

# Заменяем знаки препинания на пробелы\
text1 = text1.replace('.', ' ').replace(',', ' ').replace('!', ' ').replace('?', ' ')

# Разбиваем текст на слова\
words = text1.split()

# Создаем словарь, где ключи - слова, а значения - их количество вхождений\
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


# Сортируем словарь по значениям в обратном порядке\
sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))

# Выводим 10 самых частых слов
print('10 most common words:')
for i, (word, count) in enumerate(sorted_word_count.items()):
    print(f'{word}: {count}')
    if i == 9:  # Останавливаемся после 10 слов
        break

