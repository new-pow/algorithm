# 12980.py
# 점프와 순간 이동 https://school.programmers.co.kr/learn/courses/30/lessons/12980
# 1회차 풀이 : 에러...
import sys
from collections import deque

sys.setrecursionlimit(10**6)

def dfs(x,n):
    for i in range(1):
        if i == 0:
            nx = 2*x
            if nx == n:
                if temp<used:
                    used = temp + 1
                break
            elif nx > n:
                break
            else:
                dfs(nx,n) 
        elif i != 0:
            nx = x + 1
            temp += 1
            if nx == n:
                if temp<used:
                    used = temp + 1
                break
            elif nx > n:
                break
            else:
                dfs(nx,n)




def solution(n):
    ans = 0
    used = 10
    temp = 0
    x = 0 # 처음 출발지점
    move = []

    for x in range(10):
        dfs(x,n)

    return used

n = 5
print(solution(n))