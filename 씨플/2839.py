N = int(input())


def remainfun():
  cnt5 = N // 5
  cnt3 = 0
  remain = N % 5
  while remain >= 0 and cnt5 >= 0:
    if remain % 3 == 0:
      cnt3 = remain // 3
      return cnt5+cnt3
    else:
      cnt5 -= 1
      cnt3 += 1
      remain = N - 5 * cnt5
  return -1

print(remainfun())