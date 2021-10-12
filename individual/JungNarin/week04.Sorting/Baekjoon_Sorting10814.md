## 나이순 정렬

### 문제 설명
- 입력
  - 첫째 줄: 정수 1개(N) -> 회원의 수 
  - 그 다음 N개의 줄: 정수 1개 , 문자열 1개 -> 회원의 나이, 회원의 이름
- 출력
  - N개의 줄에 걸쳐 회원을 나이순, 나이가 같은면 가입한 순으로 한 줄에 한 명씩 나이와 이름을 공백으로 출력
  
### 조건

### 아이디어
- 첫 번째 정렬 기준은 나이이다.
  - 문자열을 정수로 바꿔서 age라는 변수에 넣어준다. (이름은 name)
- 나이가 같을 경우 가입한 순으로 출력한다.
  - 입력을 받을 때 나이, 이름, 그리고 순서도 같이 저장한다.
- 우선순위를 가지는 2가지 정렬 기준이 있다.
  - list.sort(key=lambda x: (x[0], x[2])) // x[0]: 나이, x[2]: 가입 순서

```
import sys

N = int(sys.stdin.readline())

names = []
for i in range(N):
    member = list(sys.stdin.readline().split())
    age = int(member[0])
    name = member[-1]
    names.append([age, name, i])

names.sort(key = lambda x:(x[0], x[2]))

for i in range(N):
    print(names[i][0], names[i][1])

```

