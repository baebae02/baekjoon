test = list(map(int, input().split()))
while max(test) != 0:
    test.sort()
    if test[0]*test[0] + test[1]*test[1] == test[2]*test[2]:
        print("right")
    else:
        print("wrong")
    test = list(map(int, input().split()))
