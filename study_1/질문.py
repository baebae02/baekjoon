import sys
from collections import deque

n=int(input())



for a in range(n):
    count_th=deque()
    q=deque([])

    count_th=sys.stdin.readline().split()
    q=deque(sys.stdin.readline().split())

    index=[]
    for a in range(int(count_th[0])):
        index=index+[a]
    
    index=deque(index)
    index[int(count_th[1])]='target'

    order=0
    print(*q)
    while True:
        if q[0]==max(q):
            order+=1

            if index[0]=='target':
                print(order)
                break
            else:
                q.popleft()
                index.popleft()

        else:
            q.append(q[0])
            index.append(q[0])
            q.popleft()
            index.popleft()
