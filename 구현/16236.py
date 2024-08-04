from collections import deque
N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]

baby_shark_size = 2 # 아기 상어 크기
dx = [-1, 0, 0, 1] # 북, 서, 동, 남
dy = [0, -1, 1, 0]

cur_x, cur_y = 0, 0
# 아기 상어 찾기
for i in range(N):
  if maps[i].count(9):
    cur_x, cur_y = i, maps[i].index(9)

# 먹을 수 있는 물고기 찾기 BFS
def huntfish(x, y, shark_size):
  visited = [[0] * N for _ in range(N)] # 방문 여부 체크
  distance = [[0] * N for _ in range(N)] # 거리 확인 (정렬 때 사용)

  q = deque()
  q.append((x,y)) # 지금 위치 큐에 넣어주기
  visited[x][y] = 1
  huntable = [] # 사냥 가능한 물고기들 집합

  while q:
    temp_x, temp_y = q.popleft()
    for i in range(4):
      nx = temp_x + dx[i]
      ny = temp_y + dy[i]
      if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        if maps[nx][ny] <= shark_size:
          q.append((nx, ny))
          distance[nx][ny] = distance[temp_x][temp_y] + 1
          if 0 < maps[nx][ny] < shark_size: # 나보다 크기가 작은 물고기라면
            huntable.append((nx,ny,distance[nx][ny]))

  return sorted(huntable, key=lambda x: (-x[2], -x[0], -x[1]))

time = 0
cnt = 0 # 잡아 먹은 물고기 수
while True:
  huntable = huntfish(cur_x, cur_y, baby_shark_size)
  # print(huntable, "huntable\n")
  if len(huntable) == 0: # 도와줘 엄마상어
    break 
  
  move_x, move_y, distance = huntable.pop() # 사냥감
  # print(move_x, move_y, distance, "pop")
  time += distance # 가는 동안 시간 흐름

  maps[cur_x][cur_y] = 0 # 사냥감 있는 곳으로 이동
  cur_x = move_x 
  cur_y = move_y

  maps[cur_x][cur_y] = 0 # 잡아 먹음
  cnt += 1

  if cnt == baby_shark_size:
    baby_shark_size += 1
    cnt = 0

print(time)

