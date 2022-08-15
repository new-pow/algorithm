# 0815_2606.py

# 첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다.
# 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

# 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.

def dfs(com):
    birus[com] = 1
    for i in range(n+1):
        if coms[i][com]==1:
            coms[i][com] = coms[com][i] = 0
            print(i,com)
            dfs(i)

# 컴퓨터 수
n = int(input())
coms = [[0]*(n+1) for _ in range(n+1)]

# 연결되어있는 쌍의 수
con = int(input())
for _ in range(con):
    a, b = map(int, input().split())
    coms[a][b] = coms[b][a] = 1
birus = [0]*(n+1)

dfs(1)
print(sum(birus)-1)