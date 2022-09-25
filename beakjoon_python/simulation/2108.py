# 2108.py
# 통계학 https://www.acmicpc.net/problem/2108 푸는 중

# 산술평균, 중앙값, 최빈값, 범위

# import sys
# input = sys.stdin.readlines

n = int(input())
arr = [0]*n

for i in range(n):
    arr[i] = int(input())

new_arr = arr.sort()
count = [0] * n
for i in range(n):
    if new_arr[i]==new_arr[i+1]:
        count[i] +=1

#산술평균
print(round(sum(arr)/n))
#중앙 값
arr.sort()
center = int((n-1)/2)
print(arr[center])
#최빈값


print(max(arr)-min(arr))