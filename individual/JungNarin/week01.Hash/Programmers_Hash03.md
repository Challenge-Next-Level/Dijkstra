## 3. 위장

### 문제 설명
- 파라미터: 2차원 리스트 1개
  - clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
- 반환값: 서로 다른 옷의 조합 수

### 조건
- clothes의 각 행은 [의상의 이름, 의상의 종류]로 이뤄져 있다.
- 같은 이름을 가진 의상은 존재하지 않는다.
- 최소한 한 개의 옷은 입는다.

### 아이디어
- 옷의 이름은 중요하지 않다.
  - 옷의 종류를 키로, 그 종류가 몇 번 등장했는지가 값으로 하는 딕셔너리를 만들자.
  - collections 모듈의 Counter 함수를 사용하자.
 - 옷의 종류가 뭔지, 구체적인 이름은 중요하지 않다.
  - (옷의 종류당 등장 횟수 + 1)들을 곱한 후 - 1 을 해서 모두 안입은 경우를 제외해준다. (통계의 조합과 같은 느낌)
 
```
from collections import Counter;

def solution(clothes):
    answer = 1;
    category = [c[1] for c in clothes];
    category = Counter(category).values();
    for i in category:
        answer *= (i+1);
    return answer -1;
```
