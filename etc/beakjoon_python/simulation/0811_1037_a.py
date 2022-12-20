N = int(input())
if (N>50 or N<0):
    exit

arr = set(map(int, input().split()))

A = min(arr)*max(arr)

print(A)