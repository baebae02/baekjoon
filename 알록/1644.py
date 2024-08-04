N = int(input())

primes = [False, False] + [True] * (N-1)
prime_list = []
# 에라토스테네스의 체
for i in range(2, N+1):
  if primes[i]:
    prime_list.append(i)
    for j in range(2*i, N+1, i):
      primes[j] = False

start, end = 0, 0
ans = []
while True:
  sub_sum = sum(prime_list[start:end+1])
  if sub_sum == N:
    ans.append((end-start+1))
    start += 1
  if end == len(prime_list):
    break
  elif sub_sum < N:
    end += 1
  else:
    start += 1

print(len(ans))

# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97