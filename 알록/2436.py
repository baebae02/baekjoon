GCD, LCM = map(int, input().split())

def Euclidean(a, b):
    r = a % b
    while r != 0:
        a, b = b, r
        r = a % b
    return b

#13249
ans = [100000000, 100000000]
n = LCM // GCD
# n = 43243200
for i in range(int(n ** 0.5) + 1, 0, -1):
    # print(i, ans)
    if n % i == 0 and Euclidean(i, n // i) == 1:
          # print(n, i, n // i)
          s = sum(ans)
          if s > i + n // i:
              ans = [i, n // i]
              break
ans.sort()
print(ans[0] * GCD, ans[1] * GCD)

