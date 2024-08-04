N, M = map(int, input().split())
m = [list(map(int, list(input()))) for _ in range(N)]
size = min(N, M)

def find_rect(size):
  for i in range(N-size+1):
    for j in range(M-size+1):
      if m[i][j] == m[i][j+size-1] == m[i+size-1][j] == m[i+size-1][j+size-1]:
        return True
  return False


# 어떤 정사각형도 변의 길이가 size보다 클 수 없음
for i in range(size, 0, -1):
  if find_rect(i):
    print(i**2)
    break

