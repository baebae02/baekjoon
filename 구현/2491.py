import sys
input = sys.stdin.readline
N = int(input())
S = list(map(int, input().split()))
desc = 1
desc_max = 1
asc_max = 1
asc = 1
# 증가하는 중
for i in range(1, N):
  # print(i, asc, asc_max, S[i+1], S[i])
  if S[i] >= S[i-1]:
    asc += 1
    asc_max = max(asc_max, asc)
  else:
      asc = 1

# 감소하는 중
for i in range(1, N):
  # print(i, desc, desc_max, S[i+1], S[i])
  if S[i] <= S[i-1]:
    desc += 1
    desc_max = max(desc_max, desc)
  else:
    desc = 1
print(max(asc_max, desc_max))


# max를 통한 매번 갱신도 맞지만 DP 테이블을 통한 방법도 있음.