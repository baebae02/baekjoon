import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
dp = [-1] * N

for i in range(N-2, -1, -1):
  if A[i] < A[i+1]:
    dp[i] = A[i+1]
  elif A[i] >= A[i+1]:
    if dp[i+1] <= A[i]:
      index = i+1
      while dp[index] <= A[i]:
        if dp[index] == -1:
          break
        if dp[index] > A[i]:
          break
        index += 1
      dp[i] = dp[index]
    else:
      dp[i] = dp[i+1]

print(*dp, sep=' ')