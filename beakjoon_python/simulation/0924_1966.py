# 0924_1966.py
# 프린터 큐 https://www.acmicpc.net/problem/1966 푸는 중

from collections import deque
import sys
input = sys.stdin.readline

doc = int(input())

for _ in range(doc):
    # n = 문서의 수, m = 중요도 체크할 문서
    n, m = map(int, input().split())
    doc_arr = deque(map(int,input().split()))
    imp_arr = doc_arr
    result = 0
    
    while True:
        best = min(imp_arr)
        result += 1
        temp = imp_arr.popleft()
        if temp == best:
            

    print(result)