# 11번째 해는 <1:11>
# 12번째 해는 <2:12>
# 13번째 해는 <3:1>
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
  M, N, x, y = map(int, input().split())
  i = x
  if y == N: y = 0
  answer = False
  while i <= M*N:
    # M * a + Y % 10, N * b + Y % N
    print(i, M, N, x, y)
    
    if i % N == y: # success
      print(i)
      answer = True
      break
    i += M
  if not answer:
    print(-1)
    


