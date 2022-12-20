# 0911_7568.py
# 덩치 https://www.acmicpc.net/problem/7568 풀이 완료


person = []

n = int(input()) # 인원 수
result = [1]*n # 결과 집합

for _ in range(n):
    x, y = map(int, input().split())
    person.append([x,y])

for i in range(n):
    for j in range(n):
        if (person[i][0] < person[j][0] and person[i][1] < person[j][1]):
            result[i] += 1
    print(result[i], end=" ")