N = int(input())
arr = list(map(int, input().split()))
arr2 = list(sorted(set(arr)))

dic = {}
for i in range(len(arr2)):
    dic[arr2[i]] = i
for i in arr:
    print(dic[i],end=' ')
