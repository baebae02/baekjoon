N = int(input())
cycle = 0
x = N

while True :
    n2 = x // 10
    n1 = x % 10
    new = (n2 + n1) % 10
    num = 10*n1 + new
    cycle+=1
    x = num
    if N == num :
        print(cycle)
        break