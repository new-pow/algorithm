# 17680.py
# 캐시 https://school.programmers.co.kr/learn/courses/30/lessons/17680
# 1차 풀이 : 실패
# 2차 풀이 : 성공 

def solution(cacheSize, cities):
    if cacheSize<0 or cacheSize>30:
        return False
    cache = []
    time = 0
    if cacheSize ==0:
        return 5*len(cities)
        
    for city in cities:
        city = city.lower()
        if city in cache:
            time += 1
            cache.pop(cache.index(city))
            cache.append(city)
        elif city not in cache:
            time += 5
            if len(cache)>=cacheSize:
                cache.pop(0)
            cache.append(city)
        else:
            time += 5
    return time 

cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	
print(solution(cacheSize,cities))