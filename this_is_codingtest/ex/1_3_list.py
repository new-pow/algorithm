# 1_3_list.py

# 직접 데이터 넣어 초기화
from re import I


a = [1,2,3,4,5,6,7,8,9]
print(a)

# 네번째 원소만 출력
print(a[3])

# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0]*n
print(a)

a[4] = 4
print(a)

a = [1,2,3,4,5,6,7,8,9]
print(a[2])
print(a[-1])

print(a[3])
print(a[1:4])
print(a[2:-2])

# 0부터 9까지 수를 포함하는 리스트
# 반복문부터 넣는 것을 추천한다.
array = [i for i in range(10)]
print(array)

# 0부터 19까지 수 중 홀수만 포함
array = [i for i in range(20) if i%2==1]
print(array)

# 1부터 9까지의 수들의 제곱 값을 포함하는 리스트
array = [i*i for i in range(10)]
print(array)

# N * M 크기의 2차원 리스트 초기화
n = 4
m = 3
array = [[0]*n for _ in range(n)]
print(array)

# 언더바 사용법
