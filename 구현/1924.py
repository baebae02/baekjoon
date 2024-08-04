x, y = map(int, input().split())
day_sum = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365 ]
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
# print(day_sum[x], y)
i = (day_sum[x] + y) % 7 
print(day[i])