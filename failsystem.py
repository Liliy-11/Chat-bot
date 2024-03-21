#работа с файлами

import os

#информация о текущем файле
print(
    os.getcwd()
)

#resylt
#d:/web/412/tspu-group-412-main/failsystem.py

#получить список файлов в директории
print (
    os.listdir()
)

#проверка есть ли директории
print(
    os.path.isdir('home works')
)

for f in os.listdir():
    print(
        f'is dir: {f}', os.path.isdir(f)
    )
