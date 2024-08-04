from collections import deque

N = int(input())
nums = []
for _ in range(N):
  nums.append(int(input()))

# nums.sort()
# 5
# 17
# 23
# 14
# 83

# 12 6 9 69
# -> 9 3 6 60
def gcd(a, b):
  while b:
    a, b = b, a % b
  return a

def get_divisor(n):
  ans = set()
  for i in range(2, int(n**0.5)+1):
    if n % i == 0:
      ans.add(i)
      ans.add(n // i)
  return ans

for i in range(N-1):
  nums[i] = abs(nums[i+1] - nums[i])
del nums[-1]
gcd_value = nums[0]
for j in range(N-1):
  gcd_value = gcd(gcd_value, nums[j])

result = get_divisor(gcd_value)
result.add(gcd_value)

print(*sorted(result))


