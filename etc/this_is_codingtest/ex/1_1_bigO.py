# N개의 데이터 합을 계산하는 프로그램 예제

from ipaddress import summarize_address_range
print('#01')

array = [3,5,1,2,4] # 5개의 데이터 (N=5)
summary = 0 # 합계를 저장할 변수

# 모든 데이터를 하나씩 확인하며 합계 계산
for item in array:
    summary += item

# 결과를 출력
print(summary)

# 수행 데이터의 개수 N에 비례한다. 시간복잡도 : O(N)

print('#02')

# 2중 반복문을 이용하는 프로그램 예제
array = [3,5,1,2,4] # 5개의 데이터(N=5)
temp = 0

# 각 변수의 곱
for item in array:
    for item2 in array:
        temp = item * item2
        print(temp)

# 시간복잡도 O(N^2)