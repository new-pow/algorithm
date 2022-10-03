# 1979.py

import sys
input = sys.stdin.readline

t = int(input())

# 세로
def dfs_col(a, b):
    

def dfs_row(a, b):


for _ in range(t):
    n, k = map(int, input().split())
    puzzle = []
    result = 0
    for _ in range(n):
        temp = list(map(int, input().split()))
        puzzle.append(temp)
    
    # 가로 카운트
    for i in range(n):
        num = puzzle[i].count(1)
        if num == k:
            result += 1
    # 세로 카운트
    for i in range(n):
        num =0
        for j in range(n):
            num += puzzle[i][j]
        if num == k:
            print("num : ",num)
            result += 1
    
    print("result : ",result)