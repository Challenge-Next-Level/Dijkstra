### 더 맴게

**문제 설명**
- 매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

- 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
- Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
- Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

**제한 사항**
- scoville의 길이는 2 이상 1,000,000 이하입니다.
- K는 0 이상 1,000,000,000 이하입니다.
- scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
- 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.

**입출력 예**

|scoville|K|return|
|---|---|---|
|[1, 2, 3, 9, 10, 12]|7|2|

**아이디어**
- heapq 활용하여 scoville 을 heapq 를 활용하여 heap 자료구조로 사용
- heappop 을 활용하여 가장 작은 두 수 를 확인


```python
import heapq

def solution(scoville, K):
    
    answer = 0
    
    heapq.heapify(scoville)
    chk = True
    while chk:
        if len(scoville) == 1:
            if scoville[0] >= K:
                break
            else :
                answer = -1
                break
        
    
        min_1 = heapq.heappop(scoville)
        min_2 = heapq.heappop(scoville)
        
        if min_1 >= K and min_2 >= K :
            chk = False
            break
        
        new = min_1 + 2*min_2
        
        heapq.heappush(scoville, new)
        answer += 1
    return answer
```


```python
solution([10,12,3,9,1,2], 7)
```

    [1, 9, 2, 10, 12, 3]
    




    2



### 디스크 컨트롤러

**문제 설명**
- 하드디스크는 한 번에 하나의 작업만 수행할 수 있습니다. 디스크 컨트롤러를 구현하는 방법은 여러 가지가 있습니다. 가장 일반적인 방법은 요청이 들어온 순서대로 처리하는 것입니다.

- 각 작업에 대해 [작업이 요청되는 시점, 작업의 소요시간]을 담은 2차원 배열 jobs가 매개변수로 주어질 때, 작업의 요청부터 종료까지 걸린 시간의 평균을 가장 줄이는 방법으로 처리하면 평균이 얼마가 되는지 return 하도록 solution 함수를 작성해주세요. (단, 소수점 이하의 수는 버립니다)

**제한 사항**
- jobs의 길이는 1 이상 500 이하입니다.
- jobs의 각 행은 하나의 작업에 대한 [작업이 요청되는 시점, 작업의 소요시간] 입니다.
- 각 작업에 대해 작업이 요청되는 시간은 0 이상 1,000 이하입니다.
- 각 작업에 대해 작업의 소요시간은 1 이상 1,000 이하입니다.
- 하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다.

**입출력 예**

|jobs|return|
|---|---|
|[[0, 3], [1, 9], [2, 6]]|9|

**아이디어**
- 이전 작업 종료시 요청이 들어온 작업들 중 가장 소요시간이 작은 작업 시작
    - 시간 반복
        - 시작 시간이 됬을 시 heap에 추가
        - 종료 시 heap 에서 heappop 하여 가장 소요시간이 작은 작업 시작


```python
import heapq

def solution(jobs):
    answer = 0
    time = 0
    num_jobs = len(jobs)
    req_task = []
    doing_task = []
    while jobs or req_task or doing_task:
        # 작업 요청 시각 == 현재 시각
        if jobs:
            if time == jobs[0][0] :
                job = jobs.pop(0)
                new_job = [job[1], job[0]]
                heapq.heappush(req_task, new_job)
        
        # 현재 작업중인 작업이 있을 시 작업이 끝났는지 확인
        if doing_task:
            if doing_task[0] == time:
                doing_task = []
            
        # 현재 작업중인 작업이 없을 시 작업 시작
        if not doing_task and req_task:
            job = heapq.heappop(req_task)
            finish_task = time + job[0]
            doing_task = [finish_task] # 종료 시각
            answer += (finish_task - job[1])
            
        time += 1
    answer = answer // num_jobs
    return answer
```


```python
import heapq

def solution(jobs):
    time = 0
    num_jobs = len(jobs)
    heapq.heapify(jobs) # heap 정렬
    req_task = []
    answer = 0
    while jobs or req_task:
        # 작업 요청
        while jobs and jobs[0][0] <= time:
            job = heapq.heappop(jobs)
            new_job = [job[1], job[0]] # 수행시간, 요청 시각
            heapq.heappush(req_task, new_job)
            
        # req_task 가 비어있는지 확인
        if req_task:
            # 작업 수행
            do_task = heapq.heappop(req_task)
            time += do_task[0]
            answer += time - do_task[1]
        else:
            time += 1
        
    answer = answer // num_jobs
    
    return answer
```

### 이중우선순위 큐

**문제 설명**
- 이중 우선순위 큐는 다음 연산을 할 수 있는 자료구조를 말합니다.

|명령어|수신 탑(높이)|
|---|---|
|I 숫자|큐에 주어진 숫자를 삽입합니다.|
|D 1|큐에서 최댓값을 삭제합니다.|
|D -1|큐에서 최솟값을 삭제합니다.|

- 이중 우선순위 큐가 할 연산 operations가 매개변수로 주어질 때, 모든 연산을 처리한 후 큐가 비어있으면 [0,0] 비어있지 않으면 [최댓값, 최솟값]을 return 하도록 solution 함수를 구현해주세요.

**제한사항**
- operations는 길이가 1 이상 1,000,000 이하인 문자열 배열입니다.
- operations의 원소는 큐가 수행할 연산을 나타냅니다.
- 원소는 “명령어 데이터” 형식으로 주어집니다.- 최댓값/최솟값을 삭제하는 연산에서 최댓값/최솟값이 둘 이상인 경우, 하나만 삭제합니다.
- 빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 해당 연산은 무시합니다.

**입출력 예**

|operations|return|
|---|---|
|["I 16","D 1"]|[0,0]|
|["I 7","I 5","I -5","D -1"]|[7,5]|

**아이디어**
- answer - heap 으로 활용
- operations 반복문
    - 해당 연산 수행


```python
import heapq

def solution(operations):
    answer = []
    for oper in operations:
        type_oper, num_oper = oper.split(" ")
        num_oper = int(num_oper)
        if type_oper == "I":
            heapq.heappush(answer, num_oper)
        else:
            if num_oper == 1 and answer:
                answer.remove(max(answer))
                heapq.heapify(answer)
            elif num_oper == -1 and answer:
                heapq.heappop(answer)
                
    if answer:
        return [max(answer), min(answer)]
    else:
        return [0,0]
```


```python
solution(["I 16","D 1"])
```

    []
    




    [0, 0]




```python
solution(["I 7","I 5","I -5","D -1"])
```

    [5, 7]
    




    [7, 5]




```python
solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])
```




    [0, 0]


