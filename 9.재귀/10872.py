def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
n = int(input())
print(factorial(n))
