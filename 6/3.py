
N = int(input())
count = 0
for i in range(N+1): # 0부터 n까지가 range 0일 경우에는 카운트를 안함. 
    if i == 0:
        continue
    elif i < 100 :
        count += 1 # 한자리 수, 두자리 수는 모두 한수니까 ! 
    elif i < 1000 :
        stri = str(i)
        n1 = int(stri[0]) #일의 자리
        n2 = int(stri[1]) #십의 자리
        n3 = int(stri[2]) #백의 자리 
        if ((n2 - n1) == (n3 - n2)):
            count+=1 #등차수열일 경우엔 count++
print(count)
