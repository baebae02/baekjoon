from collections import deque

n, w, L = map(int, input().split())
q = deque(map(int, input().split()))
time = 0
current = deque()
while q or current:
  if current and current[0][1] == w:
    current.popleft()

  for i in range(len(current)):
    current[i][1] += 1

  if q:
    if sum(c[0] for c in current) + q[0] <= L:
      current.append([q[0], 1])
      q.popleft()
  time += 1

print(time)