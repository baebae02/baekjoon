import sys


def home(k,n):
    if a[k][n] > 0: 
        return a[k][n]
    sum = 0
    if(k == 0):
        return n
    else:
        for i in range(1,n+1):
            sum += home(k-1,i)
    return sum


a=[[0]*14 for i in range(14)]

N = int(sys.stdin.readline())

for i in range(N):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(home(k,n))