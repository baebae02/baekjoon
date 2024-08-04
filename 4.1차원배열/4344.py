def avg(li) :
    sum = 0
    for i in range(len(li)) :
        sum += int(li[i])
    avg = sum / (len(li))
    return avg

def rate(li) :
    count = 0
    li = list(map(int, li))
    for i in li :
        if i > avg(li) :
            count += 1
    return count / (len(li)) * 100 

C = int(input())
for i in range(C) :
    str = list(input().split())
    n = int(str[0])
    del str[0]
    r = rate(str)
    print(f'{r:.3f}%')
    
    
    

