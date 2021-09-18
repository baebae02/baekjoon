li = []
for i in range(0,9):
    n = int(input())
    li.append(n)

max = li[0]
count = 0
for i in range(len(li)):
    if li[i] > max:
        max = li[i]
        count = i

print(max)
print(count+1)
