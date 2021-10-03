## 3. 이중우선순위큐

### 문제 설명
1. 입력: 1차원 리스트(operations)
    - I 숫자: 큐에 주어진 숫자를 삽입
    - D 1: 큐에서 최댓값 삭제
    - D -1: 큐에서 최솟값 삭제
2. 출력
    - 모든 연산 처리 후 큐가 비어있으면: [0,0]
    - 그렇지 않으면: [최댓값, 최솟값]
    
### 조건
- 빈 큐에 데이터를 삭제하라는 연산이 주어질 경우 해당 연산은 무시된다.

### 아이디어
- 리스트 원소 하나는 문자열이고, 문자열[0]이 I인지, D인지에 따라 조건을 나눈다.
- 문자열[0]이 D라면 -1인지 1인지에 따라서 조건을 나눈다.
- 모든 연산을 처리한 후에 큐의 길이가 2보다 작으면 큐가 비어있는 것과 다름 없다.


```
def solution(operations):
    heap = []   
    for operation in operations:
        if operation[0] == "I":
            heap.append(int(operation[2:]))
        else:
            if len(heap) <= 0: //빈 큐일때 삭제하라는 연산은 무시하자
                continue
            else:
                if operation[2:] == '-1':
                    heap.remove(min(heap))
                else:
                    heap.remove(max(heap))
    if len(heap) >= 2:
        return [max(heap), min(heap)]
    else:
        return [0,0]
```
