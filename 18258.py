import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
queue = deque([])
for _ in range(n):
    sen = list(sys.stdin.readline().rstrip().split())
    if sen[0] == "push":
        queue.append(sen[1])
    elif sen[0] == "pop":
        print(-1 if len(queue) == 0 else queue.popleft())
    elif sen[0] == "front":
        print(-1 if len(queue) == 0 else queue[0])
    elif sen[0] == "back":
        print(-1 if len(queue) == 0 else queue[-1]) 
    elif sen[0] == "size":
        print(len(queue))
    elif sen[0] == "empty":
        print(1 if len(queue) == 0 else 0)
