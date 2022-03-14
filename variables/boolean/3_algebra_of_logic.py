"""Алгебра логики."""

number_a = 12
number_b = 14
number_c = 9

print(f'number_a = {number_a}')
print(f'number_b = {number_b}')
print(f'number_c = {number_c}\n')

print('1) Конъюнкция\n'
      + '+-------+-------+----------+\n'
      + '|   A   |   B   |  A and B |\n'
      + '+-------+-------+----------+\n'
      + '| True  | True  |   True   |\n'
      + '+-------+-------+----------+\n'
      + '| True  | False |   False  |\n'
      + '+-------+-------+----------+\n'
      + '| False | True  |   False  |\n'
      + '+-------+-------+----------+\n'
      + '| False | False |   False  |\n'
      + '+-------+-------+----------+\n'
      )

# Пример конъюнкции
print('number_a < number_b and number_a > number_c =',
      number_a < number_b and number_a > number_c)
print('number_a < number_b and number_a < number_c =',
      number_a < number_b and number_a < number_c)
print('number_a > number_b and number_a > number_c =',
      number_a > number_b and number_a > number_c)
print('number_a > number_b and number_a < number_c =',
      number_a > number_b and number_a < number_c, '\n')

print('2) Дизъюнкция\n'
      + '+-------+-------+----------+\n'
      + '|   A   |   B   |  A or B  |\n'
      + '+-------+-------+----------+\n'
      + '| True  | True  |   True   |\n'
      + '+-------+-------+----------+\n'
      + '| True  | False |   True   |\n'
      + '+-------+-------+----------+\n'
      + '| False | True  |   True   |\n'
      + '+-------+-------+----------+\n'
      + '| False | False |   False  |\n'
      + '+-------+-------+----------+\n'
      )

# Пример дизъюнкции
print('number_a < number_b or number_a > number_c =',
      number_a < number_b or number_a > number_c)
print('number_a < number_b or number_a < number_c =',
      number_a < number_b or number_a < number_c)
print('number_a > number_b or number_a > number_c =',
      number_a > number_b or number_a > number_c)
print('number_a > number_b or number_a < number_c =',
      number_a > number_b or number_a < number_c, '\n')

print('3) Инверсия\n'
      + '+-------+-------+\n'
      + '|   A   | not A |\n'
      + '+-------+-------+\n'
      + '| True  | False |\n'
      + '+-------+-------+\n'
      + '| False | True  |\n'
      + '+-------+-------+\n'
      )

# Пример инверсии
print(f'not number_a = {not number_a}')
print(f'not not number_a = {not not number_a}')
