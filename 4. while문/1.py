#백준 10951번 실패 
while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break

# 예외처리
#try:
#     ...
# except [발생 오류[as 오류 메시지 변수]]:
#     ...
