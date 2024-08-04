import sys
input = sys.stdin.readline

prime_arr = [True] * 1000001
prime_arr[0] = False

def solution():
  c = int(1000001**0.5)
  for i in range(2, c+1):
    if prime_arr[i]:
      for j in range(i+i, 1000001, i):
        prime_arr[j] = False

  while True:
    n = int(input())
    if n == 0:
      break
    for i in range(3, n):
        if prime_arr[i] and prime_arr[n - i]:
            print("%d = %d + %d" % (n, i, n - i))
            break
    else:
        print("Goldbach's conjecture is wrong.")

solution()