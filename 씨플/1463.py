N = int(input())
# 피보나치 수열처럼 ! 이전 결과를 반영해서 최솟값을 계산하는 거임.
# N의 수가 10^6까지 인 것도 힌트. 
DP = [0] * 1000001

for i in range(2, N+1):
  
  # 1을 더하는 경우
  DP[i] = DP[i-1] + 1

  # 2로 나눠지는 경우
  if i % 2 == 0:
    DP[i] = min(DP[i], DP[i//2] + 1)
  
  # 3으로 나눠지는 경우
  if i % 3 == 0:
    DP[i] = min(DP[i], DP[i//3] + 1)


print(DP[N])