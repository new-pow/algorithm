# 아직 글을 모르는 영석이가 벽에 걸린 칠판에 자석이 붙어있는 글자들을 붙이는 장난감을 가지고 놀고 있다. 

# 이 장난감에 있는 글자들은 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’이다.
# 영석이는 칠판에 글자들을 수평으로 일렬로 붙여서 단어를 만든다.
# 다시 그 아래쪽에 글자들을 붙여서 또 다른 단어를 만든다.
# 이런 식으로 다섯 개의 단어를 만든다. 아래 그림 1은 영석이가 칠판에 붙여 만든 단어들의 예이다.

# 한 줄의 단어는 글자들을 빈칸 없이 연속으로 나열해서 최대 15개의 글자들로 이루어진다. 또한 만들어진 다섯 개의 단어들의 글자 개수는 서로 다를 수 있다. 
# 심심해진 영석이는 칠판에 만들어진 다섯 개의 단어를 세로로 읽으려 한다. 세로로 읽을 때, 각 단어의 첫 번째 글자들을 위에서 아래로 세로로 읽는다.
# 다음에 두 번째 글자들을 세로로 읽는다. 이런 식으로 왼쪽에서 오른쪽으로 한 자리씩 이동 하면서 동일한 자리의 글자들을 세로로 읽어 나간다.
# 위의 그림 1의 다섯 번째 자리를 보면 두 번째 줄의 다섯 번째 자리의 글자는 없다.
# 이런 경우처럼 세로로 읽을 때 해당 자리의 글자가 없으면, 읽지 않고 그 다음 글자를 계속 읽는다. 그림 1의 다섯 번째 자리를 세로로 읽으면 D1gk로 읽는다. 

# 칠판에 붙여진 단어들이 주어질 때, 영석이가 세로로 읽은 순서대로 글자들을 출력하는 프로그램을 작성하시오.

# -----

# # 1줄씩 변수로 정의 + 문자열타입으로 바꿔주기
# str1 = input()
# str2 = input()
# str3 = input()
# str4 = input()
# str5 = input()

# # list에 입력
# array1 = list(str1)
# array2 = list(str2)
# array3 = list(str3)
# array4 = list(str4)
# array5 = list(str5)
# array = [len(array1), len(array2), len(array3), len(array4), len(array5)]
# maxlength = max(array)

# # 인덱스 0부터 출력 + 공백일경우 패스
# for num in range(maxlength):
#     print(array1[num]+array2[num]+array3[num]+array4[num]+array5[num], end='')

# ---- 풀이2

# 한줄에 최대 15개인 2차원 배열 선언
arr = [[0] * 15 for _ in range(5)]
print(arr)

# 5줄 반복하여 배열 반복
for i in range(5):
    line = list(input())
    for j in range(len(line)):
        arr[i][j] = line[j]
print(arr)

# 출력
for i in range(15):
    for j in range(5):
        if arr[j][i] == 0:
            continue
        else: print(arr[j][i], end="")