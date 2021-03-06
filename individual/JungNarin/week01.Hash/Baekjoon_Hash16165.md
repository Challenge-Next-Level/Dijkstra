## 걸그룹 마스터 준석이

### 문제 설명
- 입력
  - 첫 번째 줄: 걸그룹 수(N), 맞혀야 할 문제 수(M)
  - 두 번째 줄~: 걸그룹 팀 이름, 인원 수, 멤버 이름 (한 줄씩)
  - 그 다음 줄: M 개의 퀴즈 입력
    - 각 퀴즈는 두 줄로 이뤄져 있다. 
    - 첫 줄: 팀의 이름 or 멤버 이름
    - 두번째 줄(퀴즈의 종류): 0(첫 줄이 팀의 이름일 경우) or 1(첫 줄이멤버 이름일 경우)

- 출력
  - 첫 번째 줄~: 퀴즈에 대한 답 출력.
  - 퀴즈의 종류가 0일 경우: 해당 팀의 멤버 이름 사전순으로 한 줄 씩 출력.
  - 퀴즈의 종류가 1일 경우: 해당 멤버가 속한 팀의 이름을 출력.
  
### 조건
- 같은 팀의 동명이인은 없다.
- 서로 다른 걸그룹에 동명이인은 없다.

### 아이디어
- 팀 이름을 키로 하고, 멤버 이름을 값으로 갖는 딕셔너리를 만들자.
  - for문을 돌려 members라는 리스트에 멤버 이름을 넣는다.
- 퀴즈의 종류 == 0: 
  - 딕셔너리에서 입력받은 팀이름의 값을 출력하자. 
  - 단, 사전순으로 멤버 이름을 출력해야 하므로 sorted()함수를 사용하자.
- 퀴즈의 종류 == 1:
  - 딕셔너리의 값들에서 해당 멤버의 이름이 포함되어 있는 값을 갖는 키를 출력하자.
  - .keys() 함수를 사용해서 딕셔너리의 값(여기에선 리스트)들을 모아둔 리스트를 가져오자.
  
  
