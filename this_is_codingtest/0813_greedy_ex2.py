# 각 자리가 숫자(0~9)로만 이루어진 문자열 S가 주어졌을 때,
# 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며
# 숫자 사이에 X또는 +연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램
# 무조건 모든 연산은 왼쪽부터 순서대로!

arr = list(map(int,list(input())))
result = 0
for i in range(len(arr)-1):
    if (arr[i]>1 and arr[i+1]>1):
        arr[i+1] = arr[i]*arr[i+1]
        result = arr[i+1]
    else:
        arr[i+1] = arr[i]+arr[i+1]
        result = arr[i+1]
print(result)