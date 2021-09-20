## 1. 완주하지 못한 선수


```
from collections import Counter;

def solution(participant, completion):
    p = Counter(participant);
    c = Counter(completion);
    result = p-c;
    return list(result.keys())[0];
```

## 2. 전화번호 목록

```
def solution(phone_book):
    phone_book = sorted(phone_book);
    for pair in zip(phone_book, phone_book[1:]):
        print(pair);
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False;
    return True;
```

## 3. 위장

```
from collections import Counter;

def solution(clothes):
    answer = 1;
    category = [c[1] for c in clothes];
    category = Counter(category).values();
    print(type(category))
    for i in category:
        answer *= (i+1);
    return answer -1;
```
