from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
q = deque()
for _ in range(N):
  cmd = input().split()
  if cmd[0] == 'pop_front':
    if q:
      print(q.popleft())
    else:
      print(-1)
  elif cmd[0] == 'pop_back':
    if q:
      print(q.pop())
    else:
      print(-1)
  elif cmd[0] == 'size':
    print(len(q))
  elif cmd[0] == 'empty':
    print(0 if q else 1)
  elif cmd[0] == 'front':
    if q:
      print(q[0])
    else:
      print(-1)
  elif cmd[0] == 'back':
    if q:
      print(q[-1])
    else:
      print(-1)
  elif cmd[0] == 'push_front':
    q.appendleft(cmd[1])
  elif cmd[0] == 'push_back':
    q.append(cmd[1])