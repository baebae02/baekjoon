N = int(input())
li = list(map(int, input().split()))
for i in range(1, N):
  li[i] = max(li[i], li[i]+li[i-1])

# print(li)
print(max(li))