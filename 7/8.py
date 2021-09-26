alp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
sentence = input()

for i in alp:
    sentence = sentence.replace(i, 'A')

print(len(sentence))