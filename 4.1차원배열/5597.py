li = [i for i in range(1, 31)]
for i in range(28):
  a = int(input())
  if a in li:
    li.remove(a)

li.sort()

for i in li:
  print(i)

# 숏코딩 = dict의 차집합 이용하기