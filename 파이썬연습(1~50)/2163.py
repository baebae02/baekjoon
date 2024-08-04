N, M = map(int, input().split())
if N > M:
  print((N-1) + (M-1)*N)
else:
  print((M-1) + (N-1)*M)