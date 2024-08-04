import sys
input = sys.stdin.readline
s = list(input().strip())
di = {}
for i in s:
  if i in di:
    di[i] += 1
  else:
    di[i] = 1

# print(di)
mid = ''
result = ''
cnt = 0
for key, value in di.items():
  if value % 2 == 1:
    cnt += 1
    mid = key
  if cnt >= 2:
    print("I'm Sorry Hansoo")
    exit()

for key, value in sorted(di.items()):
  result += key * (value//2)

print(result + mid + result[::-1])


