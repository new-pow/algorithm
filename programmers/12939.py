# 12939.py
# 최댓값과 최솟값 https://school.programmers.co.kr/learn/courses/30/lessons/12939

s = "1 2 3 4"

s_arr = list(map(int, s.split()))

print('{} {}'.format(min(s_arr),max(s_arr)))