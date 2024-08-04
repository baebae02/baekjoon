import copy
from collections import deque
import sys 
input = sys.stdin.readline
N, M = map(int, input().split())
graph = []
dx = [0, 0, 1, -1] # 상 하 오른 왼
dy = [1, -1, 0, 0]
for i in range(N):
  graph.append(list(map(int, input().split())))

# 바이러스 퍼트리기 BFS
def virus():
  copy_graph = copy.deepcopy(graph)
  virus_queue = deque()

  # 바이러스 모으기
  for i in range(N):
    for j in range(M):
      if copy_graph[i][j] == 2:
        virus_queue.append((i,j))

  # 바이러스 퍼트리기
  while virus_queue:
    x, y = virus_queue.popleft()

    # 상하좌우 비교하는 법
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
      if copy_graph[nx][ny] == 0:
        virus_queue.append((nx, ny))
        copy_graph[nx][ny] = 2
  
  # 다 퍼지고 나서 남은 공간 세기
  global answer
  cnt = 0
  for i in range(N):
    cnt += copy_graph[i].count(0)
  answer = max(answer, cnt)

  


# 벽 세우기 백 트래킹
def makewall(cnt):
  if cnt == 3:
    virus()
    return
  for i in range(N):
    for j in range(M):
      if graph[i][j] == 0:
        graph[i][j] = 1 # 빈칸이면 벽을 세우고
        makewall(cnt+1) # 다음 벽 세우러 가기 
        graph[i][j] = 0 # 벽 허물기 

answer = 0
makewall(0)
print(answer)