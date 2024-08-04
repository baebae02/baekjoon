code1cnt = 0
code2cnt = 0
def fib(n): 
  global code1cnt
  if (n == 1 or n == 2):
    code1cnt += 1
    return 1  # 코드1
  else:
    return (fib(n - 1) + fib(n - 2))

N = int(input())
f = [0] * (N+1)
def fibonacci(n):
    global code2cnt
    f[1] = 1
    f[2] = 1
    for i in range (3,n+1):
        f[i] = f[i - 1] + f[i - 2]  # 코드2
        code2cnt += 1
    return f[n]

fib(N)
fibonacci(N)
print(code1cnt)
print(code2cnt)