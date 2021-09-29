## 1. 완주하지 못한 선수

### 문제 설명
- 파라미터: 리스트 2개(participant, completion)
    - participant: 마라톤 참가자
    - completion: 마라톤 완주자
- 반환값: 완주하지 못한 선수의 이름

### 조건
- completion의 길이 = participant의 길이 - 1
    - 즉, 완주하지 못한 사람은 <b>한 명</b>이다.
- 참가자 중에는 동명이인이 있을 수 있다.

### 아이디어
- participant에는 있지만, completion에 없는 이름을 반환하자.
- 단, 위의 아이디어만으로는 '동명이인'인 참가자를 가려낼 수 없다.
    - ex) participant = ["a", "a", "b", "c"], completion = ["a", "b", "c"]
- 따라서 <b>이름</b>을 <b>key</b>로, <b>각 리스트에서의 개수</b>를 <b>value</b>로 하는 딕셔너리를 만들자.
    - collections 모듈의 Counter함수 사용하자.
- Counter(participant) - Counter(completion) = 같은 키의 값들을 뺀다. 이때 값이 0이 되면 해당 pair는 삭제된다.
    - 남은 한 개의 pair의 키가 바로 반환값이다.
    
```
from collections import Counter;

def solution(participant, completion):
    p = Counter(participant);
    c = Counter(completion);
    result = p-c;
    return list(result.keys())[0];
```
