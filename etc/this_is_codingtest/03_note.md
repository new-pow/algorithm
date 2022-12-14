# 자료형
- 모든 프로그래밍은 결국 데이터를 다루는 행위
    - 자료형에 대한 이해는 프로그래밍의 길에 있어서의 첫걸음
- 파이썬의 자료형으로 다음이 있다.
    - 정수형
    - 실수형
    - 복소수형
    - 문자열
    - 리스트
    - 튜플
    - 사전

# 정수형
- Integer 정수를 다루는 자료형
- 양의 정수, 음의 정수, 0

# 실수형
- 소수점 아래 데이터를 포함하는 수 자료형
- 파이수에서는 변수에 소수점을 붙인 수를 대입하면 자동으로 실수형 변수로 처리된다.
- 소수부가 0이거나 정수부가 0일때 0을 생략할 수 있다.

## 지수표현 방식
- 파이썬에서는 e나 E를 이용한 지수표현 방식 사용 가능
    - e나 E 다음에 나오는 수를 10의 지수부를 의미합니다.
    - 1e9 -- 10^9
- 지수 표현 방식은 임의의 큰 수를 표현하기 위해 자주 사용된다.
- 최단 경로 알고리즘에서는 도달할 수 없는 노드에 대해 최단 거리를 무한INF로 설정하곤 한다.
- 이때 가능한 최댓값이 10억 미만이라면 무한의 값으로 1e9를 이용할 수 있다.
- 결과값은 실수형으로 나온다.

## 실수형 더 알아보기
- 지금 가장 널리 쓰이는 IEEE754 표준에서는 실수형을 저장하기 위해 4바이트, 혹은 8바이트의 고정된 크기의 메모리를 할당하므로, 컴퓨터 시스템은 실수 정보를 표현하는 정확도에 한계를 가진다.
- 예를 들어 10진수 체계에서는 0.3과 0.6을 더한 값이 0.9로 정확히 떨어진다.
    - 하지만 2진수에서는 0.9를 정확히 표현할 수 있는 방법은 없다.
    - 컴퓨터는 최대한 0.9와 가깝게 표현하지만 미세한 오차가 발생한다.
- 개발 과정에서는 실수값을 제대로 비교하지 못해서 원하는 결과를 엊지 못할 수 있다.
- 이럴때는 round() 함수를 이용할 수 있으며, 이렇나 방법이 권장된다.
- 예를 들어 123.456을 소수 셋째자리에서 반올림하려면 `round(123.456,2)` 라고 작성

## 수 자료형의 연산
- 수 자료형에 대하여 사칙연산과 나머지 연산자가 많이 사용된다.
- 단 나누기 연산자(/)를 주의해서 사용
    - 나눠진 결과는 실수형으로 반환한다.
