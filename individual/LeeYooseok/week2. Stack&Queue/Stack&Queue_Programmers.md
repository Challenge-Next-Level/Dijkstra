### 기능 개발

**문제 설명**
- 프로그래머스 팀에서는 기능 개선 작업을 수행 중입니다. 각 기능은 진도가 100%일 때 서비스에 반영할 수 있습니다.

- 또, 각 기능의 개발속도는 모두 다르기 때문에 뒤에 있는 기능이 앞에 있는 기능보다 먼저 개발될 수 있고, 이때 뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포됩니다.

- 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록 solution 함수를 완성하세요.

**제한 사항**
- 작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
- 작업 진도는 100 미만의 자연수입니다.
- 작업 속도는 100 이하의 자연수입니다.
- 배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.

**입출력 예**

|progresses|speeds|return|
|---|---|---|
|[93, 30, 55]|[1, 30, 5]|[2, 1]|
|[95, 90, 99, 99, 80, 99]|[1, 1, 1, 1, 1, 1]|[1, 3, 2]|

**아이디어**
- 100 에서 progress 리스트의 각 값들 을 빼서 남은 진행 율 리스트 생성
- 남은 진행 율 리스트 를 speeds 의 각 값들로 나누어 남은 일수 리스트 생성
- 남은 일수 리스트 앞부터 확인하여 이전값이 현재 값보다 크면 pop(0) 한다. 
    - pop(0)의 횟수를 세어 result 리스트에 최종 추가
- 남은 일 수 계산시 // 연산 시 버림을 하게 되지만 해당 문제의 경우 올림을 해 주어야 한다.
    - math 모듈의 ceil 활용


```python
import math

def solution(progresses, speeds):
    residuals = list()
    for progress in progresses:
        residuals.append(100-progress)
    
    days = list()
    for i in range(len(residuals)):
        days.append(math.ceil(residuals[i] / speeds[i]))
        
    result = list()
    while len(days) != 0:
        chk = days.pop(0)
        cnt = 1
        if(len(days) == 0):
            result.append(cnt)
            break
        while chk >= days[0]:
            cnt += 1
            days.pop(0)
            if(len(days) == 0):
                break
        result.append(cnt)

    return result
```


```python
solution([93,30,55],[1,30,5])
```




    [2, 1]



### 프린터

**문제 설명**
- 일반적인 프린터는 인쇄 요청이 들어온 순서대로 인쇄합니다. 그렇기 때문에 중요한 문서가 나중에 인쇄될 수 있습니다. 이런 문제를 보완하기 위해 중요도가 높은 문서를 먼저 인쇄하는 프린터를 개발했습니다. 이 새롭게 개발한 프린터는 아래와 같은 방식으로 인쇄 작업을 수행합니다.

1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
3. 그렇지 않으면 J를 인쇄합니다.

- 예를 들어, 4개의 문서(A, B, C, D)가 순서대로 인쇄 대기목록에 있고 중요도가 2 1 3 2 라면 C D A B 순으로 인쇄하게 됩니다.

- 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 알고 싶습니다. 위의 예에서 C는 1번째로, A는 3번째로 인쇄됩니다.

- 현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities와 내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 location이 매개변수로 주어질 때, 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return 하도록 solution 함수를 작성해주세요.

**제한사항**
- 현재 대기목록에는 1개 이상 100개 이하의 문서가 있습니다.
- 인쇄 작업의 중요도는 1~9로 표현하며 숫자가 클수록 중요하다는 뜻입니다.
- location은 0 이상 (현재 대기목록에 있는 작업 수 - 1) 이하의 값을 가지며 대기목록의 가장 앞에 있으면 0, 두 번째에 있으면 1로 표현합니다.

**입출력 예**

|priorities|location|return|
|---|---|---|
|[2, 1, 3, 2]|2|1|
|[1, 1, 9, 1, 1, 1]|0|5|

**아이디어**
- 큐 자료구조를 활용하여 가장 앞의 문서 를 꺼낸다. - pop(0)
- 우선순위에 남아있는 목록 중 꺼내어진 문서보다 우선순위가 높은 문서가 있는지 확인
    - 있을 시
        - append() 하여 우선순위 목록의 제일 마지막에 추가한다.
    - 없을 시
        - print 한다.
- 내 문서의 순서 확인하는 방법
    - answer 변수 생성
        - 내 문서의 순서 체크


