N = int(input())

count = 0
for i in range(N):
    a = input()
    for i in range(len(a)):
        if(len(a) == 1):
            count+=1
            break

        index = a[0]
        a = a[1:]
        if a.find(index) == -1:
            continue
        elif a.find(index) == 0:
            continue
        elif a.find(index) > 0:
            break
        
print(count)