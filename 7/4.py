N = int(input())
li = ""
for i in range(N): # test 케이스만큼 반복
    n, str = input().split() # num, str 입력 받고
    for j in range(len(str)): # 문자열 길이만큼 반복
        li+=(str[j]*int(n))
        if j == len(str)-1:
            print(li)
            li=""

#정답
# t=int(input())
# for i in range(t):
#  a,b=input().split()
#  for j in b:
#   print(int(a)*j, end='')
#  print()