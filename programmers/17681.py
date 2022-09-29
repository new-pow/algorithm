# 17681.py
# 비밀지도 https://school.programmers.co.kr/learn/courses/30/lessons/17681#

from dataclasses import replace

def solution(n, arr1, arr2):
    answer = []
    
    if 1>n or 16<n:
        return False
    else:
        map = [[0]*n for _ in range(n)]
        for i in range(n):
            temp = bin(arr1[i])[2: ]
            if len(temp) == n :
                map[i] = list(temp)
            elif len(temp) != n:
                map[i] = list('0'*(n-len(temp)) + temp)
            
        for i in range(n):
            temp = bin(arr2[i])[2: ]
            if len(temp) == n :
                temp_arr = list(temp)
            elif len(temp) != n:
                temp_arr = list('0'*(n-len(temp)) + temp)

            for j in range(n):
                if map[i][j] == '0':
                    map[i][j] = temp_arr[j]
                if map[i][j] == '1':
                    map[i][j] = '#'
                elif map[i][j] == '0':
                    map[i][j] = ' '
            
            str = ''.join(s for s in map[i])
            answer.append(str)

    return answer