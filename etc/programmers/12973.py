# 12973.py
# 짝지어 제거하기 https://school.programmers.co.kr/learn/courses/30/lessons/12973
# 1회차 풀이 : 실패

def solution(s):
    answer = 0
    arr = []
    before = s[0]

    while True:
        replace = 0
        check = 0
        arr.append(before)
        print(arr)

        for i in range(1,len(s)):
            if arr.pop()==s[i]:
                s = s.replace(s[i]+s[i], "")
                replace += 1
                arr.pop()
        if replace == check and s=="":
            answer = 1
            break
        elif replace == check and s!="":
            break
    return answer


print(solution('baabaa'))