import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

def gcd(a, b):
    while a % b > 0:
        c = a % b
        a = b
        b = c
    return b

arr = deque()
for _ in range(N):
  arr.append(int(input()))

gcd_result = arr[-1] - arr[0]
for j in range(0, len(arr)-1):
  gcd_result = gcd(gcd_result, (arr[j+1] - arr[j]))
print(((arr[-1] - arr[0]) // gcd_result) + 1 - N)
