## 프린터

### 문제 설명
- 입력: 리스트 1개(priorities), 정수 1개(location)
    - priorities: 인쇄 대기 목록에 있는 문서들의 중요도
    - location: 인쇄 요청한 문서가 처음의 대기 목록의 어떤 위치에 있는지 알려주는 location
    
- 출력: 인쇄 요청한 문서가 몇 번째로 인쇄되는지


### 조건
1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼낸다.
2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 하나라도 존재하면 J를 대기목록의 가장 마지막에 넣는다.
3. 그렇지 않으면 J를 인쇄한다.
- 중요도는 1~9로 표현되며, 숫자가 클수록 중요도가 높다.
- location은 인덱스를 의미한다.
- 

### 아이디어
- 큐를 사용하자
    - prioirites를 큐로 만들자.(p_queue)
    
- 처음 입력으로 받은 priorities의 인덱스를 저장해둘 큐(i_queue)를 만들자.
    - location으로 찾고 싶은 문서(원소)가 결과적으로 마지막에 만들어질 인덱스 리스트(i_list)의 몇번째에 위치하는지 알기 위해 필요하다.
    - p_queue의 원소의 인덱스 변화와 i_queue의 원소의 인덱스 변화는 동일하다.
    
 - 중요도를 비교하기 위해 max()함수를 이용하자.
    - p_queue.popleft()한 값이 max이면: i_queue.popleft()한 값을  i_list의 맨 뒤에 추가한다.
    - p_queue.popleft()한 값이 max가 아니면: p_queue.popleft()한 값을 p_queue의 맨 뒤에 추가하고 i_queue.popleft()한 값도 i_queue의 맨 뒤에 추가한다.
    
- i_list에서 location과 같은 값의 인덱스를 얻기 위해 index()를 사용하자.



```
from collections import deque;

def solution(priorities, location):
    p_queue = deque(priorities);
    i_queue = deque(list(range(priorities)));
    i_list = []
    
    while p_queue:
        p = p_queue.popleft()
        if p_queue:
            if p < max(list(p_queue)):
                p_queue.append(p);
                i = i_queue.popleft();
                i_queue.append(i);
            else:
                i = i_queue.popleft();
                i_list.append(i);
        else:
            i = i_queue.popleft();
            i_list.append(i);
    return i_list.index(location) +1;
```
