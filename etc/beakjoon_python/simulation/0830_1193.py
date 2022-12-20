# 0830_1193.py

# 이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
# X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.


x = int(input())
l = 1
i = 1
j = 1
for _ in range(1,x):
    if l==i and j==1:
        l += 1
        i = 1
        j = l
    elif l==j and j>i:
        i +=1
    elif l==i and i==j:
        i = l
        j = 1
    elif l==i and i>j:
        j +=1

if x==1:
    print("1/1")
else:
    print(i, end="/")
    print(j)