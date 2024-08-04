N = int(input())
count = 0

for i in range(N):
    a = input()
    for i in range(len(a)):
        if(len(a) == 1):
            count += 1
            break
        x = a[0]
        a=a[1:]
        if( a.find(x) < 1 ): #-1이면 없는 거 0이면 연속인 거
            continue

        elif(a.find(x) > 0):
            break
print(count)
        


