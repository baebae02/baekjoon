N = int(input())
sum = 0
count = 0
while sum <= N:
  print(sum, count)
  count += 1
  sum += count
print(count-1)