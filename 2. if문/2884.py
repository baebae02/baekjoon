h,m= map(int,input().split())
x = h * 60 + m - 45
h = x // 60
m = x % 60
if h < 0 :
    h += 24
print (h,m)

# map 사용을 조금씩 해보자 ,,,,