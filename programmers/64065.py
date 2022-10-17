# 64065.py
# 튜플 https://school.programmers.co.kr/learn/courses/30/lessons/64065
# 1회차 풀이 : 구현은 성공. 정규식 공부할 것 

def solution(s):
    answer = []
    arr = list(s[2:-2].split('},{'))
    for i in range(len(arr)):
        arr[i].replace('}','')
        arr[i].replace('{','')
        arr[i] = list(map(int,arr[i].split(',')))
    arr.sort(key=len)
    for i in arr:
        for j in i:
            if j not in answer:
                answer.append(j)

    return answer
s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"	
print(solution(s))
