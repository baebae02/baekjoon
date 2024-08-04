arr = []
for i in range(9):
  arr.append(list(map(int, input().split())))


col = 0
row = 0
max_num = 0
for i in range(9):
  a = max(arr[i])
  if a > max_num:
    row = i
    col = arr[i].index(a)
    max_num = a

print(max_num)
print(row+1, col+1)
