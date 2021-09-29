## 기능 개발

### 문제설명
- 입력: 리스트 2개(progresses, speeds)
  - progresses: 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열(100이 작업의 완성임).
  - speeds: 각 작업의 개발 속도가 적힌 정수 배열
- 출력: 각 배포마다 배포되는 기능의 개수

### 조건
- 배포는 하루에 한 번만 할 수 있따.
- 배포는 하루의 끝에 이뤄진다.

### 아이디어
- 큐(Queue)를 사용한다.
    - progresses의 인덱스는 <b>우선순위</b>를 의미한다.
    - speeds도 같은 progress의 인덱스에 의존한다.
- 배포까지 걸리는 날을 담은 큐(d)를 만들자.
    - 100에서 해당 작업 진도를 빼고, 잔업 양을 속도로 나눈다.
    - 단, 나누어 떨어지지 않는 경우에 +1을 해야 하므로 math.ceil()을 사용한다.
- while문을 돌려서
    - result = 1 (default임.)
        - result란 같은 날 배포될 기능의 개수
    - 바로 뒤의 원소보다 현재 원소가 크거나 같을 경우: result += 1
    - 바로 뒤의 원소보다 현재 원소가 클 경우: result = 1 (다시 초기화)

```
from collections import deque;
import math;

def solution(progresses, speeds):
    pro = deque(progresses);
    sp = deque(speeds);
    result = 1;
    answer = []
    days = [];
    
    while pro:
        leftover = 100 - pro.popleft();
        s = sp.popleft();
        days.append(math.ceil(leftover / s) );
            
    d = deque(days);
    day = d.popleft();
    
    while d:
        d_day = d.popleft();
        if day >= d_day:
            result += 1;
        else:
            answer.append(result);
            result = 1;
            day = d_day;
            
    answer.append(result);
    return answer
```
