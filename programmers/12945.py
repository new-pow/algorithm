# 12945.py
def solution(n):
    answer = 0
    d=[0]*(n+1)
    d[1]=1
    for i in range(2,n+1):
        d[i]=d[i-1]+d[i-2]
    return d[n]%1234567