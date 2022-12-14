# 그래프 탐색 알고리즘 : DFS / BFS
- 탐색 search란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
- 대표적인 그래프 탐색 알고리즘 DFS, BFS

# 미리 알아두어야 할 자료구조
## 스택 자료구조
- 먼저 들어온 데이터가 나중에 나가는 형식(선입후출)의 자료구조
- 입구와 출구가 동일한 형태로 스택을 시각화 할 수 있다.
- DFS 뿐만 아니라 다양한 알고리즘에서 사용된다.
- 파이썬에서 '리스트'로 표현, 자바에서 'stack'으로 표현

## 큐 자료구조
- 먼저 들어온 데이터가 먼저 나가는 형식(선입선출)의 자료구조
- 큐는 입구와 출구가 모두 뚫어있는 터널과 같은 형태로 시각화 할 수 있다.
- 파이썬에서 'deque' 라이브러리 사용
    - 리스트를 이용하면 pop() 수행 후 원소의 위치를 다시 설정해주어야해서 시간복잡도가 더 높아진다.
```py
from collections import deque

queue.append(n)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력
```
- 자바는 LinkedList에 구현된 Queue를 사용하는 것이 일반적이다.
```java
Queue<Integer> q = new LinkedList<>();
q.offer(5); // 삽입
q.poll(); // 꺼내기

// 먼저 들어온 원소부터 추출
while (!q.isEmpty()) {
    System.out.print(q.poll()+" ");
}
```

# 미리 알아두어야 할 함수
## 재귀 함수
- Recursive Function
- 자기 자신을 다시 호출하는 함수
- 단순한 형태의 재귀 함수 예제
    - 파이썬의 경우, 깊이 제한이 있어서 경고 메시지가 출력된다.

```py
def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()

recursive_function()
```

- 재귀 함수를 문제풀이에서 사용할 때, 재귀 함수의 종료 조건을 반드시 명시해야 한다.
- 종료조건을 제대로 명시하지 않으면 무한히 호출될 수 있다.
    - 종료조건을 포함한 재귀 함수 예제

```py
def recursive_function(i):
    if i == 100:
        return
    print(i,'번째 재귀함수에서', i+1, '번째 재귀함수를 호출합니다.')
    recursive_function(i+1)
    print(i,'번째 재귀함수를 종료합니다.')
recursive_function()
```

### 유의사항
- 재귀 함수를 잘 활용하면 복잡한 알고리즘을 간결하게 작성할 수 있으나
    - 오히려 다른 사람들이 이해하기 어려운 형태의 코드가 될 수 있으므로 신중하게 사용
- 모든 재귀함수는 반복문을 이용하여 동일한 기능 구현
- 재귀함수가 반복문보다 유리한 경우도 있고 불리한 경우도 있다.
- 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓인다.
    - 그래서 스택을 사용해야 할 때 구현상 스택 라이브러리 대신에 재귀 함수를 이용하는 경우가 많다.


# DFS
- Depth-First Search
- 깊이 우선 탐색
- 깊은 부분을 우선적으로 탐색하는 알고리즘
- 스택 자료구조(혹은 재귀 함수)를 이용하며, 구체적인 동작 과정은 다음과 같다.
    1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
    2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리. 방문하지 않은 인접 노트가 없으면 스택에서 최상단 노드를 꺼낸다.
    3. 더이상 2번의 과정을 수행할 수 없을 때까지 반복

# BFS
- Breadth-First Search
- 너비 우선 탐색
- 가까운 노드부터 우선적으로 탐색하는 알고리즘
- 큐 자료구조를 이용, 구체적인 동작 과정은 다음과 같다.
    1. 탐색 시작 노드를 큐에 삽입하고 방문처리
    2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
    3. 더이상 2번의 과정을 수행할 수 없을 때까지 반복
