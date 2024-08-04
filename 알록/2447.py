def generate_pattern(n):
    if n == 1:
        return ['*']
    
    # 재귀적으로 작은 패턴 생성
    smaller = generate_pattern(n // 3)
    
    # 새로운 패턴 생성
    pattern = []
    for i in range(3):
        for line in smaller:
            if i == 1:
                pattern.append(line + ' ' * (n // 3) + line)
            else:
                pattern.append(line * 3)
    
    return pattern

def print_pattern(n):
    pattern = generate_pattern(n)
    for line in pattern:
        print(line)

# 사용 예
n = int(input())
print_pattern(n)