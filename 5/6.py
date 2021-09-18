n = int(input())
for i in range(n) : 
    li = list(input())
    sum = 0
    c = 0
    for item in li :
        if item == 'O' :
            c += 1
            sum += c
        else :
            c = 0
    print(sum)

    
# 몰라서 블로그 참고함 
# c += 1 하고 sum += c 해서 틀렸었음
# c를 기본값을 1로 하고 sum 계산 후에 c를 증가해줌
# 연속으로 O인지 상관없이 그냥 O인지 확인을 하나씩 해줌. 