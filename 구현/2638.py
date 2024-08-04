import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
maps = []
for _ in range(N):
  maps.append(list(map(int, input().split())))

time = 0
dx = [0, 1, 0 ,-1]
dy = [1, 0, -1, 0]

def check_zero():
  for i in range(N):
    if maps[i].count(1) > 0:
      return False
  return True

def air_bfs():
  q = deque()
  q.append([0,0]) # 0,0부터 탐색
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<N and 0<=ny<M:
        if visited[nx][ny] == 0 and maps[nx][ny] == 0: # 방문 안한 공기면
          q.append([nx,ny])
          visited[nx][ny] = 1
        elif maps[nx][ny] == 1: # 방문 했던 안했던 치즈이면 
          visited[nx][ny] += 1




while True:
  visited = [[0] * M for _ in range(N)]
  air_bfs()
  time += 1

  # 2번 이상 방문한 곳은 녹음
  for i in range(N):
      for j in range(M):
        if visited[i][j] >= 2:
          maps[i][j] = 0
  # 치즈가 다 녹았으면 종료
  if check_zero():
    print(time)
    break

  

  