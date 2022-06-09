n, m = map(int,input().split())
li = []
check = []
for _ in range(n):
    li.append(input())
for _ in range(m):
    check.append(input())

li.sort()
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end + 1) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

cnt = 0
for i in range(m):
    if binary_search(li, check[i], 0, n-1) != None:
       cnt += 1
print(cnt)
