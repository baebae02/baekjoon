#분수찾기
#cnt = 집합 번호 (대각선)
#s = 분자 p = 분모 

n=int(input())
i=n
cnt = 0
while(i > 0):
    cnt = cnt + 1
    i = i-cnt


def sum(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    return sum


if (cnt%2 == 0):
    s = n - sum(cnt-1)
else:
    s =(cnt+1) - n + sum(cnt-1)
print (str(s)+"/"+str(cnt+1-s))