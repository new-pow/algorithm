# 실전에서 유용한 표준 라이브러리

## 내장 함수
- 기본 입출력 함수부터 정렬 함수까지 기본적인 함수 제공
### 자주 사용하는 내장 함수
1. sum()
2. min(), max()
3. eval()
4. sorted(배열)
    - sorted([1,2,3], reverse=True)
    - result = sorted(array, key=lambda x: x[1], reverse=True)

## itertools
- 순열과 조합 라이브러리는 코딩 테스트에서 자주 사용
1. 순열
```py
from itertools import permutations
data = ['A', 'B', 'C'] #데이터 준비
result = list(permutations(data, 3)) # 모든 순열 구하기
```
2. 조합
```py
from itertools import combinations
data = ['A', 'B', 'C'] #데이터 준비
result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합 구하기
```

3. 중복 순열과 중복 조합
```py
from itertools import product
data = ['A','B','C'] # 데이터 준비
result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기 (중복 허용)
print(result)
```

```py
from itertools import combinations_width_replacement
data = ['A','B','C']
result = list(combinations_with_replacement(data,2)) # 2개를 뽑는 모든 조합 구하기 (중복 허용)
```

## heapq
- 일반적으로 우선순위 큐 기능을 구현하기 위해 사용

## bisect
- 이진탐색(Binary Search) 기능을 제공

## collections
- 덱, 카운터 등의 유용한 자료구조 포함

1. Counter
- 리스트와 같은 반복 가능한 객체가 주어졌을 때, 원소의 등장횟수를 셀 수 있다.

```py
from collections import Counter
counter = Counter([1,2,3,3,4,5])
print(counter[2]) #2가 등장한 횟수
print(dict(counter)) #사전 자료형으로 반환
```

## math
- 필수적인 수학적 기능 제공
- 팩토리얼 제곱근, 최대공약수, 삼각함수 관련 함수부터 파이와 같은 상수를 포함

1. 최대 공약수와 최소 공배수
    - 최대 공약수 math라이브러리의 gcd()
```py
import math

def lcm(a,b):
    return a*b

a=21
b=14

print(math.gcd(21,14)) #최대 공약수
print(lcm(21,14)) #최소 공배수
```

