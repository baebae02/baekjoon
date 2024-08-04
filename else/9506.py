def findprime(num):
  ans = [1]
  for i in range(2, num):
    if num % i == 0:
      ans.append(i)
  return ans

n = int(input())
while n != -1:
  v = findprime(n)
  if n == sum(v):
    v = map(str, v)
    print(n, " = "," + ".join(v), sep="")
  else:
    print(n,"is NOT perfect.")
  n = int(input())