H, W = map(int, input().split())
blocks = list(map(int, input().split()))

maps = [[0] * W for _ in range(H)]

visited = [[0] * W for _ in range(H)]
for i in range(W):
  height = blocks[i]
  for j in range(height):
    maps[j][i] = 1

ans = 0

for i in range(1, W-1):
  left_max = max(blocks[:i])
  right_max = max(blocks[i+1:])
  
  maximum = min(left_max, right_max)

  if blocks[i] < maximum:
    ans += maximum - blocks[i]

print(ans)