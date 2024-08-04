alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sen = input()
def calNum(sentence):
    sum = 0
    for i in range(len(sentence)):
        index = alp.index(sentence[i])
        if index > 21 : #WXYZ
            sum += 10
        elif index > 18 : #TUV
            sum += 9
        elif index > 14 : #PQRS
            sum += 8
        elif index > 11 : #MNO
            sum += 7
        elif index > 8 : #JKL
            sum += 6
        elif index > 5: #GHI
            sum += 5
        elif index > 2: #DEF
            sum += 4
        else : #ABC
            sum += 3 
    return sum
print(calNum(sen))