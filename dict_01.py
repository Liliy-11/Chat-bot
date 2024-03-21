# словари

man = {
    'name': 'John',
    'age': 33,
    'last_name': 'Doe',
    'hobby': 'swimming',
    # 'addres': '2265 Mount Road',
    'addres': {
        'city': 'Los Angeles',
        'state': 'CA',
        'zip': 90210,
        'street': '2265 Mount Road'
    },
    'phone': None,
}

print(
    'person', man,
)

# получение значений

print(
    'name:', man.get('name'),
    'name:', man['name'],
    # 'email:', man['email'],
    'email:', man.get('email', None),
)
# name: John name: John email: None

# получение только значений словаря
print(
    man.values()
)
# dict_values(['John', 33, 'Doe', 'swimming', {'city': 'Los Angeles', 'state': 'CA', 'zip': 90210, 'street': '2265 Mount Road'}, None])

# получить только ключи
print(
    man.keys()
)
# dict_keys(['name', 'age', 'last_name', 'hobby', 'addres', 'phone'])

# получение пар ключ-значение
print(
    man.items()
)
# dict_items([('name', 'John'), ('age', 33), ('last_name', 'Doe'), ('hobby', 'swimming'), ('addres', {'city': 'Los Angeles', 'state': 'CA', 'zip': 90210, 'street': '2265 Mount Road'}), ('phone', None)])

for k in man.items():
    print(k)

for k in man.values():
    print(k)

# Добавление значения
    
man['birthday'] = '2005-06-13'

print(
    'man:',man
)