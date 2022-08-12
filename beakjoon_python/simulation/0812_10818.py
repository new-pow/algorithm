# 0812_10818.py

# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
# 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.
# 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.

N = int(input())
if N<0 or N>1000000:
    exit()
else:
    num_arr = list(map(int, input().split()))
    print(min(num_arr), max(num_arr))

# 매우 쉽게 해결
# 입력 수 조건 처리 방법을 좀 더 알아보자!