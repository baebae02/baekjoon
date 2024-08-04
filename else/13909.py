N = int(input())
for i in range(N, 0, -1):
  if int(i**0.5) == i**0.5:
    print(int(i**0.5))
    break
  
# 규칙 찾는 게 중요했던 문제. 규칙 찾고 의심하지 말기 !