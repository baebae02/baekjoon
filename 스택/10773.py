n = int(input())
stack = list()
for i in range(n):
    num = int(input())
    if num > 0:
        stack.append(num)
    elif num == 0:
        stack.pop(-1)
print(sum(stack))