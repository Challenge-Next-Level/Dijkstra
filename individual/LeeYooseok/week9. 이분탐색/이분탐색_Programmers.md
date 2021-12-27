### 입국 심사

**문제 설명**
- n명이 입국심사를 위해 줄을 서서 기다리고 있습니다. 각 입국심사대에 있는 심사관마다 심사하는데 걸리는 시간은 다릅니다.

- 처음에 모든 심사대는 비어있습니다. 한 심사대에서는 동시에 한 명만 심사를 할 수 있습니다. 가장 앞에 서 있는 사람은 비어 있는 심사대로 가서 심사를 받을 수 있습니다. 하지만 더 빨리 끝나는 심사대가 있으면 기다렸다가 그곳으로 가서 심사를 받을 수도 있습니다.

- 모든 사람이 심사를 받는데 걸리는 시간을 최소로 하고 싶습니다.

- 입국심사를 기다리는 사람 수 n, 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times가 매개변수로 주어질 때, 모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return 하도록 solution 함수를 작성해주세요.

**제한사항**
- 입국심사를 기다리는 사람은 1명 이상 1,000,000,000명 이하입니다.
- 각 심사관이 한 명을 심사하는데 걸리는 시간은 1분 이상 1,000,000,000분 이하입니다.
- 심사관은 1명 이상 100,000명 이하입니다.

**입출력 예**

|n|times|return|
|---|---|---|
|6|[7, 10]|28|

**아이디어**
- 0 ~ 최대 시간 (max(times) * n) 시간 배열을 이분 탐색
- 중간 값이 가능 하다면, 
    - result = mid
    - right = mid - 1
- 중간 값이 불가능 하다면
    - left = mid + 1


```python
n = 6
times = [7,10]

def solution(n, times):
    answer = 0
    left = 0
    right = max(times)*n
    
    while left <= right:
        mid = (left+right)//2
        people = 0
        for t in times:
            people += (mid//t)
        
        if people >= n:
            answer = mid
            right = mid-1
        else:
            left = mid+1
    
    return answer
    
solution(n, times)
```

    28


### 징검 다리

**문제 설명**
- 출발지점부터 distance만큼 떨어진 곳에 도착지점이 있습니다. 그리고 그사이에는 바위들이 놓여있습니다. 바위 중 몇 개를 제거하려고 합니다.
- 예를 들어, 도착지점이 25만큼 떨어져 있고, 바위가 [2, 14, 11, 21, 17] 지점에 놓여있을 때 바위 2개를 제거하면 출발지점, 도착지점, 바위 간의 거리가 아래와 같습니다.

|제거한 바위의 위치|각 바위 사이의 거리|거리의 최솟값|
|---|---|---|
|[21, 17]|[2, 9, 3, 11]|2|
|[2, 21]|[11, 3, 3, 8]|3|
|[2, 11]|[14, 3, 4, 4]|3|
|[11, 21]|[2, 12, 3, 8]|2|
|[2, 14]|[11, 6, 4, 4]|4|

- 위에서 구한 거리의 최솟값 중에 가장 큰 값은 4입니다.

- 출발지점부터 도착지점까지의 거리 distance, 바위들이 있는 위치를 담은 배열 rocks, 제거할 바위의 수 n이 매개변수로 주어질 때, 바위를 n개 제거한 뒤 각 지점 사이의 거리의 최솟값 중에 가장 큰 값을 return 하도록 solution 함수를 작성해주세요.

**제한사항**
- 도착지점까지의 거리 distance는 1 이상 1,000,000,000 이하입니다.
- 바위는 1개 이상 50,000개 이하가 있습니다.
- n 은 1 이상 바위의 개수 이하입니다.

**입출력 예**

|distance|rocks|n|return|
|---|---|---|---|
|25|[2, 14, 11, 21, 17]|2|4|

**아이디어**



```python
distance = 25
rocks = [2,14,11,21,17]
n = 2

def solution(distance, rocks, n):
    rocks.sort()
    rocks.insert(0, 0)
    rocks.append(distance)
    
    distances = list()
    for r in range(1, len(rocks)):
        distances.append(rocks[r]-rocks[r-1])
    for _ in range(n):
        i = distances.index(min(distances[:-1]))
        n = distances[i] + distances[i+1]
        del distances[i]
        del distances[i]
        distances.insert(i, n)
    print(distances)
        
    return min(distances)
    
solution(distance, rocks, n)
```

    [11, 6, 7, 1]





    1


