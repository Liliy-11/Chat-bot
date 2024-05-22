import random
import os

# 1. Функция выбора случайного(рандомного) элемента из списка

a = [1, 23, 45, 6, 2566, 66]
random_element = random.choice(a)
print('Random element:', random_element)



# 2. Получить список файлов в директории и выбрать случайный файл

folder = 'images\cats'
c = []

for files in os.scandir(folder):
    if files.is_file():
        c.append(files.name)

random_file = random.choice(c)
print('Random file:', random_file)
