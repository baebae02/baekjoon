#7568 덩치
n = int(input())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append([a,b])

ans = [0] * len(arr)
for i in range(len(arr)):
    j = 0
    cnt = 1
    for j in range(len(arr)):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            cnt = cnt + 1
    ans[i] = cnt
print(*ans)
