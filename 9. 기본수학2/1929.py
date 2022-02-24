#1929
def find_num(n):
    if n < 2:
        return False
    i = 2
    while i <= n ** 0.5:
        if n % i == 0:
            return False
        i = i + 1
    return True


M, N = map(int, input().split())
for i in range(M, N+1):
    if find_num(i):
        print(i)