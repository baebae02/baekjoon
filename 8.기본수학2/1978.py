#1978
def find_num(n):
    if n < 2:
        return False
    i = 2
    while i <= n // 2:
        if n % i == 0:
            return False
        i = i + 1
    return True


num = int(input())
numbers = map(int, input().split())
cnt = 0
for item in numbers:
    if find_num(item):
        cnt = cnt + 1

print(cnt)