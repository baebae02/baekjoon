import sys
sys.setrecursionlimit(10**9)
M, N = map(int, input().split())
building = []
for _ in range(M):
  building.append(list(map(int, input().split())))

dp = [[-1] * N for _ in range(M)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y):

  # (0,0) 부터 탐색 시작
  if x == 0 and y == 0:
    return 1
  
  # 이미 방문한 곳이면 dp 값 그대로 리턴
  if dp[x][y] != -1:
    return dp[x][y]
  
  # 방문 표시
  dp[x][y] = 0
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < M and 0 <= ny < N:
      if building[x][y] < building[nx][ny]:
        # print(dp, nx, ny)
        dp[x][y] += dfs(nx, ny)

  return dp[x][y]
      
dfs(M-1,N-1)
# print(dp)

# print(dfs(0,0))
print(dp[M-1][N-1])