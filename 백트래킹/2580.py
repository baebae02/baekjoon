import sys
sdocu = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if sdocu[i][j] == 0:
            blank.append([i,j])

def row(a, n): # 가로
    for i in range(9):
        if n == sdocu[a][i]: # 이미 있으면
            return False
    return True

def column(a, n): # 세로
    for i in range(9):
        if n == sdocu[i][a]: # 이미 있으면
            return False
    return True

def square(y, x, n): # 3x3 칸
    for i in range(3):
        for j in range(3):
            if n == sdocu[y//3 * 3 + i][x//3 * 3 + j]: # 칸내에 이미 있으면
                return False
    return True

def backtracking(n):
  if n == len(blank):
    for x in sdocu:
      print(*x)
    exit()
  
  for i in range(1, 10):
    y = blank[n][0]
    x = blank[n][1]
    if column(x,i) and row(y,i) and square(y, x, i):
        sdocu[y][x] = i
        backtracking(n+1)
        sdocu[y][x] = 0

backtracking(0)