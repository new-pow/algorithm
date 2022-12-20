# 1204.py
# 최빈수 구하기 https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV13zo1KAAACFAYh&categoryId=AV13zo1KAAACFAYh&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=ALL&select-1=2&pageSize=10&pageIndex=1&&&&&&&&&&

t = int(input())

for _ in range(t):
    tc = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    scores = [0]*100
    temp = 0
    for i in range(0,101):
        nums.count(i)
        # if i == len(nums)-1:
            
        # elif nums[i]==nums[i+1]:
        #     temp += 1
        # elif nums[i] != nums[i+1]:
        #     scores[nums[i]] = temp