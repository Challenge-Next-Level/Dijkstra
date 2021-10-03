## 1. 더 맵게

### 문제 설명
1) 모든 음식의 스코빌 지수를 K이상으로 만들기 위해 다음과 같은 수식을 사용해 새로운 음식을 만든다.
    - 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
2) 입력: 스코빌 지수를 담은 배열(scoville), 원하는 스코빌 지수(K)
3) 출력: 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수

### 조건
- 리스트 내 모든 값을 다 더해도 K 이상으로 만들 수 없을 경우는 -1를 반환


### 아이디어
- 리스트 내의 가장 작은 수가 K 미만이면 섞어야 할 필요가 있다.
    - 오름차순으로 정렬해주는 heap을 사용하자
    - import heapq
- heap의 0번째 원소가 K보다 작은데 길이가 2보다 작으면 더이상 가능성이 없다.


```
import heapq

def solution(scoville, K):
    heap = []
    cnt = 0
    for s in scoville:
        heapq.heappush(heap, s)

    while heap[0] < K:
        if len(heap) >= 2:
            cnt += 1
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            new = first + (second *2)
            heapq.heappush(heap, new)
        else:
            return -1;

    return cnt
```

