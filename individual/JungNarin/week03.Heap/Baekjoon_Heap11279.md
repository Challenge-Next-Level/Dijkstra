## 최대힙

### 문제 설명
1. 배열에 자연수 x를 넣는다
2. 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.

- 입력
  - 첫째 줄: 정수 1개(N) -> 연산의 개수
  - 다음 N개의 줄: 연산에 대한 정보(x)
    - x == 자연수: 배열에 x라는 값을 추가하라
    - x == 0: 배열에서 가장 큰 값을 출력하고 배열에서 제거하라
- 출력
  - 입력이 0일때 해당하는 값 출력
  - 배열이 비어있을 경우 0이 입력된 경우 0을 출력
 

### 조건

### 아이디어
- 가장 큰 수가 heappop으로 먼저 힙을 빠져 나와야 한다.
  - 입력이 모두 자연수니까 -1을 곱해서 힙에 넣고, 뺄 때 -1을 다시 곱해서 양수로 만들어주자.
- 입력받은 정수가 0인 경우 or 자연수인 경우
- 힙이 비어 있는 경우 or 비어 있지 않은 경우

```
import heapq
import sys

heap = []
N = int(sys.stdin.readline())
for i in range(N):
    n = int(sys.stdin.readline())
    if n == 0:
        if heap:
            print(heapq.heappop(heap) * -1)
        else:
            print(0)
    else:
        heapq.heappush(heap, -1*n)

```


