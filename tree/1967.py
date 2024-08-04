import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
n = int(input())

tree = [[] for _ in range(n+1)] # []가 n개 있는 배열

for i in range(n-1):
  p, s, v = map(int, input().split())
  tree[p].append((s,v))
  tree[s].append((p,v)) # 여기선 루트 개념이 없음. 언제든 트리 뒤집어짐, 따라서 서로 저장


visited = [-1] * (n+1)
def dfs(start_node, distance):
  for next, next_distance in tree[start_node]: # 나랑 연결된 노드들 탐색
    if visited[next] == -1: # 아직 방문 안했으면
      visited[next] = distance + next_distance 
      dfs(next, distance + next_distance)
  
# 1번 노드 방문
visited[1] = 0
dfs(1, 0)
print(visited)
# 거리가 가장 먼 노드
max_distance_node = visited.index(max(visited))

# 다시 dfs 돌리기
visited = [-1] * (n+1)
visited[max_distance_node] = 0
dfs(max_distance_node, 0)
print(visited)
# max 값이 1번 구한 노드와 2번 구한 노드 사이의 거리, 즉 최장지름
print(max(visited))




