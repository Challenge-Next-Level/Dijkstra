## 아우으 우아으이야!!

### 문제 설명
- 입력
  - 첫째 줄: 정수 1개(N) -> 수직선 위에 그릴 선분의 개수 
  - 그 다음 N개의 줄: 좌표를 나타내는 정수쌍 (x,y)
- 출력
  - N개의 선분을 모두 그렸을 때, 수직선 위에 그어진 선분 길이의 총합의 출력
  
### 조건
- 좌표는 x가 증가하는 순으로, x가 같다면 y가 증가하는 순으로 주어진다.

### 아이디어
- agg : 이어진 선분의 길이를 저장해두는 리스트

- 3가지 경우로 나뉜다.
  - 부분만 겹치는 경우
    - agg[-1] = y - min
    - min은 그대로 유지
    - max는 새로운 x
    
  - 전체 다 겹치는 경우
    - continue;
    
  - 아예 안겹치는 경우
    - min과 max보다 x, y 로 업데이트
    - agg.append(y-x)
  
```
import sys

N = int(sys.stdin.readline())
points = []

for i in range(N):
    p = list(map(int, sys.stdin.readline().split()))
    points.append(p)

min_ = points[0][0]# -10
max_ = points[0][1]# 10
agg = [(max_ - min_)]
for i in range(1,N):
    x = points[i][0]# -1
    y = points[i][1]# 1a
    if x < max_ and y> max_:
        agg[-1] = y - min_;
        max_ = y;
        
    elif y<= max_:
        continue;
    
    elif x >= max_:
        agg.append(y - x)
        min_ = x;
        max_ = y;


print(sum(agg))
    

```
