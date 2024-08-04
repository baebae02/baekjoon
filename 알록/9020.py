T = int(input())

# 조건 1. 항상 짝수만 입력
# 조건 2. 두 소수의 차이가 가장 작은 것을 출력
# 결론 -> 반을 가른 뒤, 하나씩 추가하고 빼면서 소수인지 확인

def is_prime(n):
  if n == 1:
    return False
    
  for i in range(2, int(n**0.5)+1):
    if n % i == 0:
      return False
  return True

for _ in range(T):
  n = int(input())
  a, b = n//2, n//2
  while a > 0:
    if is_prime(a) and is_prime(b):
      print(a, b)
      break
    else:
      a -= 1
      b += 1
  