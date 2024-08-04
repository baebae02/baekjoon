from itertools import permutations
import sys
input = sys.stdin.readline

candies = permutations([1,2,3,4,5,6,7,8,9], 3)


def check(ans, strikes, balls):
  
  a, b, c = ans // 100, (ans % 100) // 10, ans % 10
  ans = []
  for i in candies:
    strike = strikes
    ball = balls
    if i[0] == a:
      strike -= 1
    if i[0] == b:
      ball -= 1
    if i[0] == c:
      ball -= 1
    if i[1] == b:
      strike -= 1
    if i[1] == a:
      ball -= 1
    if i[1] == c:
      ball -= 1
    if i[2] == a:
      ball -= 1
    if i[2] == b:
      ball -= 1
    if i[2] == c:
      strike -= 1
    
    if strike == 0 and ball == 0:
      ans.append(i)
  return ans
    

 



for _ in range(int(input())):
  ans, strike, ball = map(int, input().split())
  candies = check(ans, strike, ball)
  # print(candies)


# print(candies, "final")
print(len(candies))
