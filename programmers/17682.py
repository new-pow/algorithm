# 17682.py

from tkinter import N


def solution(dartResult):
    answer = 0
    nums = []
    # 3회로 분할하기
    dartResult = dartResult.replace('*','**')
    dartResult = dartResult.replace('#','##')
    arr = []
    for i in range(len(dartResult)-1):
        if i%2 ==0:
            arr.append((dartResult[i]+dartResult[i+1]))

    # 문자열 교체하기 + 계산하기
    for i in range(len(arr)):
        if arr[i][1] == 'S': arr[i] = int(arr[i][0])**1
        elif arr[i][1] == 'D': arr[i] = int(arr[i][0])**2
        elif arr[i][1] == 'T': arr[i] = int(arr[i][0])**3

    # *와 # 연산하기
    for i in range(len(arr)):
        if arr[i] != '**' and arr[i] != '##':
            nums.append(arr[i])
        elif arr[i] == '**':
            if i>0:
                nums[-1] *= 2
            if i>1:
                nums[-2] *= 2
        elif arr[i] == '##':
            nums[-1] *= (-1)

    # 연산하기
    for i in range(len(nums)):
        answer += int(nums[i])
    return answer

solution("1D#2S*3S")