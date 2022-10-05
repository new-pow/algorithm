# 17682.py

def solution(dartResult):
    answer = 0

    score_list = []
    score_idx = -1
    idx = 0
    while idx < len(dartResult):
        if dartResult[idx].isdigit():
            num_idx = idx
            while dartResult[num_idx].isdigit():
                num_idx += 1
            if dartResult[num_idx] == 'S':
                score_list.append(int(dartResult[idx:num_idx]))
            elif dartResult[num_idx] == 'D':
                score_list.append(int(dartResult[idx:num_idx]) ** 2)
            elif dartResult[num_idx] == 'T':
                score_list.append(int(dartResult[idx:num_idx]) ** 3)
            score_idx += 1
            idx = num_idx + 1
        else:
            if dartResult[idx] == '*':
                if score_idx == 0:
                    score_list[score_idx] *= 2
                else:
                    score_list[score_idx - 1] *= 2
                    score_list[score_idx] *= 2
            elif dartResult[idx] == '#':
                score_list[score_idx] *= -1
            idx += 1
    
    answer = sum(score_list)

    return answer

# def solution(dartResult):
#     answer = 0
#     nums = []
#     idx = 0
#     temp = 0
#     while idx < len(dartResult):
#         if dartResult[idx] == 'S':
#             temp = int(temp)**1
#         elif dartResult[idx] == 'D':
#             temp = int(temp)**2
#         elif dartResult[idx] == 'T':
#             temp = int(temp)**3
#         elif dartResult[idx] == '*':
#             nums[-1] = nums[-1] * 2
#             temp = int(temp) * 2
#         elif dartResult[idx] == '#':
#             temp = int(temp)*(-1)
#         else:
#             nums.append(temp)
#             temp = dartResult[idx]
#         idx += 1
#     # 연산하기
#     for i in range(len(nums)):
#         answer += int(nums[i])
#     return answer

# solution("1D#2S*3S")


# --
# def solution(dartResult):
#     answer = 0
#     nums = []
#     # 3회로 분할하기
#     dartResult = dartResult.replace('*','**')
#     dartResult = dartResult.replace('#','##')
#     arr = []
#     for i in range(len(dartResult)-1):
#         if i%2 ==0:
#             arr.append((dartResult[i]+dartResult[i+1]))

#     # 문자열 교체하기 + 계산하기
#     for i in range(len(arr)):
#         if arr[i][1] == 'S': arr[i] = int(arr[i][0])**1
#         elif arr[i][1] == 'D': arr[i] = int(arr[i][0])**2
#         elif arr[i][1] == 'T': arr[i] = int(arr[i][0])**3
        
#         if arr[i] != '**' and arr[i] != '##':
#             nums.append(arr[i])
#         elif arr[i] == '**':
#             if i>0:
#                 nums[-1] *= 2
#             if i>1:
#                 nums[-2] *= 2
#         elif arr[i] == '##':
#             nums[-1] *= (-1)

#     # 연산하기
#     for i in range(len(nums)):
#         answer += int(nums[i])
#     return answer