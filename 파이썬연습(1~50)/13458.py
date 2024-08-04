N = int(input())
import math
A = list(map(int, input().split()))
B, C = map(int, input().split())
sum =0 
for a in A:
  sum += 1
  if a - B >= 1:
    print(a, B, sum)
    sum += math.ceil((a - B) / C)

print(sum)



