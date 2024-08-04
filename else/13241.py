num = list(map(int, input().split()))
num.sort(reverse=True)
A = num[0]
B = num[1]

# 유클리드 호제법 사용
while B != 0:
  A = A % B
  A, B = B, A

print(num[0]*num[1]//A)