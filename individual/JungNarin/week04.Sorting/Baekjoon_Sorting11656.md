## 접미사 배열

### 문제 설명
- 입력
    - 첫째 줄: 문자열 1개(S)
    
- 출력
    - 첫째 줄부터 S의 접미사를 <b>사전순</b>으로 한 줄에 하나씩 출력.
    
### 조건

### 아이디어
- 파이썬의 indexing을 사용해서 문자열을 왼쪽에서 오른쪽으로 하나씩 잘라준다.
- 오름파순으로 정렬해준다.
    - list.sort()

```
import sys

result = []
word = sys.stdin.readline()[:-1]
for i in range(len(word)):
    result.append(word[i:])
result.sort()

for r in result:
    print(r)
```
