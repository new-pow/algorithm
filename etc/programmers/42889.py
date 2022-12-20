# 42889.py

from multiprocessing.resource_sharer import stop


def solution(N, stages):
    if N<1 or N>500 or len(stages)<1 or len(stages)>200000:
        return False
    else:
        answer = []
        stops = [0] + [0] * (N+1) #실패율 배열
        stages.sort()
        
        for i in range(len(stages)): #멈춰있는 사람
            stops[stages[i]] += 1
        

        reach = [len(stages)] + [1] * (N+1)
        for j in range(1, len(stops)): #도달한 사람
            reach[j] = reach[j-1] - stops[j-1]
        
        fail_rate = [0] + [0] * (N+1)
        for i in range(len(stops)): #실패율 배열
            if reach[i]!=0:
                fail_rate[i] = stops[i]/reach[i]
            else:
                fail_rate[i] = 0
        
        fail_rate[0] = -1
        fail_rate[-1] = -1
        
        for i in range(1, N+1): #실패율대로 내림차순
            temp = max(fail_rate)
            answer.append(fail_rate.index(temp))
            fail_rate[fail_rate.index(temp)] = -1
        
    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

solution(N, stages)