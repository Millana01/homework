#!/bin/bash

file_path=$PWD/hey.py

python_script='limiting_number = 7\n
\nwhile True:\n
  \tvar = input("Введите число(q для выхода): ")\n
  \ttry:\n
    \t\tif var == "q":\n
      \t\t\tprint("Пока")\n
      \t\t\tbreak\n
    \t\telif int(var) > limiting_number:\n
      \t\t\tprint("Привет")\n
    \t\telse:\n
      \t\t\tprint("Введенное число меньше %s" % limiting_number)\n
  \texcept Exception as other:\n
    \t\tprint("Введенное Вами значение не число:", other)'

echo "Создаем файл hey.py в $PWD и записываем скрипт в этот файл"
touch $file_path && echo -e $python_script > $file_path
python3 $file_path
echo "Удаляем файл hey.py"
rm $file_path

