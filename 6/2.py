def self_num():
    li = set()
    st = set(range(1,10001))
    next_num = 1
    for i in range(1,10001):
        num=str(i)
        if i < 10:
            next_num = i + i
        elif i < 100:
            next_num = int(num[0]) + int(num[1]) + i
        elif i < 1000:
            next_num = int(num[0]) + int(num[1]) + int(num[2]) + i
        else:
            next_num = int(num[0]) + int(num[1]) + int(num[2]) + int(num[3]) + i
        # print(i, "i")
        # print(next_num, "next_num")
        li.add(next_num)

    x = sorted(list(st-li))
    for i in x:
        print (i)

self_num()

