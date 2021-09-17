a, b = input().split() # 두 가지 input을 동시에 받음. 그리고 공백을 기준으로 쪼갬 
a = int(a) #split한 건 문자열이기 때문에 정수로 바꿔줘야 함
b = int(b)
print ( a+b )
print ( a-b )
print ( a*b )
print ( a//b ) # /은 나누기 //은 몫
print ( a%b )