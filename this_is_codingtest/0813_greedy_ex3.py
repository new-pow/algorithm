# 모험가 N명에게 '공포도' 측정하였다.
# 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 한다.
# 몇개의 그룹을 만들 수 있을지 궁금. 여행을 떠날 수 있는 그룹 수의 최대값

n = int(input())
data = list(map(int, input().split()))
data.sort()
result=0
size = data[0]

for _ in range(n):
    if (size>n): break
    if (size<n):
        n -= size
        size = data[data[size]]
        result +=1
print(result)

# 답안 예시
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹 수
count = 0 # 현재 그룹에 포함된 모험가 수

for i in data:
    count+=1 # 현재 그룹에 해당 모험가 포함
    if count >= i: # 현재 그룹에 포함된 모험가 수가 현재의 공포도 이상이라면, 그룹결성
        result +=1
        count=0

print(result)