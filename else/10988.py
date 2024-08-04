def check_pelindrom(str):
  str = list(str)
  return 1 if str == list(reversed(str)) else 0

s = input()
print(check_pelindrom(s))