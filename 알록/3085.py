
N = int(input())
basket = []
for _ in range(N):
  basket.append(list(input()))
# 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y

def check(x,y):
  if x >= 0 and x < N and y >= 0 and y < N:
    return True
  return False


def find_max_length():
  # 행 탐색
  max_cnt = 1
  for i in range(N):
    cnt = 1
    for j in range(1, N):
      if basket[i][j] == basket[i][j-1]:
        cnt += 1
        max_cnt = max(max_cnt, cnt)
      else:
        cnt = 1

  # 열 탐색
  for j in range(N):
    cnt = 1
    for i in range(1, N):
      if basket[i][j] == basket[i-1][j]:
        cnt += 1
        max_cnt = max(max_cnt, cnt)
      else:
        cnt = 1
  return max_cnt


def init():
  max_cnt = find_max_length()
  dx = [0, 1, 0, -1]
  dy = [1, 0, -1, 0]
  for i in range(N):
    for j in range(N):
      for k in range(4):
        if check(i + dx[k], j + dy[k]) and basket[i][j] != basket[i + dx[k]][j + dy[k]]:
          basket[i][j], basket[i + dx[k]][j + dy[k]] = basket[i + dx[k]][j + dy[k]], basket[i][j] # 바꾸기
          max_cnt = max(max_cnt, find_max_length())
          basket[i][j], basket[i + dx[k]][j + dy[k]] = basket[i + dx[k]][j + dy[k]], basket[i][j] # 다시 돌려놓기

  return max_cnt

print(init())