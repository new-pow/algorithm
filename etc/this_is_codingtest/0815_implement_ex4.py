# 0815_implement_ex4.py

x = [0, 'a','b','c','d','e','f','g','h']
y = [0,'1','2','3','4','5','6','7','8']

position = list(input())
onX = x.index(position[0])
onY = y.index(position[1])

# 갈수있는 경우의 수
move = []
move.append([2,1])
move.append([2,-1])
move.append([-2,1])
move.append([-2,-1])
move.append([1,2])
move.append([1,-2])
move.append([-1,2])
move.append([-1,-2])

count = 0

for i in range(len(move)):
    # 경우의 수 대입
    moveX = onX + move[i][0]
    moveY = onY + move[i][1]
    if moveX > 0 and moveX < 9 and moveY >0 and moveY <9:
        count +=1

print(count)

#########
## 답변 ##
#########
# # 현재 나이트 위치 입력받기
# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0]))-int(ord('a'))+1

# # 나이트 이동할 수 있는 방향 정의
# steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

# # 각 위치 이동이 가능한지 확인
# result = 0
# for step in steps:
#     next_row = row + step[0]
#     next_column = column + step[1]
#     # 해당 위치로 이동이 가능하다면 카운트 증가
#     if next_row >= 1 and next_row<=8 and next_column >=1 and next_column <=8:
#         result += 1

# print(result)