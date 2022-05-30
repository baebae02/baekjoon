#2798블랙잭
n, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
result = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if arr[i] + arr[j] + arr[k] > M:
                continue
            else:
                if arr[i]+arr[j]+arr[k] > result:
                    result = arr[i]+arr[j]+arr[k]
                break
print(result)
