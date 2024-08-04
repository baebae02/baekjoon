from collections import deque
N= int(input())
cards = [ i for i in range(1, N+1)]

q = deque(cards)

while len(q) > 1:
  print(q.popleft(), end=' ') # 제일 위에 있는 카드 버림
  q.append(q.popleft()) # 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.


print(q[0], end='')