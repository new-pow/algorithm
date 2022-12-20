# 0903_1316.py

from os import remove
import sys


result = 0;

# 단어 입력
n = int(input())

for _ in range(n):
    str = input()
    str_list = list(str)
    word_arr = []

    # 입력 받은 단어로 연속되는 단어 없애서 배열 만들기
    for i in range(len(str_list)-1):
        if (i<len(str_list) and str_list[i] == str_list[i+1]):
            continue
        else:
            word_arr.append(str_list[i])
    word_arr.append(str_list.pop(-1))

    # 그룹 단어 카운트
    if len(word_arr) == len(set(str)):
        result += 1

print(result)

## 해답
# n = int(input())

# group_word = 0
# for _ in range(n):
#     word = input()
#     error = 0
#     for index in range(len(word)-1):  # 인덱스 범위 생성 : 0부터 단어개수 -1까지 
#         if word[index] != word[index+1]:  # 연달은 두 문자가 다른 때,
#             new_word = word[index+1:]  # 현재글자 이후 문자열을 새로운 단어로 생성
#             if new_word.count(word[index]) > 0:  # 남은 문자열에서 현재글자가 있있다면
#                 error += 1  # error에 1씩 증가.
#     if error == 0:  
#         group_word += 1  # error가 0이면 그룹단어
# print(group_word)

## 해답2
# N=int(input())

# answer=0

# for i in range(N):
#     word = input()
#     for j in range(len(word)):
#         if j!=len(word)-1:
#             if word[j]==word[j+1]:
#                 pass
#             elif word[j] in word[j+1:]:
#                 break
#         else:
#             answer+=1
# print(answer)