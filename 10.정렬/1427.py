li = list(input())
li = list(map(int,li))
li.sort(reverse=True)

for i in li:
    print(i, end='')
