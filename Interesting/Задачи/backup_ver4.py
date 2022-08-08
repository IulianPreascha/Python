import zipfile
import os
import time

source = ['D:\\copy1', 'D:\\copy2']

target_dir = "D:\\backup"

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

comment = input('Введите комментарий --> ')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' +\
        comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    zipfile.mkdir(today)
    print('Каталог успешно создан', today)

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
