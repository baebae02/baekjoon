import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N = int(input())

graph = [[] for _ in range(N+1)]
dp = [[0, 1] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
visited[1] = True
# dp = i 번째 노드가 j일 때 필요한 얼리어댑터 수

for _ in range(N-1):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

def dfs(node):
  for next in graph[node]: # 나랑 연결된 노드들
    if visited[next] == False: # 아직 방문 안한 노드일 경우
      visited[next] = True
      dfs(next) # 부모의 얼리어댑터 수를 갱신해주기 전에 next 노드에 대해 미리 계산해야 함.
      dp[node][0] += dp[next][1] # 부모가 얼리어댑터가 아니라면 자식은 얼리어댑터야 한다.
      dp[node][1] += min(dp[next]) # 부모가 얼리어댑터라면 자식은 아니여도 된다. 가 아니라 상관없다 !! ⭐️⭐️


dfs(1)
print(dp)
print(min(dp[1]))