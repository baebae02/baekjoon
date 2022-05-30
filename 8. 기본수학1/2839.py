#2839. 설탕배달
n = int(input())
def findMin(n):
    div = n // 5
    remain = n % 5
    if remain == 0:
        return div
    for i in range(div, -1, -1):
        if (n - 5*i) % 3 == 0:
            return i + (n-5*i) // 3
    return -1

print(findMin(n))
