N,K = map(int, input().split())

count = 0

for _ in range(N):
    if (N>=K):
        N = N/K
        count += 1
    elif(N!=1 and K!=1):
        N-=1
        count+=1
    elif(N==1):pass

print(count)

# 답변
# 아이디어 : 가능한 많이 최대한 나누기
# 나눌수 있다면 나누고 아니면 1을 빼자

# N, K을 공백 기준으로 구분하여 입력 받기
N,K = map(int, input().split())

result = 0

while True:
    #N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (N//K)*K
    result += (n-target)
    n = target
    #N이 K보다 작을 때, (더이상 나눌 수 없을 때, 반복문 탈출)
    if N<K:
        break
    #K로 나누기
    result +=1
    N //=K

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (N-1)
print(result)

# 이렇게 쓰는 이유 : 시간복잡도가 log시간 복잡도가 된다.
# 