# 0815_implement_ex3.py

# 정수 n이 입력되면 00시 00분 00초부터 n시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램

N=int(input())
count = 0

for h in range(N+1):
    if(h==3 or h==13 or h==23):
        count += 60*60
    else:
        count += ((15*60) + (45*15))

print(count)

# 풀이2

# N=int(input())
# result = 0

# #1시간 중 3이 들어가는 경우의 수
# h = [[0]*60 for _ in range(60)]

# for i in range(60):
#     for j in range(60):
#         if i%10 == 3:
#             h[i][j] = 1
#         if i//10 == 3:
#             h[i][j] = 1
#         if j%10 == 3:
#             h[i][j] = 1
#         if j//10 == 3:
#             h[i][j] = 1

# h_result = 0

# for i in range(60):
#     h_result += sum(h[i])

# for i in range(N+1):
#     if i%10 == 3:
#         result += 60*60
#     else:
#         result += h_result

# print(result)

# 해답

# h= int(input())
# count = 0
# for i in range(h+1):
#     for j in range(60):
#         for k in range(60):
#             # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
#             if '3' in str(i)+str(j)+str(k):
#                 count += 1

# print(count)

# 풀이시 주의사항
# 문제 범위에 주의할 것! h+1 시까지 계산한다는 것을 이해해야 한다.
# 완전탐색에 무서워하지 말자. 모든 경우의 수가 2000만 이하라면 가능!