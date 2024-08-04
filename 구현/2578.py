import sys
input = sys.stdin.readline
maps = []
speak = []
for _ in range(5):
  maps.append(list(map(int, input().split())))


for _ in range(5):
  a, b, c, d, e = map(int, input().split())
  speak.append(a)
  speak.append(b)
  speak.append(c)
  speak.append(d)
  speak.append(e)

bingo = [[0] * 5 for _ in range(5)]

def check():
  res = 0
  for i in range(5):
    row_cnt = 0
    col_cnt = 0
    for j in range(5):
      if bingo[i][j] == 1:
        row_cnt += 1
      if bingo[j][i] == 1:
        col_cnt += 1
    if row_cnt == 5:
      res += 1
    if col_cnt == 5:
      res += 1
  print("res", res)
  return res

def check_dial():
  res = 0
  right_cnt = 0
  left_cnt = 0
  for i in range(5):
    if bingo[i][5-i-1] == 1:
      right_cnt += 1
    if bingo[i][i] == 1:
      left_cnt += 1
  if right_cnt == 5:
    res += 1
  if left_cnt == 5:
    res += 1
  print("dial", res)
  return res
  

    


cnt = 0
for index, i in enumerate(speak):
  # print(index, i)
  for x in range(5):
    for y in range(5):
      if maps[x][y] == i:
        cnt = 0
        bingo[x][y] = 1
        cnt += check()
        cnt += check_dial()
        if cnt >= 3:
          print(index+1)
          exit()



