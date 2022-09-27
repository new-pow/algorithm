# 1859.py
# 백만장자 프로젝트 https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1&&&&&&&&&&
# 푸는 중

# N일동안 물건 매매가 예측
# 1일에 1개 구입가능
# 판매량은 상관 없음

# 테스트 케이스 수 T
from collections import deque


t = int(input())

for tc in range(1,t+1):
    # 자연수 2<=N<=1000000
    n = int(input())

    # 매매가 N개, (10,000원 이하)
    arr = deque(map(int, input().split()))

    last = arr[-1]

    result = 0

    # while n_arr:
    #     if n_arr[0]<max(n_arr):
    #         result += max(n_arr)-n_arr[0]
    #         n_arr.popleft()
    #     elif n_arr[0]>=max(n_arr):
    #         n_arr.popleft()

    for i in range(len(arr)-1,-1,-1): # 핵심! 뒤부터 보기
        if last > arr[i]:
            result += last-arr[i]
        else: # 같거나 작을 때 
            last = arr[i]

    # 결과출력
    print('#{} {}'.format(tc,result))