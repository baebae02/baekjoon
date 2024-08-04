import sys
input = sys.stdin.readline
N, M = map(int, input().split())
brand = [list(map(int, input().split())) for _ in range(M)]

# print(brand)
min_set = min(list(x[0] for x in brand))
min_one = min(list(x[1] for x in brand))
# print(min_set, min_one)

price = 0
while N > 0:
  if N >= 6:
    if 6 * min_one <= min_set:
      price += 6 * min_one
    else:
      price += min_set
    N -= 6
  else:
    if N * min_one <= min_set:
      price += N * min_one
    else:
      price += min_set
    break
print(price)


# 상식을 벗어난 테스트 케이스도 고려하자. 