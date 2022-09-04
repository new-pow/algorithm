# 0817_10451.py

# 순열 그래프 (3, 2, 7, 8, 1, 4, 5, 6) 에는 총 3개의 사이클이 있다. 이러한 사이클을 "순열 사이클" 이라고 한다.
# N개의 정수로 이루어진 순열이 주어졌을 때, 순열 사이클의 개수를 구하는 프로그램을 작성하시오.

# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 순열의 크기 N (2 ≤ N ≤ 1,000)이 주어진다. 둘째 줄에는 순열이 주어지며, 각 정수는 공백으로 구분되어 있다.
# 각 테스트 케이스마다, 입력으로 주어진 순열에 존재하는 순열 사이클의 개수를 출력한다.

# t = int(input()) # 테스트 케이스 개수

# def dfs(x):
#     check[x] = True
#     index = arr[x]
#     if not check[index]:
#         dfs(index)

# for _ in range(t):
#     n = int(input()) # 케이스의 순열 크기
#     arr = [0] + list(map(int, input().split()))
#     check = [True] + [False]*n
#     count = 0;

#     for i in range(1,n+1):
#         if not check[i]:
#             dfs(i)
#             count += 1
#     print(count)

# ### 다시풀이

import sys
sys.setrecursionlimit(2000)


def dfs(x):
    check[x] = True
    index = arr[x]
    if not check[index]:
        dfs(index)

t = int(input()) # 테스트 케이스 개수
count = 0

for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    check = [True]+([False]*n)
    count = 0

    for i in range(n+1):
        if not check[i]:
            dfs(i) # 순열 1사이클
            count += 1
    print(count)