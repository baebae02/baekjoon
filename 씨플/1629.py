import sys
input = sys.stdin.readline
A, B, C = map(int, input().split())


def power(C, n, r):
  result = 1
  while n:
    if n % 2 != 0:
      result *= C
    C *= C % r
    n = n // 2
  return result % r

print(power(A, B, C))

# print(A)