N = int(input())
A = list(map(int, input().split()))
dp_increase = [1 for _ in range(N)]
dp_decrease = [1 for _ in range(N)]

# 증가하는 수열
for i in range(N):
  for j in range(0, i):
    if A[i] > A[j]:
      dp_increase[i] = max(dp_increase[i], dp_increase[j]+1)

# 감소하는 수열
for i in range(N-1, -1, -1):
  for j in range(N-1, i, -1):
    if A[i] > A[j]:
      dp_decrease[i] = max(dp_decrease[i], dp_decrease[j]+1)

# print(dp_increase)
# print(dp_decrease)

# 배열 합치기
for i in range(N):
  dp_increase[i] += dp_decrease[i]

print(max(dp_increase)-1)