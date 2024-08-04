from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
queue = deque()
for i in range(N):
  cmd = list(map(int,input().split()))
  if cmd[0] == 1:
    queue.append(cmd[1])
  elif cmd[0] == 2:
    if len(queue)== 0:
      print(-1)
    else:
      print(queue.pop())
  elif cmd[0] == 3:
    print(len(queue))
  elif cmd[0] == 4:
    print(1 if len(queue) == 0 else 0)
  elif cmd[0] == 5:
    if len(queue) == 0: 
      print(-1)
    elif len(queue) > 0: 
      print(queue[-1])
  print(cmd, queue)
    
