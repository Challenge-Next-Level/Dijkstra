### 조이스틱

**문제 설명**
- 조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
- ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA


- 조이스틱을 각 방향으로 움직이면 아래와 같습니다.
    - ▲ - 다음 알파벳
    - ▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
    - ◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
    - ▶ - 커서를 오른쪽으로 이동


- 예를 들어 아래의 방법으로 "JAZ"를 만들 수 있습니다.
    - 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
    - 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
    - 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.


- 따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
- 만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.


**제한 사항**
- name은 알파벳 대문자로만 이루어져 있습니다.
- name의 길이는 1 이상 20 이하입니다.

**입출력 예**

|name|return|
|---|---|
|"JEROEN"|56|
|"JAN"|23|

**아이디어**
- 딕셔너리
    - A : 0
    - B : 1
    - ...
    - N : 12
    - M : 13
    - ...
    - Z : 1
- A 있는지 확인
    - 있을 시
        - A 가 처음부터 몇개가 이어져 있는지
        - A 가 뒤에서부터 몇개가 이어져 있는지
        - 더 큰 수를 길이에서 빼기
    - 없을 시
        - 전체 길이-1 더하기


```python
def solution(name):
    alpha = {
        "A" : 0,
        "B" : 1,
        "C" : 2,
        "D" : 3,
        "E" : 4,
        "F" : 5,
        "G" : 6,
        "H" : 7,
        "I" : 8,
        "J" : 9,
        "K" : 10,
        "L" : 11,
        "M" : 12,
        "N" : 13,
        "O" : 12,
        "P" : 11,
        "Q" : 10,
        "R" : 9,
        "S" : 8,
        "T" : 7,
        "U" : 6,
        "V" : 5,
        "W" : 4,
        "X" : 3,
        "Y" : 2,
        "Z" : 1
    }
    answer = 0
    
    if "A" == name[1] or "A" == name[-1]:
        head = 0 # 뒤로 돌아갈 시 안 움직여도 될 횟수
        tail = 0 # 앞으로 갈 시 안 움직여도 될 횟수
        for i in range(1, 21):
            if "A" * i == name[1:i+1] :
                head = i 
            if "A" * i == name[-1 -1*i:]:
                tail = i
            if "A" * i != name[1:i+1] and "A"*i != name[-1 -1*i]:
                break
        answer += len(name)-max(head+1, tail+1)
    else :
        answer += len(name)-1
        
    for n in name:
        answer += alpha[n]
    return answer
```


```python
solution("JEROEN")
```




    56




```python
solution("AAAAABAAABAAA")
```




    10




```python
solution("BBBAAAB")
```




    10



### 구명보트

**문제 설명**
- 무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 **한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한**도 있습니다.

- 예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이 100kg이라면 2번째 사람과 4번째 사람은 같이 탈 수 있지만 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로 구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.

- 구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.

- 사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때, 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

**제한사항**
- 무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
- 각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
- 구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
- 구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.

**입출력 예**

|people|limit|return|
|---|---|---|
|[70, 50, 80, 50]|100|3|
|[70, 80, 50]|100|3|

**아이디어**
- 오름차순 정렬
    - 가장 큰 사람 과 가장 작은사람 값을 더해 limit 값과 비교
        - 넘을 시
            - 큰사람만 태움
        - 작을 시
            - 둘다 태움


```python

from collections import deque

def solution(people, limit):
    boat = 0
    people.sort()

    # 보트는 2명씩만 탈 수 있고 무게 제한도 있음.
    q = deque(people)
    cnt = 0
    while q:
        if len(q) >= 2:
            if q[0] + q[-1] <= limit: # 제일 많이 나가는 사람 + 제일 적은 사람 <= limit
                q.pop()
                q.popleft() # 두명 다 태움
                boat += 1
            elif q[0] + q[-1] > limit:
                q.pop() # 1명만 태움
                boat += 1
        else:
            if q[0] <= limit:
                q.pop()
                boat += 1
    return boat
```


```python
solution([70,50,80,50], 100)
```




    3



### 단속 카메라

**문제 설명**
- 고속도로를 이동하는 모든 차량이 고속도로를 이용하면서 단속용 카메라를 한 번은 만나도록 카메라를 설치하려고 합니다.

- 고속도로를 이동하는 차량의 경로 routes가 매개변수로 주어질 때, 모든 차량이 한 번은 단속용 카메라를 만나도록 하려면 최소 몇 대의 카메라를 설치해야 하는지를 return 하도록 solution 함수를 완성하세요.

**제한사항**

- 차량의 대수는 1대 이상 10,000대 이하입니다.
- routes에는 차량의 이동 경로가 포함되어 있으며 routes[i][0]에는 i번째 차량이 고속도로에 진입한 지점, routes[i][1]에는 i번째 차량이 고속도로에서 나간 지점이 적혀 있습니다.
- 차량의 진입/진출 지점에 카메라가 설치되어 있어도 카메라를 만난것으로 간주합니다.
- 차량의 진입 지점, 진출 지점은 -30,000 이상 30,000 이하입니다.

**입출력 예**

|routes|return|
|---|---|
|[[-20,-15], [-14,-5], [-18,-13], [-5,-3]]|2|

**아이디어**
- 진입 / 진출 지점 뽑아낸다.
    - 리스트 화 및 정렬
- while 반복문
    - 카메라 개수 1씩 증가
    - 지점 리스트 중 해당 개수만큼 카메라 설치한다고 가정 시
        - 모든 차량을 확인할 수 있는지 확인


```python
import itertools
import copy

def solution(routes):
    points = set()
    for r in routes:
        points.add(r[0])
        points.add(r[1])
    points = list(points)
    
    answer = 0
    chk = True
    
    for _ in range(len(points)):
        if not chk :
            break
        answer += 1
        for camera in list(itertools.combinations(points, answer)):
            test = copy.deepcopy(routes)
            for c in camera:
                delete = list()
                for t in test:
                    if t[0] <= c <= t[1]:
                        delete.append(t)
                if len(delete) != 0:
                    for d in delete:
                        test.remove(d)
            if len(test) == 0:
                chk = False
                break
                   
    return answer
```


```python
solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])
```




    2



**아이디어**
- 지출 지점 기준으로 정렬 후 카메라에 걸리는 지 확인하는 방법
    - 진출 지점에 카메라를 설치하는 이유는 다음 구간의 차량의 진입 시점과 비교하면 설치한 카메라에 걸리는 지 O(N)으로 확인이 가능하다


```python
def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1]) # routes를 차량이 나간 지점 (진출) 기준으로 정렬
    camera = -30001 # -30001부터 카메라 위치를 찾습니다.

    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]
    return answer
```


```python
solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])
```




    2


