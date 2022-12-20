# 12985.py
# 예상 대진표 https://school.programmers.co.kr/learn/courses/30/lessons/12985
# 1차시도 : 성공

def solution(n,a,b):
    answer = 0
    # 2**1로 나눈 몫이 같으면 1번
    # 2**2로 나눈 몫이 같으면 2번
    # 2**3로 나눈 몫이 같으면 3번
    
    for i in range(1,n):
        answer += 1
        round = pow(2, i)
        if (a-1)//round == (b-1)//round:
            # 몫이 바뀌는 지점을 고려하여 (그리고 인덱스는 0부터 시작하므로) a와 b에 1씩 더해주었다. 그랬더니 boom! 해결
            break

    return answer

n = 8
a = 4
b = 7
print(solution(n,a,b))