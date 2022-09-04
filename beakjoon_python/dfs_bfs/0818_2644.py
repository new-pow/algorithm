# 0818_2644.py

# 사람들은 1, 2, 3, …, n (1 ≤ n ≤ 100)의 연속된 번호로 각각 표시된다. 입력 파일의 첫째 줄에는 전체 사람의 수 n이 주어지고, 둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호가 주어진다. 그리고 셋째 줄에는 부모 자식들 간의 관계의 개수 m이 주어진다. 넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다. 이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호를 나타낸다.
# 각 사람의 부모는 최대 한 명만 주어진다.

# 입력에서 요구한 두 사람의 촌수를 나타내는 정수를 출력한다.
# 어떤 경우에는 두 사람의 친척 관계가 전혀 없어 촌수를 계산할 수 없을 때가 있다. 이때에는 -1을 출력해야 한다.

# --------------- dfs 써야한다.

# def dsf(x):
#     if x not in check:
#         global result
#         check[x] == False
#         for i in range(n):
#             if people[i][x] == 1 and i not in check:
#                 if i==end:
#                     break
#                 result += 1
#                 dsf(i)
#                 result -= 1

# n = int(input()) # 전체 사람 수
# start,end = map(int,input().split()) # 촌수를 구해야 하는 사람
# m = int(input()) # 부모자식 관계 수
# check = [True]+[False]*(n)
# result = 0

# people = [[0]*(n+1) for _ in range(n+1)]
# for _ in range(m):
#     x, y = map(int, input().split())
#     people[x][y] = people[y][x] = 1

# dsf(start)

# if check[end]==False:
#     result = -1

# print(result)

###### 다시 풀이 DFS ######

# 함수 dfs
def dfs(i):
    for j in relation[i]:
        if visit[j] == 0:
            visit[j] += visit[i]+1
            dfs(j)

# 문제 입력
n = int(input()) # 총 사람 수
start, end = map(int, input().split())
m = int(input()) # 관계 수

relation = [[] for _ in range(n+1)] # 관계 그래프
for _ in range(m):
    x,y = map(int, input().split())
    relation[x].append(y)
    relation[y].append(x)

visit = [0]*(n+1) # 방문 체크

dfs(start)


print(visit[end] if visit[end]>0 else -1)