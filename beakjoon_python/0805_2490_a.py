# 0805_2490_a.py

# 우리나라 고유의 윷놀이는 네 개의 윷짝을 던져서 배(0)와 등(1)이 나오는 숫자를 세어 도, 개, 걸, 윷, 모를 결정한다.
# 네 개 윷짝을 던져서 나온 각 윷짝의 배 혹은 등 정보가 주어질 때
# 도(배 한 개, 등 세 개), 개(배 두 개, 등 두 개), 걸(배 세 개, 등 한 개), 윷(배 네 개), 모(등 네 개) 중 어떤 것인지를 결정하는 프로그램을 작성하라.

# 2차원 배열 생성
playarr = [[0]*4 for _ in range(3)]
sumarr = [0, 0, 0]

# 공백 제거하여 배열에 저장
for i in range(3):
    play = list(input().replace(" ",""))
    for j in range(4):
        playarr[i][j] = int(play[j])
        sumarr[i] += playarr[i][j]

# 출력
for i in range(3):
    result = sumarr[i]
    if result==0:
        print("E")
    elif result==4:
        print("D")
    elif result==3:
        print("C")
    elif result==2:
        print("B")
    else:
        print("A")
