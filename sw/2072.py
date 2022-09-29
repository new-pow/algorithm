# 2072.py

t = int(input())
for tc in range(1, t+1):
    arr = list(map(int,input().split()))
    result = 0
    for i in range(len(arr)):
        if arr[i]%2 == 1:
            result += arr[i]

    print('#{} {}'.format(tc, result))