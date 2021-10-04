## 카드 합체 놀이

### 문제 설명
1. 석환이는 자연수가 쓰여진 n장의 카드를 가지고 있다.
2. x번 카드와 y번 카드를 골라 2장에 쓰여진 두 수를 더한다. (x != y)
3. 계산한 값을 x번 카드와 y번 카드 2장에 모두 덮어 쓴다.
4. 카드 합체는 총 m번 진행한다.
5. 합체가 끝난 후 n장의 카드에 적혀 있는 수의 합이 이 놀이의 점수가 된다.
6. 이 점수를 가장 작게 만들고 싶다.

### 입력
- 첫 번째 줄: 정수 2개
  - n : 카드의 개수
  - m : 카드 합체 횟수
- 두 번째 줄: 맨 처음 카드의 상태를 나타내는 n개의 자연수

### 출력
- m번의 카드 합체 후 n장의 카드에 적힌 수의 합 중 최소값

### 아이디어
- 결과 값이 가장 작으려면, 매번 합체때 가장 작은 두 수를 합체해줘야 한다.

```
import sys
import heapq

N, M = map(int,sys.stdin.readline().split())

heap = list(map(int,sys.stdin.readline().split()))
heapq.heapify(heap);
    
for i in range(M):
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    heapq.heappush(heap, first + second)
    heapq.heappush(heap, first + second)

print(sum(heap))
```
