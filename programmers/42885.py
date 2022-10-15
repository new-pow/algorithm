# 42885.py
# 구명보트 https://school.programmers.co.kr/learn/courses/30/lessons/42885
# 1회차 풀이 성공

from collections import deque
from tkinter.tix import Tree


def solution(people, limit):
    answer = 0
    people.sort()
    q = deque(people)
    boart = 0
    boart += q.pop()
    while q:
        if limit - boart >= q[-1]:
            boart += q.pop()
        elif limit - boart >= q[0]:
            boart += q.popleft()
        else:
            answer += 1
            boart = 0
    
    if boart != 0:
        answer +=1

    return answer

people = [70, 80, 50]
limit = 100

print(solution(people,limit))