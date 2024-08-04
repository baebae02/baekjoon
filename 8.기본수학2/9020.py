import math

def findprime(n):
  arr = [True for _ in range(n+1)]
  arr[0] = False
  arr[1] = False
  for i in range(2, int(math.sqrt(n)+1)):
    if arr[i] == True:
      j = 2
      while i * j <= n:
        arr[i*j] = False
        j+=1
  return arr


t = int(input())
for i in range(t):
  n = int(input())
  arr = findprime(n)
  ans = [100000, 0, 0]
  for i in range(int((len(arr) // 2)+1)):
    if arr[i] == True and arr[n-i] == True:
      cur_diff = abs(i * 2 - n)
      if ans[0] > cur_diff:
        ans[0] = cur_diff
        ans[1] = i
        ans[2] = n - i
  print(ans[1], ans[2])

