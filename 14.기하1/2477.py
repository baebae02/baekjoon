

K = int(input())

li = [[],[],[],[]]
ans = []
#  동쪽은 1, 서쪽은 2, 남쪽은 3, 북쪽은 4
direction = [1, -1, -1, +1]
map = []
for i in range(6):
  di, num = input().split()
  di = int(di)
  num = int(num)
  map.append([direction[di-1], num])
  li[di-1].append(num)
  

for i in range(1, 6):
  if i >= 5: i = i - 6
  if map[i][0] != map[i-1][0] and map[i][0] != map[i+1][0]:
    ans.append(map[i][1] * map[i+1][1])
    print(i)
    break

sum = 1
for i in li:
  if len(i) == 1:
    sum = sum * i[0]
print((sum - ans[0]) * K)