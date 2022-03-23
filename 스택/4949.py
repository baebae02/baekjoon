def strcheck(str):
    li = []
    for i in str:
        if i == "(" or i=="[":
            li.append(i)
        elif i == ")" :
            if len(li)!=0 and li[-1] == "(":
                li.pop()
            else:
                return "no"
        elif i == "]" :
            if len(li)!=0 and li[-1] == "[":
                li.pop()
            else:
                return "no"
    if len(li) == 0:
        return "yes"
    else:
        return "no"
    # str = sys.stdin.readline()
while True:
    str = input()
    li = []
    if str == ".":
        break
    print(strcheck(str))
