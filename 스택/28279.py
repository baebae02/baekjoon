from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
deq = deque()

for _ in range(N):
  cmd = input()
  # l=list(map(int,sys.stdin.readline().strip().split()))로 해결가능하다. 기억하자 strip() !!
  if cmd[0] == '1' or cmd[0] == '2':
    cmd, X = map(int, cmd.split())
    if cmd == 1:
      deq.appendleft(X)
    elif cmd == 2:
      deq.append(X)
  elif cmd[0] == '3':
    print(deq.popleft() if len(deq) > 0 else -1)
  elif cmd[0] == '4':
    print(deq.pop() if len(deq) > 0 else -1)
  elif cmd[0] == '5':
    print(len(deq))
  elif cmd[0] == '6':
    print(1 if len(deq) == 0 else 0)
  elif cmd[0] == '7':
    print(deq[0] if len(deq) > 0 else -1)
  elif cmd[0] == '8':
    print(deq[-1] if len(deq) > 0 else -1)