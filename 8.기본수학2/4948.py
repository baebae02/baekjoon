#4948.베르트랑 공준
import sys
def isDecimal(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True
    
n = int(sys.stdin.readline())

while n != 0:
    sum = 0
    for i in range(n+1, 2*n + 1, 1):
        if isDecimal(i):
            sum = sum + 1
    print(sum)
    n = int(sys.stdin.readline())
