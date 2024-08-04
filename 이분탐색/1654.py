import sys
input = sys.stdin.readline
K, N = map(int, input().split())
lines = []
for _ in range(K):
  lines.append(int(input()))

start, end, mid = 1, max(lines), 0
while start <= end:
  print(start, end, mid)
  mid = (start + end) // 2
  cnt = 0
  for line in lines:
      # print(line, mid, "ddd")
    cnt += line // mid
    
  # print("cnt", cnt)
  if cnt >= N:
    start = mid + 1
  else:
    end = mid - 1
print(end)
