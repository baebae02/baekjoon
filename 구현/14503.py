import sys
input = sys.stdin.readline
N, M = map(int, input().split())
r, c, d = map(int, input().split())
graph = []

for i in range(N):
  graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
blank = False
# d가 0이면 북, 1이면 동, 2이면 남 3이면 서
# 백트래킹?
while True:
  # print(r, c, graph, cnt, d, blank)
  blank = False
  if graph[r][c] == 0:
    graph[r][c] = 2 # 청소함
    cnt += 1

  for i in range(4):
    nx = r + dx[i]
    ny = c + dy[i]
    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    if graph[nx][ny] == 0:
      blank = True
      # 반시계 방향을 회전
      d = (d - 1) % 4
      # print("d\n",d)
      nx2 = r + dx[d]
      ny2 = c + dy[d]
      
      if nx2 < 0 or nx2 >= N or ny2 < 0 or ny2 >= M or graph[nx2][ny2] == 1:
        continue
      # 앞쪽 칸이 청소가 안되어있을 경우 전진
      elif graph[nx2][ny2] == 0:
        r = nx2 
        c = ny2
        break
  
  if not blank:
    # 빈 칸이 없는 경우
    back = (d+2)%4
    nx = r + dx[back] # 방향을 유지한 채 후진
    ny = c + dy[back]
    if nx < 0 or nx >= N or ny < 0 or ny >= M or graph[nx][ny] == 1:
      break
    else:
      r = nx
      c = ny

print(cnt)
