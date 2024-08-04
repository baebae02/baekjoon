N = int(input())

fib = [0] * 1000001
fib[1] = 1
fib[2] = 2

for i in range(3, N+1):
  fib[i] = (fib[i-1] + fib[i-2]) % 15746
  
print(fib[N]%15746)