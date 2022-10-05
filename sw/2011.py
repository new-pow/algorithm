# 2011.py

def catch(a,b):
    global max_num
    sum = 0
    for i in range(len(dx)):
        for j in range(len(dy)):
            x = a+dx[i]
            y = b+dx[j]
            sum += graph[x][y]
        if max_num<sum:
            max_num = sum

t = int(input())
n, m = map(int, input().split())
max_num = 0
if n>=5 and 15>=n and m>=2 or m<=n:
    graph = []

    for _ in range(t):
        for _ in range(n):
            temp = list(map(int, input().split()))
            graph.append(temp)
        print(graph)

    dx = []
    dy = []

    for i in range(m):
        dx.append(i)
        dy.append(i)

    for i in range(n-m):
        for j in range(n-m):
            catch(i,j)

    print('#{} {}'.format(t, max_num))