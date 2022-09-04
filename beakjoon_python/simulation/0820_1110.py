# 0820_1110.py

# 0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다.
# 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다.
# 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 다음 예를 보자.

# N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.

n = int(input())
nums = list(str(n))
result = 0
print(nums)

if n<10:
    newN = 0+int(nums[0])

while True:
    m = int(nums[0])+int(nums[1])
    result += 1
    nums = list(str(m))
    if m == n:
        break

print(result)