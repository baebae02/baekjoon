from collections import deque
T = int(input())
def cal(p):
  reversed = False
  while p:
      cmd = p.popleft()
      if cmd == 'D':
        if not str:
          print("error")
          return
        if reversed:
          str.pop()
        else:
          str.popleft()
      elif cmd == 'R':
        reversed = not reversed
  if reversed:
    str.reverse()
  print("[", ",".join(str), "]", sep='')
  return

for _ in range(T):
  p = deque(input().strip())
  n = int(input())
  arr = input()
  str = deque(arr.rstrip("]").lstrip("[").split(","))
  # print(str)
  if n == 0:
    str = deque()
  cal(p)
  

# n == 0일때 deque()로 선언하는 센스. reversed Flag로 시간 단축하기