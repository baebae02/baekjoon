import sys
from collections import deque 
n = int(sys.stdin.readline().rstrip())
q = deque([])
for i in range(n):
    q.append(n-i)
while True:
    if len(q) == 1:
        break
    del(q[-1])
    q.appendleft(q[-1])
    del(q[-1])
print(q[0])
