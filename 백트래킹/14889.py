import sys
input = sys.stdin.readline
N = int(input())
maps = []
start_team = []
link_team = []
visited = [False for _ in range(N+1)]
for _ in range(N):
  maps.append(list(map(int, input().split())))

INF = 2147000000
minimum = INF

def backtracking(depth, idx):
  global minimum
  if depth == N // 2:
    start_team_total = 0
    link_team_total = 0
    # total 계산해서 minimum이랑 비교
    for i in range(1, N+1):
      for j in range(1, N+1):
        if visited[i] and visited[j]:
          start_team_total += maps[i-1][j-1]
        elif not visited[i] and not visited[j]:
          link_team_total += maps[i-1][j-1]

    minimum = min(minimum, abs(start_team_total - link_team_total))
    return
  for i in range(idx, N+1):
    if not visited[i]:
      visited[i] = True
      backtracking(depth + 1, i+1)
      visited[i] = False


backtracking(0, 1)
print(minimum)


# 첫번째 시도. 리스트에 추가 & 빼기로 백트래킹
# 두번째 시도. 시간초과 -> visited 로 리스트 탐색 대신 방문 여부 확인
# 세번째 시도. 시간초과 -> for 문 전체 탐색이 아닌 idx 이후로 탐색