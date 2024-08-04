#유클리드 호제법
#a = bq + r이라 할 때 gcd(a,b) = gcd(b,r)

a, b = map(int, input().split())
final_a, final_b = a, b
while True:
  r = a % b
  q = a // b
  if r == 0:
    break
  a = b
  b = r

# 24 = 18 * 1 + 6
# a = 18, b = 6

print(b)
print(int(final_a*final_b/b))


# 모범답안
# 최대공약수 = GDD 최소공배수 = LCM
# a, b = map(int, input().split())

# def gcd(a, b):
# 	while b > 0:
# 		a, b = b, a % b
# 	return a

# def lcm(a, b):
# 	return a * b / gcd(a, b)
# print(gcd(a, b))
# print(int(lcm(a, b)))