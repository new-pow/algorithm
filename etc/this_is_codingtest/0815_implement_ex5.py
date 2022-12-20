# 문자열 S를 정렬하자
# 문자 - 숫자 오름차순 정렬

S = list(input())
sum = 0
strings = []

for s in S:
    if ord(s)<65:
        sum += int(s) 
    else:
        strings.append(s)

strings.sort()

for i in range(len(strings)):
    print(strings[i], end='')
print(sum)

##### 해답 #####
data = input()
result = []
value = 0

# 문자 1개씩 확인
for x in data :
    # 알파벳인 경우 결과리스트에 삽입
    if x.isalpha():
        result.append(x)
    #숫자인 경우
    else:
        value += int(x)
result.sort()
# 숫자가 하날도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))
# 최종 결과 출력(리스트를 문자열로 변환하여 출력
print(''.join(result))