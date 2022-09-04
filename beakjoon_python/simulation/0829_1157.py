# 0829_1157.py

# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

word = input().upper()
char = list(set(word))
count = [0]*(len(char))

for i in range(len(char)):
    for j in range(len(word)):
        if char[i] == word[j] :
            count[i] += 1

# for x in char :
#     cnt = word.count(x)
#     count.append(cnt)  # count 숫자를 리스트에 append

result = [i for i, ele in enumerate(count) if ele == max(count)]
print("?" if len(result)!=1 else char[result[0]])

########## 풀이

