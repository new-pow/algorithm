# 문자열다루기 기본 https://school.programmers.co.kr/learn/courses/30/lessons/12918
# 푸는 중

import sys
input = sys.stdin.readline

s = list(input())

s.pop()

result = 'ture'

for i in range(len(s)):
    if ord(s[i])>=65 and ord(s[i])<=122:
        result = 'false'

print(result)