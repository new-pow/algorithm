import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * (n)
for i in range(n):
    temp = int(input())
    arr[i] = temp
arr.sort()

for i in range(len(arr)):
    print(arr[i])