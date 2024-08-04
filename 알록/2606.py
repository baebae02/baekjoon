from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
  A, B = map(int, input().split())
  graph[A].append(B)
  graph[B].append(A)

queue = deque()
queue.append(1)
cnt = 0
visited = [False] * (N+1)
visited[1] = True
while queue:
  x = queue.popleft()
  for i in graph[x]:
    if not visited[i]:
      visited[i] = True
      queue.append(i)
      cnt += 1
  
print(cnt)