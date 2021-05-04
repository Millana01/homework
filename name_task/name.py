true_name = 'Вячеслав'

while True:
  name = input('Введите имя(нажмите q для выхода): ')
  if name == 'q':
    print('Пока')
    break
  elif name.capitalize() == true_name:
    print('Привет, %s' % true_name)
  else:
    print('Нет такого имени')
    
    