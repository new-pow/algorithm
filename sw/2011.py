# 2011.py

def catch():
    

t = int(input())
n, m = map(int, input().split())
if n>=5 and 15>=n and m>=2 or m<=n:
    graph = []

    for _ in range(t):
        for _ in range(n):
            temp = list(map(int, input().split()))
            graph.append(temp)
        print(graph)

    max_num = 0

    dx = [0,1,0,1]
    dy = [0,0,1,1]

    for i in range(0, n-m+1):
        catch()