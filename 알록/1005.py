T = int(input())
for _ in range(T):
  N, K = map(int, input().split())
  D = list(map(int, input().split()))
  D = [0] + D
  DP = [[] for _ in range(N+1)]
  for _ in range(K):
    A, B = map(int, input().split())
    # print(A, B)
    DP[A].append(B)
  W = int(input())

  for i in range(1, N+1):
    if DP[i] != []:
      for j in DP[i]:
        if D[j] < D[i] + D[j]:
          D[j] += D[i]
        print(D)

# 10 20 1 5 8 7 1 43
39
