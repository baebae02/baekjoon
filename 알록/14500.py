import sys
input = sys.stdin.readline
N, M = map(int, input().split())
maps = []
for _ in range(N):
  maps.append(list(map(int, input().split())))

maximum = 0
visited = [[False] * M for _ in range(N)]

def dfs(cnt, sum, i, j):
  global maximum
  global visited
  print(i, j, sum)
  if cnt == 3:
    maximum = max(maximum, sum)
    return
  
  # 밑, 위, 오른, 왼쪽
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  for z in range(4):
    x = i + dx[z]
    y = j + dy[z]
    if x>=0 and y>=0 and x < N and y < M and visited[x][y] == False:
      visited[x][y] = True
      dfs(cnt+1, sum+maps[x][y], x, y)
    

# dfs(0, 0, 0, 0)
# print(maximum)


for i in range(N):
  for j in range(M):
    # visited = [[False] * M for _ in range(N)]
    visited[i][j] = True
    dfs(0, maps[i][j], i, j)
    visited[i][j] = False
# visited[0][4] = True
# dfs(0, 5, 0, 4)
    # visited[i][j] = False 

print(maximum)