- 다양한 로직을 설계할 때 나머지 연산자(%)를 이용해야 할 때가 많다.
- 몫을 얻기 위해 몫 연산자(//)
- 거듭 제곱 연산자 (**)

# 리스트 자료형
- 여러 개의 데이터를 연속적으로 담아 처리하기 위해 사용하는 자료형
    - 사용자 입장에서 C나 자바에서의 배열(Array)의 기능 및 연결 리스트와 유사한 기능 지원
    - C++의 STL vector와 기능적으로 유사
    - 리스트 대신에 배열 혹은 테이블이라고 부르기도 함
- 다른 언어에서 배열 이용할 때 list이용하면 된다.

## 리스트의 초기화
- 리스트는 대괄호[] 안에 원소를 넣어 초기화, 쉼표(,)로 원소를 구분
- 비어 있는 리스트를 선언하고자 할 때는 list() 혹은 간단히 []를 이용할 수 있다.
- 리스트의 원소에 접근할때는 [] 안에 숫자를 넣는다.
    - 0부터 시작한다.
```py
# 직접 초기화
a = [1,2,3,4]

# 네 번째 원소만 출력
print(a[3])

# 뒤에서 두번째 원소 출력
pinrt(a[-2])

# 슬라이싱
print(a[2:3])

# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0]*n
```

## 리스트 컴프리 헨션

```py
# 0부터 9까지 수를 포함하는 리스트
array = [i for i in range(10)]

# 0부터 19까지 홀수만 포함하는 리스트
array = [i for i in range(20) if i%2 == 1]
```

## 리스트 메소드
1. append()
    - `변수명.append()`
    - 리스트에 원소를 하나 삽입
    - O(1)
2. sort()
    - `변수명.sort()`, `variable.sort(reverse=True)`
    - 기본 정렬기능으로 오름차순, 내림차순 정ㄹ려
    - O(NlogN)
3. reverse()
    - `variable.reverse()`
    - 리스트의 원소 순서를 모두 뒤집어 놓는다.
    - O(N)
4. insert()
    - `insert(삽입할 위치 인덱스, 삽입할 값)`
    - 특정한 인덱스 위치에 원소를 삽입할 때 사용한다.
    - O(N)
5. count()
    - `variable.count(value)`
    - 리스트에서 특정한 값을 가지는 데이터 개수를 셀 때 사용한다.
    - O(N)
6. remove()
    - `variable.remove(value)`
    - 특정한 값을 갖는 원소를 제거하는데, 값을 가진 원소가 여러 개면 하나만 제거한다.
    - O(N)
    - 1개의 원소만 제거

### 리스트에서 특정 값을 가지는 원소를 모두 제거
```py
a = [1,2,3,4,5,5,5]
remove_set = {3,5} #집합 자료형

# remove_list에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]
```

# 문자형 자료형
- 문자열 변수를 초기화할때 큰 따옴표나 작은 따옴표 사용
- 문자열 안에 큰따옴표나 작은따옴표가 포함되어야 하는 경우가 있다.
    - 전체 문자열을 큰따옴표로 구성하는 경우, 내부적으로 작은따옴표를 포함할 수 있다.
    - 전체 문자열을 작은따옴표로 구성하는 경우, 내부적으로 큰따옴표를 포함시킬 수 있다.
    - 혹은 백슬래시 \ 를 이용하면, 큰따옴표나 작은따옴표를 원하는 만큼 포함시킬 수 있다.

## 문자열 연산
- + : 문자열이 뒤쪽으로 연결
- * : 양의 정수와 곱하는 경우, 문자열이 그만큼 여러번 더해진다.
- 문자열에서 인덱스를 가져올수있지만, 인덱스 변경이 불가능하다.

# 튜플 자료형
- 리스트와 유사하지만 몇가지 차이점
    - 한 번 선언된 값을 변경할 수 없다.
    - 리스트는 대괄호[] 를 이용하지만 튜플은 소괄호()를 이용한다.
- 상대적으로 리스트에 비해 공간 효율적
```py
a = (1,2,3,4,5,6)

# 네번째 원소 출력
print(a[3])
```

## 튜플 사용하면 좋은 경우
1. **서로 다른 성질**의 데이터를 묶어서 관리
    - 최단 경로 알고리즘에서 (비용, 노드번호) 등의 형태로 튜플 자료형을 자주 사용한다.
2. 데이터의 나열을 **해싱(Hashing)의 키값**으로 사용해야 할 때
    - 튜플은 변경이 불가능하므로 리스트와 다르게 키값으로 사용될 수 있다.
3. 리스트보다 메모리를 효율적으로 사용해야 할 때

# 사전 자료형
- 키와 값을 데이터 쌍으로 가지는 자료형
    - 순차적으로 저장과 대조적
- 원하는 '변경 불가능한 자료형'을 키로 사용할 수 있다.
- 파이썬의 사전 자료형은 해시 테이블을 이용하므로 데이터의 조회 및 수정에 있어서 O(1)의 시간을 처리할 수 있다.

```py
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

data[key] = value

# 특정 키 존재하는지 찾기
if '사과' in data:
    print("존재합니다.")

b = {
    '홍길동' : 97,
    '이순신' : 98
}
```

## 사전 자료형 메소드
- 키 데이터만 뽑아서 리스트로 이용 keys() 함수
- 값 데이터만 뽑아서 리스트로 이용 values() 함수

# 집합자료형
- 중복을 허용하지 않는다.
- 순서가 없다.
- 리스트 혹은 문자열을 이용해서 초기화 할 수 있다.
    - set() 함수 이용
- 혹은 중괄호{} 안에 각 원소를 , 로 구분하여 삽입해서 초기화 할 수 있다.
- 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있다.

## 연산
- 합집합, 교집합, 차집합 연산 가능
    - |, &, -

## 관련 함수

```py
data = set([1,2,3])

# 새로운 원소 추가
data.add(4)

# 새로운 원소 여러개 추가
data.update([5,6])
print(data)

# 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)
```

## 사전 자료형과 집합 자료형의 특장
- 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없다.
    - 사전의 키(key) 혹은 집합의 원소를 이용해 O(1)의 시간 복잡도로 조회한다.