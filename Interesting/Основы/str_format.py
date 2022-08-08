age = 26
name = 'Swaroop'

print('Возраст {0} -- {1} лет.'.format(name, age))
print('Почему {0} забавляется с этим Python?'.format(name))

# Или (the same)

print('Возраст {} -- {} лет.'.format(name, age))
print('Почему {} забавляется с этим Python?'.format(name))

# В методе format Python помещает значение каждого аргумента в обозначенное место.
# Могут быть и более детальные обозначения, как то:

# десятичное число (.) с точностью в 3 знака для плавающих:
print('{0:.3}'.format(1/3))

# заполнить подчёркиваниями (_) с центровкой текста (^) по ширине 11:
print('{0:_^11} {1:_^11}'.format('hello', 'huilo'))

# по ключевым словам:
print('{name} написал {book}'.format(name='Swaroop', book='A Byte of Python'))
