from collections import deque
S = list(input())
N = len(S)
q = []

for _ in range(N):
  q.append(''.join(S))
  S.pop(0)

# print(q)
q.sort()
# print(q)

for i in q:
  print(i)