## 크리스마스 선물

### 문제 설명
1. 산타가 아이들에게 선물을 나눠준다.
2. 산타는 중간중간 거점을 들려 선물을 충전한다.
3. 산타는 아이들을 만날 때 본인이 가지고 있는 선물 중 가장 가치 있는 걸 선물한다.

### 입력
- 첫 번째 줄: 정수 1개(n) -> 아이들과 거점을 방문한 횟수
- 다음 n줄: a 와 a개의 숫자
  - a == 0: 아이를 만났다
  - a != 0: 거점을 들렀다. 뒤에 나올 a개의 선물을 충전한다.
  
### 출력
- a == 0: 아이에게 준 선물의 가치를 출력
- 가지고 있는 선물이 없다면: -1 출력

### 아이디어
- 가장 큰 숫자를 먼저 출력해야 한다.
  - 숫자 * -1로 힙에 넣고
  - 다시 밸 때 -1을 곱해서 출력한다.

```
import sys
import heapq

heap = []
n = int(sys.stdin.readline())

for i in range(n):
    a = sys.stdin.readline()
    if a[0] == '0':
        if heap:
            print(heapq.heappop(heap) * -1)
        else:
            print(-1)
    else:
        a = list(map(int, a.split()))
        for i in a[1:]:
            heapq.heappush(heap, -1 * i)
```
