## 베스트 셀러

### 문제 설명
- 입력
    - 첫째 줄: 정수 N -> 오늘 하루동안 팔린 책의 수 (N <= 1000)
    - 다음 N개의 줄: 책의 제목
- 출력
    - 가장 많이 팔린 책의 제목.
    - 만약 가장 많이 팔린 책이 여러 권일 경우, 사전 순으로 가장 앞서는 제목을 출력한다.
   
### 조건

### 아이디어
- Counter 함수를 사용해서 책 제목이 각각 몇 번 등장했는지 알아낸다.
    - from collections import Counter
- dict.values()가 max(dict.values())인 key들을 result 리스트에 저장한다.
- result.sort()

```
import sys
from collections import Counter

N = int(sys.stdin.readline())
books = []
for i in range(N):
    books.append(input())

books = Counter(books)

n = max(books.values())

result = []
for book, number in books.items():
        if number == n:
            result.append(book)
print(sorted(result)[0])

```
