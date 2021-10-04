## 절댓값 힙

### 문제설명
1. 배열에 정수 x(0이 아닌)를 넣는다.
2. 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 
3. 절댓값이 가장 작은 값이 여러 개일때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.

### 입력
- 첫째 줄: 정수 1개(N) -> 연산의 개수
- 다음 N개의 줄: 정수 x
    - x == 0: 배열에서 가장 작은 값 출력 + 배열에서 그 값 제거
    - x == 정수: 배열에 x라는 값 추가
    
### 출력
- 입력에서 0이 주어진 횟수만큼 답을 출력
- 만약 배열이 비어 있는 경우: 0이 입력되면 0을 출력한다.

### 아이디어
- 힙에 삽입할 때 -1이 1보다 높은 우선순위를 가져야 한다.
    - -1 + 0.5 = -0.5
    -  1 + 0.5 = 1.5
    -  즉, x에 0.5를 더해주면 -1과 1이 우선순위를 다르게 가지면서
    -  동시에 다른 정수 2, -2 등등의 우선순위에는 영향을 받지 않는 채로 우선순위를 가질 수 있게 된다.
    -  heapq.heappush(heap, (abs(x),x+0.5)
- 절대값
    - abs(x)
 
 ```
 import sys
import heapq
import math

heap = []
N = int(sys.stdin.readline())

for i in range(N):
    n = int(sys.stdin.readline())

    if n == 0:
        if heap :
            x = heapq.heappop(heap)
            print(math.floor(x[1]))
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(n), n+0.5))
    

 ```
   
