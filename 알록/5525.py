def find_ioi_patterns(S, N, M):
    answer = 0
    count = 0
    i = 0
    
    while i < (M - 1):
        if S[i:i+3] == 'IOI':
            i += 2
            count += 1
            if count == N:
                answer += 1
                count -= 1
        else:
            i += 1
            count = 0
    
    return answer
 
# 입력 받기
N = int(input())  # 문자열 S의 길이
M = int(input())  # 찾고자 하는 연속된 IOI의 개수
S = input()       # 문자열 S

# 결과 출력
result = find_ioi_patterns(S, N, M)
print(result)