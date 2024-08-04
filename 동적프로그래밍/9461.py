fib = [0] * 101
fib[1]=1
fib[2]=1
fib[3]=1

def fibonacci(n):
  if n == 1:
    return 1
  if n == 2:
    return 1
  if n == 3:
    return 1
  if fib[n]:
    return fib[n]
  else:
    fib[n] = fibonacci(n-2) + fibonacci(n-3)
    return fib[n]

T = int(input())
for _ in range(T):
  n = int(input())
  print(fibonacci(n))