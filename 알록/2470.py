N = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

start = 0
end = N - 1
result = [2000000000, start, end]

while start < end:
  sub_sum = liquid[start] + liquid[end]
  abs_sum = abs(sub_sum)
  print(start, end, sub_sum, abs_sum)
  if abs_sum < abs(result[0]):
    result = [sub_sum, start, end]
  if sub_sum == 0:
    result = [sub_sum, start, end]
    break
  if sub_sum < 0:
    start += 1
  elif sub_sum > 0:
    end -= 1

print(liquid[result[1]], liquid[result[2]])

# -100 -1 0 100

# -100 -1 100 > -1   
# -1 0 100
