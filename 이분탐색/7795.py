import sys
input = sys.stdin.readline

T = int(input())

def binary_search(N, M, a,b):
  a.sort()
  b.sort()
  cnt = 0
  start = 0
  for i in range(N):
    while True:
      if  start == M or a[i] <= b[start]:
        cnt += start
        break
      else:
        start += 1
  return cnt

for _ in range(T):
  N, M = map(int, input().split())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  print(binary_search(N, M, a,b))