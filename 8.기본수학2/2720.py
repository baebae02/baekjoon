T = int(input())
for _ in range(T):
  charge = int(input())
  ans = [0,0,0,0]
  ans[0] = charge // 25
  charge = charge % 25
  ans[1] = charge // 10
  charge = charge % 10
  ans[2] = charge // 5
  charge = charge % 5
  ans[3] = charge
  print(*ans)