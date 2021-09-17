a=input()
b=input()
a=int(a)
b=str(b)
b1=int(b[2])
b2=int(b[1])
b3=int(b[0])
b=int(b)
print(a*b1)
print(a*b2)
print(a*b3)
print(a*b)

# short code
# a,b=map(int,open(0))
# print(b%10*a,b%100//10*a,b//100*a,b*a)

# map 
# map(function, iterable) 처럼 생김. (함수, 반복 가능한 자료형)
# 두 번째 인자로 들어온 반복 가능한 자료형 (리스트나 튜플)을 첫 번째 인자로 들어온 함수에 하나씩 집어넣어서 함수를 수행
# 예제
# >>> a = [1.2, 2.5, 3.7, 4.6]
# >>> for i in range(len(a)):
# ...     a[i] = int(a[i])
# ...
# >>> a
# [1, 2, 3, 4]
# 이때 for 문 대신 a = list(map(int, a)) 를 사용할 수 있음. list에 있는 값들을 int로 바꿔달라는 뜻. 