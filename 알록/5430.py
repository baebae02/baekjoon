from collections import deque
T = int(input())

for _ in range(T):
  p = list(input())
  n = int(input())
  x = input().strip('[]')
  x = deque(x.split(",")) if n != 0 else deque()

  to_right = True
  for i in p:
    if i == 'R':
      to_right = not to_right
    else:
      if not x:  # 리스트가 비어있을 때
        print("error")
        break
      if to_right:
        x.popleft()
      else:
        x.pop()
  if to_right:
    print("[" + ",".join(x) + "]", sep='')
  else:
    x.reverse()
    print("[" + ",".join(x) + "]", sep='')
