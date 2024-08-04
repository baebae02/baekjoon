import sys
sys.setrecursionlimit(150000)
input = sys.stdin.readline


cnt = 1
N, M, R =  map(int, input().split())
E = [[] for _ in range(N+1)]

for _ in range(M):
  a, b = map(int, input().split())
  E[a].append(b)
  E[b].append(a)


visited = [0] * (N+1)
def dfs(R):
  global cnt
  visited[R] = cnt
  E[R].sort()
  for i in E[R]:
    if visited[i] == 0:
      cnt += 1
      dfs(i)

dfs(R)

for i in range(1, N+1):
  print(visited[i])