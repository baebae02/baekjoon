a, b, c, d, e, f = map(int, input().split())
# x = (c*e-b*f) / (a*e - b*d)
# y = (c*d - a*f) / (b*d - a*e)
# print(int(x), int(y))

for i in range(-999, 1000):
  for j in range(-999, 1000):
    if a*i + b*j == c and d*i + e*j == f:
      print(i, j)
      break