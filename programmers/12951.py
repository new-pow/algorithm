# # 12951.py

# def solution(s):
#     arr = list(s.split())
#     answer = ''
#     for i in range(len(arr)):
#         if arr[i][0].isalpha():
#             if arr[i][0] != arr[i][0].upper():
#                 arr[i] = arr[i].lower().capitalize()
        
#     return ' '.join(arr)

# s = "3people unFollowed me"
# solution(s)
# print(solution(s))


# 12951.py

# def solution(s):
#     arr = list(s.split())
#     answer = ''
#     for i in range(len(arr)):
#         arr[i] = arr[i].lower().capitalize()
        
#     return ' '.join(arr)

# s = "3people unFollowed me"
# solution(s)
# print(solution(s))

# def solution(s):
#     arr = s.split()
#     answer = []
#     for i in arr:
#         answer.append(i.lower().capitalize())
        
#     return ' '.join(answer)

# s = "3people unFollowed me"
# solution(s)
# print(solution(s))

def solution(s):
    arr = s.split(' ')
    answer = []
    for i in arr:
        answer.append(i.lower().capitalize())
        
    return ' '.join(answer)

s = "3people unFollowed me"
solution(s)
print(solution(s))