N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
maximum = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(cnt, i, j, value):
  global maximum
  if cnt == 4:
    maximum = max(maximum, value)
    return
  
  # 상하좌우
  for t in range(4):
    x = i + dx[t]
    y = j + dy[t]
    if 0 <= x < N and 0 <= y < M and not visited[x][y]:
      visited[x][y] = True
      dfs(cnt+1, x, y, value+maps[x][y])
      visited[x][y] = False


def exception(i, j):
  global maximum
  for n in range(4): # ㅗ, ㅜ, ㅓ, ㅏ 4번
    tmpsum = maps[i][j]
    for k in range(3): # 나 빼고 상하좌우 3번
      x = i + dx[(n+k)%4]
      y = j + dy[(n+k)%4]
      if 0 <= x < N and 0 <= y < M:
        tmpsum += maps[x][y]
      else:
        tmpsum = 0
        break
    maximum = max(maximum, tmpsum)
                 


for i in range(N):
  for j in range(M):
    # 상하좌우 이동하면서 4개 maximum 찾기
    visited[i][j] = True
    dfs(1, i, j, maps[i][j])
    visited[i][j] = False

    # 현재 위치 기준으로 ㅗ, ㅜ, ㅓ, ㅏ maximum 찾기
    exception(i, j)

print(maximum)