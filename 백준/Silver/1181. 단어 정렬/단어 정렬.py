# 1181
# 단어 정렬 https://www.acmicpc.net/problem/1181

n = int(input())
arr = set()
for i in range(n):
    arr.add(input())

arr = list(arr)
arr.sort()
arr.sort(key= lambda x:len(x))

for i in arr:   
    print(i)