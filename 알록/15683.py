N, M = map(int, input().split())
office = []
for _ in range(N):
  office.append(list(map(int, input().split())))


# 방향 정의 북 : 0 동 : 1 남 : 2 서 : 3
cctv_directions = [
  [], # 0번
  [[0], [1], [2], [3]], # 1번
  [[0, 2], [1, 3]], # 2번
  [[0, 1], [1, 2], [2, 3], [3, 0]], # 3번
  [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], # 4번
  [[0, 1, 2, 3]] # 5번
]

def backtracking_search(office, cctvs):

  def mark_cctv_area(office, x, y, directions):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for direction in directions:
      nx, ny = x, y
      while 0 <= nx < N and 0 <= ny < M and office[nx][ny] != 6:
        if office[nx][ny] == 0:
          office[nx][ny] = '#'
        nx += dx[direction]
        ny += dy[direction]

  def backtracking(index, current_office):
    if index == len(cctvs):
      return sum([row.count(0) for row in current_office]) # count blind spots
    
    min_spots = float('inf')
    cctv_type, x, y = cctvs[index]
    for directions in cctv_directions[cctv_type]:
      next_office = [row[:] for row in current_office] # deep copy
      mark_cctv_area(next_office, x, y, directions)
      print(directions, "\n", next_office, "\n", min_spots)

      # 현재까지의 최소값보다 이미 크다면 더 이상 탐색하지 않음.
      current_spots = sum([row.count(0) for row in next_office])
      # if current_spots < min_spots:
        # print("directions", directions, cctv_type)
      min_spots = min(min_spots, backtracking(index + 1, next_office))

    return min_spots
  return backtracking(0, office)

print(backtracking_search(office, [(office[i][j], i, j) for i in range(N) for j in range(M) if 1 <= office[i][j] <= 5]))