n = int(input())
arr = list(map(int, input().split()))
min = arr[0]
max = arr[0]

for num in arr :
    if num < min :
        min = num
    if num > max :
        max = num

print("%d %d" %(min, max))

