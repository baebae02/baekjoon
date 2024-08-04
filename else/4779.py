

def rmstr(arr):
  l = len(arr)
  if l == 1:
    return arr
  for i in range(l//3, l//3*2):
    arr[i] = ' '
  return rmstr(arr[:(l//3)]) + [' ' for _ in range(l//3)] + rmstr(arr[(l//3*2):])
  # return rmstr(arr[:(l//3)+1]) + [None for _ in range(l//3)] + rmstr(arr[(l//3*2)+1:])



while True:
  try:
    N = int(input())
    string = ['-'] * (3**(N))
    print(''.join(rmstr(string)))
  except:
    break