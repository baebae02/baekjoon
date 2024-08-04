import sys
import copy
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())

graph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 지도 입력 받기
for i in range(N):
  graph.append(list(map(int, input().split())))

chicken = deque([])
house = deque([])

select = deque([])
for a in range(N):
    for b in range(N):
        if graph[a][b] == 1:        # 집 위치 추가
            house.append((a, b))
        elif graph[a][b] == 2:      # 치킨집 위치 추가
            chicken.append((a, b))

def cal(): # 치킨 거리 계산하기 BFS
  city_distance = 0
  global answer
  for h in house:
    min_distance = float('inf')
    for c in select:
      min_distance = min(min_distance, abs(c[0]-h[0]) + abs(c[1]-h[1]))
    city_distance += min_distance
  answer = min(answer, city_distance)

# 치킨집 M개 고르기, 즉 chicken - M개 폐업시키기
def selectChicken(cnt, who):
  if cnt == M:
    cal() # 치킨 거리 계산하기
    return
  for i in range(who, len(chicken)):
    select.append(chicken[i])
    selectChicken(cnt+1, i+1)
    select.pop()

answer = float('inf')
selectChicken(0, 0)
print(answer)


# 백 트래킹 안에서 select 즉 치킨 큐를 관리함으로써 for 문 중첩 방지