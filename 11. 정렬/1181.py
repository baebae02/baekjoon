N = int(input())
li = set()
for i in range(N):
    word = input()
    li.add(word)
li = list(li)
li.sort()
li.sort(key=len)
for i in li:
    print(i)
