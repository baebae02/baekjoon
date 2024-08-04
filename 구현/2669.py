maps = [[False] * 101 for _ in range(101)]

maximum = 0
for _ in range(4):
  x1, y1, x2, y2 = map(int, input().split())
  maximum = max(maximum, x1, y1, x2, y2)
  for x in range(x1, x2):
    for y in range(y1, y2):
      maps[x][y] = True

cnt = 0

for i in range(maximum):
  true_cnt = maps[i].count(True) 
  # print(i, true_cnt - 1)
  if true_cnt > 0:
    cnt += true_cnt

print(cnt)