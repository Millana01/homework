target_name = 'вячеслав'

while True:
  name = input('Введите имя(нажмите q для выхода): ')
  input_name = name.lower()
  if input_name == 'q':
    print('Пока')
    break
  elif input_name == target_name:
    print('Привет, %s' % target_name.capitalize())
  else:
    print('Нет такого имени')
    
    