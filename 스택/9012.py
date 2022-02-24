n = int(input())
for i in range(n):
    b = input()
    stack = list(b)
    sum = 0
    for item in stack:
        if item == '(':
            sum = sum + 1
        elif item == ')':
            sum = sum - 1
        if sum < 0:
            print('NO')
            break
    if sum == 0:
        print('YES')
    else:
        print('NO')