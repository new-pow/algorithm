# 0912_10773.py
# 제로 https://www.acmicpc.net/problem/10773 풀이완료!

k = int(input())
q = list()
for _ in range(k):
    num = int(input())
    if num!=0:
        q.append(num)
    if num==0:
        q.pop()

result = 0 # 결과값

while q:
    result += q.pop()

print(result)