sum = 0
minnum = []
for i in range(7):
  n = int(input())
  if n % 2 == 1:
    sum += n
    minnum.append(n)

if len(minnum) == 0:
  print(-1)
  exit()
print(sum)
print(min(minnum))