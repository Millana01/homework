while True:
  number_list = [int(x) for x in input().split()]
  for x in number_list:
    if x % 3 == 0:
      print(x)
    else:
      continue


