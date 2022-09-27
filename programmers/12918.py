# 문자열다루기 기본 https://school.programmers.co.kr/learn/courses/30/lessons/12918
# 풀이완료

def solution(s):
    result = True

    if len(s)!=4 and len(s)!=6:
        result = False
    else:
        for i in range(len(s)):
            if ord(s[i])>=65:
                result = False
                break
    return result