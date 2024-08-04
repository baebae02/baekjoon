while True:
  try:
    n = int(input())
  except:
    break
  one_arr = 1
  while True:
    if one_arr % n == 0:
      print(len(str(one_arr)))
      break
    else:
      one_arr = one_arr * 10 + 1
