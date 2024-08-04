N, K = map(int, input().split())
def fact(n):
  if n == 0:
    return 1
  return n * fact(n-1)


print((fact(N) // fact(K) // fact(N-K)) % 10007)