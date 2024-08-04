from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)


visited = [False] * (N+1)
def bfs(start):
  q = deque()
  q.append(start)
  visited[start] = True
  while q:
    x = q.popleft()
    for i in graph[x]:
      if not visited[i]:
        visited[i] = True
        q.append(i)

answer = 0
for i in range(1, N+1):
  if not visited[i]:
    bfs(i)
    answer += 1

print(answer)