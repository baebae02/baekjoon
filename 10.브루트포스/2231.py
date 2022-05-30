#2231 분해합
stdin = input()
n = int(stdin)
length = len(stdin)
arr = []

def checkSum(n):
    if n < 0:
        return 0
    arr = list(str(n))
    arr = map(int, arr)
    return (sum(arr))

result = 0

for i in range(n - 9*length, n):
    if i + checkSum(i) == n:
        result = i
        break

print(result)
