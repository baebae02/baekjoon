a = int(input())
b = int(input())
c = int(input())

cal = a*b*c
li = list(cal)
for i in range (0,10):
    print(li.count('%d' %(i)))