```python
def solution(priorities, location):
    answer = 0
    while True:
        chk = priorities.pop(0)
        
        # 큐에 하나만 남았을때 경우
        if len(priorities) == 0:
            answer += 1
            break
        
        # 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
        if chk < sorted(priorities, reverse = True)[0]:
            priorities.append(chk)
        # 순서가 한번 밀려나고, 만약 내 위치가 0 이면 출력된다.
        else :
            answer += 1
            if location == 0 :
                break
            
        # 내 문서의 위치를 설정한다.
        if location != 0:
            location -= 1
        else :
            location = len(priorities) - 1
    return answer
```


```python
solution([1,1,9,1,1,1],0)
```




    5



### 다리를 지나는 트럭
**문제 설명**
- 트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를 견딜 수 있습니다. 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.

- 예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.

|경과 시간|다리를 지난 트럭|다리를 건너는 트럭|대기 트럭|
|---|---|---|---|
|0|[]|[]|[7,4,5,6]|
|1~2|[]|[7]|[4,5,6]|
|3|[7]|[4]|[5,6]|
|4|[7]|[4,5]|[6]|
|5|[7,4]|[5]|[6]|
|6~7|[7,4,5]||[6]|[]|
|8|[7,4,5,6]|[]|[]|

- 따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.

- solution 함수의 매개변수로 다리에 올라갈 수 있는 트럭 수 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭 별 무게 truck_weights가 주어집니다. 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

**제한 조건**
- bridge_length는 1 이상 10,000 이하입니다.
- weight는 1 이상 10,000 이하입니다.
- truck_weights의 길이는 1 이상 10,000 이하입니다.
- 모든 트럭의 무게는 1 이상 weight 이하입니다.

**입출력 예**

|bridge_length|weight|truck_weights|return|
|---|---|---|---|
|2|10|[7,4,5,6]|8|
|100|100|[10]|101|
|100|100|[10,10,10,10,10,10,10,10,10,10]|110|

- 다리를 지나는 시간은 - bridge_length 이다.
- 다리에 한번에 올라갈 수 있는 차의 무게가 weight 이다.

**아이디어**
- truck_weights 리스트를 큐 자료구조로 활용한다.
    - 다리를 건너는 트럭 딕셔너리 변수를 생성한다. (큐 자료구조로 활용)
    - 현재 지나가는 트럭과 대기 중인 트럭들이 없으면 
        - 반복문 break
        
    - 현재 지나가는 트럭의 입장 시각 + 다리 길이 가 현재 시각과 같을 시
        - 해당 트럭을 지나가는 트럭 딕셔너리에서 제거한다.
        
    - 현재 지나가고 있는 트럭들의 무게를 잰다.
    
    - 현재 지나가고 있는 트럭들의 무게 + 대기중인 트럭중 맨 앞의 트럭 무게 <= 다리가 버틸 수 있는 무게
        - truck_weights.pop(0) 로 맨 앞의 트럭을 pop 한다.
        - 다리에 올라간 시각을 key 로 pop 한 데이터를 value 로 딕셔너리에 추가한다.
    
    - 현재 시각 리턴


```python
def solution(bridge_length, weight, truck_weights):
    answer = 0
    on_trucks = dict()
    while True:
        answer += 1
        
        if len(truck_weights) == 0 and len(on_trucks) == 0:
            break
            
        if len(on_trucks) != 0 :
            if int(list(on_trucks.keys())[0]) + bridge_length == answer:
                del on_trucks[list(on_trucks.keys())[0]]
            
        on_weight = sum(on_trucks.values())
            
        if len(truck_weights) != 0:
            if  on_weight + truck_weights[0] <= weight:
                on_trucks[str(answer)] = truck_weights.pop(0)
    return answer - 1
```


```python
solution(2,10,[7,4,5,6])
```




    8



### 주식 가격

**문제 설명**
- 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

**제한사항**
- prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
- prices의 길이는 2 이상 100,000 이하입니다.

**입출력 예**

|prices|return|
|---|---|
|[1, 2, 3, 2, 3]|[4, 3, 1, 1, 0]|

**아이디어**
- 반복문 (price)
    - 반복문 (prices)
        - price 가 prices 값들보다 크다면
            - break
    - answer 리스트에 걸린 시간 추가


```python
def solution(prices):
    answer = []
    for i in range(len(prices)):
        chk = 0
        for j in range(i+1,len(prices)):
            chk += 1
            if prices[i] > prices[j]:
                break
        answer.append(chk)
    return answer
```


```python
solution([1,2,3,2,3])
```




    [4, 3, 1, 1, 0]


