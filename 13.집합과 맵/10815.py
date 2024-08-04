n = int(input())
li = list(map(int, input().split()))
m = int(input())
compare = list(map(int, input().split()))

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

for i in range(m):
    if binary_search(li, compare[i], 0, n - 1) != None:
        print(1, end=' ')
    else:
        print(0, end= ' ')
