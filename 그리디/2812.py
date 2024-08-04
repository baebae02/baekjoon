from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
# n = list(input())
n = input().rstrip()
q = []
for num in n:
  while q and q[-1] < num and K > 0:
    # print(q, q[-1], num, K)
    q.pop()
    K -= 1
  q.append(num)

if K > 0:
  print(''.join(q[:-K]))
else:
  print(''.join(q))