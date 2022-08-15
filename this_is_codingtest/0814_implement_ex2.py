# 첫째줄 공간의 크기를 나타내는 N (1<=N<=100)
# 둘째 줄에 A가 이동할 계획서 내용 (1<=이동횟수<=100)
# 첫째줄에 여행가 A가 최종적으로 도착할 지점의 좌표(X,Y)를 공백을 기준으로 구분하여 출력

N = int(input())
plans = list(input().split())

# 시작지점 설정
position = [1,1]

# R L D U
moveX = [1, -1, 0, 0]
moveY = [0, 0, 1, -1]

for plan in plans:
    index=0
    if (plan=="R"): index=0
    if (plan=="L"): index=1
    if (plan=="D"): index=2
    if (plan=="U"): index=3

    position[0] += moveX[index]
    position[1] += moveY[index]
    
    if (position[0]<1): position[0]=1
    if (position[0]>N): position[0]=N
    if (position[1]<1): position[1]=1
    if (position[1]>N): position[1]=N

print(position[0],position[1])

# 해답

N = int(input())
plans = input().split()
x, y = 1, 1

moveX = [1, -1, 0, 0]
moveY = [0, 0, 1, -1]
move_types = ['R','L','D','U']

# 이동계획 하나씩 확인
for plan in plans:
    # 이동후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + moveX[i]
            ny = y + moveY[i]
    # 공간 벗어나면 무시
    if nx<1 or ny<1 or nx>N or ny>N:
        continue
    # 이동수행
    x, y = nx,ny

print(x,y)