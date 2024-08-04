# import sys
# input = sys.stdin.readline

# T=int(input())

# def is_prime(N):
#   for i in range(2, int(N**0.5)+1):
#     if N % i == 0:
#       return False
#   return True

# def find_gold(N):
#   cnt = 0
#   for i in range(2, (N//2)+1):
#     if is_prime(i) and is_prime(N-i):
#       cnt += 1
#   return cnt

# for _ in range(T):
#   N = int(input())
#   print(find_gold(N))

# 위에는 틀린 풀이
# 틀린 이유 : 일반적인 소수 찾기를 시도하면 시간 초과가 난다. 에라토스테네스의 체를 활용해야 한다.
# 2 < N ≤ 1,000,000 라서 !

sieve = [False, False] + [True] * 999999
for i in range(2, 1000000):
  if sieve[i]:
    for j in range(i*2, 1000001, i):
      sieve[j] = False


T = int(input())
for _ in range(T):
  N = int(input())
  cnt = 0
  for k in range(2, N//2+1):
    if sieve[k] and sieve[N-k]:
      cnt += 1
  print(cnt)

  