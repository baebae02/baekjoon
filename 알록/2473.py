N = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

result = [3000000000, 0, 0, 0]

for i in range(N-2):
  start = i + 1
  end = N - 1
  while start < end:
    sub_sum = liquid[i] + liquid[start] + liquid[end]
    if abs(sub_sum) < result[0]:
      result = [abs(sub_sum), i, start, end]
    if sub_sum < 0:
      start += 1
    elif sub_sum > 0:
      end -= 1
    else:
      break

print(liquid[result[1]], liquid[result[2]], liquid[result[3]])

# -100 -1 0 100 -1
# -100 
# -100 -1 0 100
#start mid end = 양수, 
# start mid는 음음 음양 양양
# 음수 음수 -> mid