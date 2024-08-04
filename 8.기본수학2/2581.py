#2581
def find_num(n):
    if n < 2:
        return False
    i = 2
    while i <= n // 2:
        if n % i == 0:
            return False
        i = i + 1
    return True


minimum = int(input())
maximum = int(input())

li = list()
for i in range(minimum, maximum + 1):
    if find_num(i):
        li.append(i)
if len(li) != 0:
    print(sum(li))
    print(min(li))
else:
    print(-1)
