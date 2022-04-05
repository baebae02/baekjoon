n = int(input())
stack = []
ans = []
flag = True
k = 1
for i in range(n):
    num = int(input())
    while k <= num:
        stack.append(k)
        ans.append("+")
        k=k+1
    if stack[-1] == num:
        stack.pop()
        ans.append("-")
    else:
        flag = False
        print("NO")
        break
        
if flag==True:
    for i in ans:
        print(i)
