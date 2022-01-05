N = int(input())
#list 순서 O 중복 O set 순서 X 중복 X
list = input()
sum = 0
for i in range(N):
    sum += int(list[i])
print(sum)
