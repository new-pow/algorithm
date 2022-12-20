# 0903_2941.py

# char = ['c=','c-','dz=','d-','lj','nj','s=','z=']

# # 문자 입력받기
# word = input()
# result = 0
# n = 0 #슬라이싱 넘버

# # 앞에서부터 비교하기
# while n < len(word):
#     if word[n:n+3] in char:
#         n+=3
#         result +=1
#     elif word[n:n+2] in char:
#         n+=2
#         result +=1
#     else:
#         n+=1
#         result +=1

# print(result)

# 풀이1

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in croatia :
    word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수
print(len(word))