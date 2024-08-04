n = int(input())

def fibo(n):
  a = 0
  b = 1
  for i in range(2, n+1):
    temp = b
    b = b + a
    a = temp
  return b

print(fibo(n))