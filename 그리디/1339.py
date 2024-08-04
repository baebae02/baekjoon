import sys
input = sys.stdin.readline

N = int(input())
num = list(input().rstrip() for _ in range(N))
# num.sort(key=lambda x : (len(x), x), reverse=True)
# print(num)
d = dict()
for k in num:
  ten = len(k) - 1
  for l in k:
    if l in d:
      d[l] += 10 ** ten
    else:
      d[l] = 10 ** ten
    ten -= 1

d = sorted(d.values(), reverse=True)
print(d)
result = 0
count = 9
for m in d:
  result += count * m
  count -= 1

print(result)


# 생각치도 못한 방법 입이 떡 벌어짐 ..