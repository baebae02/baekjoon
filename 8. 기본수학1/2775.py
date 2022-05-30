n = int(input())
def recursion(k, n):
    sum = 0
    if k == 0:
        return n
    if k == 1:
        return int(n * (n+1) / 2)
    else:
        for i in range(1, n+1):
            sum = sum + recursion(k-1, i)
        return sum
for i in range(n):
    k = int(input())
    n = int(input())
    print(recursion(k,n))
