limiting_number = 7

while True:
  var = input('Введите число(q для выхода): ')
  try:
    if var == 'q':
      print('Пока')
      break
    elif int(var) > limiting_number:
      print('Привет')
    else:
      print('Введенное число меньше %s' % limiting_number)
  except Exception as other:
    print("Введенное Вами значение не число:", other)
