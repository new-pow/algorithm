# 12981.py
# 영어 끝말잇기 https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer = [0, 0]
    turns = [0]*n
    says = []

    says.append(words[0])

    for i in range(1, len(words)):
        turn = (i%n)+1
        turns[i%n] += 1 # 차례 카운트
        if words[i] in says or words[i-1][-1]!=words[i][0]:
            return [turn, turns[i%n]]
        
        says.append(words[i])

    return answer

n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]

print(solution(n, words))

# def solution(n, words) :
#     turn = 1 # 처음 순서
#     before = words[0][-1]
#     for i in range(1, len(words)) :
#         # 단어의 시작이 잘못 되었거나 이전에 이미 말한적이 있다면
#         if words[i][0] != before or words[i] in words[:i] :
#             a, b = divmod(i, n) # 몫, 나머지
#             return [b + 1, a + 1]
#         else :
#             before = words[i][-1]

#     return [0, 0]