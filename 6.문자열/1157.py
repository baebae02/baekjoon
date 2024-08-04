word = input().lower()
alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
count = []
for i in alp:
    count.append(word.count(i))

max_count = count.count(max(count))
count_index = count.index(max(count))
if max_count != 1 :
    print("?")
else : 
    print(alp[count_index].upper())