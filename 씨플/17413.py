S = input()

sts = []
tag = []
wd = []
hash_flag = False
for i in S:
  if i == '<':
    hash_flag = True
    tag.append(i)
    sts.append(''.join(wd))
    wd = []
  elif i == '>':
    hash_flag = False
    tag.append(i)
    sts.append(''.join(tag))
    tag = []
  elif i == ' ' and not hash_flag:
    sts.append(''.join(wd))
    wd = []
  elif hash_flag:
    tag.append(i)
  else:
    wd.append(i)
if len(wd) > 0:
  sts.append(''.join(wd))


for i in range(len(sts)):
  if sts[i].startswith('<'):
    print(sts[i], end='')
  else:
    print(sts[i][::-1], end='')
    if i < len(sts) - 1:
      if not sts[i+1].startswith('<'):
          print(' ', end='')
