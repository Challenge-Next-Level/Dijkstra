## 2. 디스크 컨트롤러

### 설명
1) 입력: 2차원 배열(jobs)
    - jobs = [[작업이 요청되는 시점 , 작업의 소요시간]]
2) 출력: 작업의 요청부터 종료까지 걸린 시간의 평균 중 최소값

### 조건

### 아이디어
- 현재 시점에서 실행 가능한 task 중 작업 소요시간이 가장 짧은 task에게 우선순위를 주자.
- 현재 시점에서 실행 가능한 task가 없어도 계속 +1 해주면서 시간이 계속 흐르고 있음을 구현해야 한다.

```
import heapq

def solution(jobs):
    answer = 0
    now = 0 //현재 시점
    finished = 0 //실행 완료한 작업의 수
    before_j = -1 //바로 전 작업이 시작한 시점
    heap = []

    while finished < len(jobs):
        for j in jobs:
            if before_j <j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        if len(heap) > 0:
            on_j = heapq.heappop(heap)
            before_j = now
            now += on_j[0]
            answer += (now - on_j[1])
            finished += 1
        else:
            now += 1
    return int(answer/ len(jobs))
```
