a, b = input().split()
a = a[::-1] #문자열 뒤집기
b = b[::-1]
if a > b :
    print(a)
else :
    print(b)

# 문자열 다루기
# # >>> s[4:10:1] #정방향 4~9까지
# >>> s[4:10:-1] #역방행 4~9까지인데 시작위치와 끝위치가 정방향
# >>> s[10:4:-1] # 10~5까지 역방향
# >>> s[::-1] #문자열 뒤집기
# >>> s[::2] #2칸 단위로