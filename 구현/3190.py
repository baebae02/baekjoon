from collections import deque
N = int(input()) # 지도 크기
maps = [[0] * (N+1) for _ in range(N+1)]

directions = []
snakes = deque()

K = int(input()) # 사과 개수
for _ in range(K):
  x, y = map(int, input().split())
  maps[x][y] = 2

L = int(input()) # 방향 변환 횟수
for _ in range(L):
  X, C = input().split()
  directions.append([int(X),C])

time = 0
cur_x = 1
cur_y = 1
dx = [0, 1, 0, -1] # 0: 북, 1: 동, 2: 남, 3: 서
dy = [1, 0, -1, 0]

cur_dir = 0
snakes.append((cur_x, cur_y))

while True:
  # print(time, x, y, cur_x, cur_y)
  x = 0
  y = 0
  time += 1
  x = cur_x + dx[cur_dir]
  y = cur_y + dy[cur_dir]
  # print(time, x, y, "2")
  # 종료되는 경우
  if x <= 0 or y <= 0 or x > N or y > N or (x,y) in snakes:
    break

  # 사과를 먹지 못하는 경우
  if maps[x][y] != 2:
    a, b = snakes.popleft()
    maps[a][b] = 0
  
  # print(time, x, y, "3")
  # 사과를 먹은 경우
  snakes.append((x,y))
  maps[x][y] = 1
  cur_x = x
  cur_y = y

  # 방향 전환이 있을 경우
  for X, c in directions:
    if time == X:
      if c == 'L':
        cur_dir = ( cur_dir - 1 + 4 ) % 4
      elif c == 'D':
        cur_dir = (cur_dir + 1) % 4


print(time)