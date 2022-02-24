#11653
n = int(input())
if n != 1:
    i = 2
    while i <= n // 2:
        if n % i == 0:
            print(i)
            n = n / i
            i = 1
        i = i + 1
    print(int(n))