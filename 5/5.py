n = int(input())
li = list(map(int,input().split()))

def cal(n):
    return n / max * 100
    
max = 0
for i in li:
    if i > max:
        max = i

li = list(map(cal, li))
sum = 0.0
for i in li:
    sum = sum + i
print(sum / len(li))