n = int(input())
paper = [[False for _ in range(100)] for _ in range(100)]

for i in range(n):
  x, y = map(int, input().split())
  for j in range(x, x+10):
    for k in range(y, y+10):
      paper[j][k] = True

cnt = 0
for i in range(100):
  cnt += paper[i].count(True)
print(cnt)