# 1206.py
for t in range(1,11):
    n = int(input())
    result = 0
    buildings = list(map(int,input().split()))
    for i in range(2,n-2):
        h1 = buildings[i]-buildings[i-2]
        h2 = buildings[i]-buildings[i-1]
        h3 = buildings[i]-buildings[i+1]
        h4 = buildings[i]-buildings[i+2]
        if h1>0 and h2>0 and h3>0 and h4>0:
            result += min(h1,h2,h3,h4)
    print('#{} {}'.format(t, result))