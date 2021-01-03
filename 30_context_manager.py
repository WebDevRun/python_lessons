# не безопасно при сбое. Поьеряет все данные
# r = open('./exmples_for_lesson_30/file.txt', 'a')

# r.write('something' + '\n')
# r.write('что-то')
# r.close()

# print('Все нормально')

# безопасно при сбое. Запишет все до сбоя
with open('./examples_for_lesson_30/file.txt', 'a') as r:
    r.write('something' + '\n')
    # 10/0
    r.write('что-то')

print('Все нормально')
