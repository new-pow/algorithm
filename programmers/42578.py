# 42578.py
# 위장 https://school.programmers.co.kr/learn/courses/30/lessons/42578
# 1회차 풀이분 : 

def solution(clothes):
    sets = {}
    for i in range(len(clothes)):
        if clothes[i][1] not in sets:
            sets[clothes[i][1]] = 2
        else:
            sets[clothes[i][1]] += 1
    
    answer = 1

    for i in sets.values():
        answer *= i # 경우의 수
    answer -= 1 # 모든 요소를 착용하지 않을 때

    return answer

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	

print(solution(clothes))