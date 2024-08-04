N = int(input())
now = 0
count = 0
time = []
for i in range(N):
  start, end = map(int, input().split())
  time.append([start, end])

# print(time)
time.sort(key=lambda x : (x[1], x[0]))
for new_start, new_end in time:
  if new_start >= now:
    count += 1
    now = new_end

print(count)

# for k in range(N):
#   # print(k, now, count)
#   if now in time:
#     # print("Here", now)
#     r = time[now]
#     past_now = now
#     now = r
#     count += 1
#     for j in range(past_now, r):
#       # print("HEE", now, j)
#       if j in time and now in time and time[j] <= time[now]:
#         now = time[j]
#   else:
#     now += 1

# print(count)

# 좀 덜 욕심쟁이였던 방법 ....
# 그리디는 그냥 큰 숫자 먼저 !!! 즉 정렬을 많이 사용함.
    
