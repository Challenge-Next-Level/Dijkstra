### 가장 먼 노드


**문제 설명**
- n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다. 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다. 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.

- 노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.

**제한사항**
- 노드의 개수 n은 2 이상 20,000 이하입니다.
- 간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
- vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.

**입출력 예**

|n|vertex|return|
|---|---|---|
|6|[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]|3|

**아이디어**
- 최단 경로 구하는 알고리즘 사용하여 가장 많은 노드들의 개수 세기
- 인접 리스트 활용
    - 노드가 각각 누구와 연결 되어 있는지 정의


```python
from collections import deque

def bfs(v, visited, adj):
    count = 0
    q = deque([[v, count]]) # [node, 1에서 부터 거리]
    while q:
        value = q.popleft() # 제일 첫번째 원소 반환
        v = value[0] # 첫번째 node
        count = value[1] # 1에서 부터 첫번째 노드 까지의 거리
        if visited[v] == -1: # 방문 안했을 시
            visited[v] = count # count = 1에서 부터 이전 노드 까지의 거리
            count += 1 
            for e in adj[v]:
                q.append([e, count])

def solution(n, edge):
    answer = 0
    
    adj = [[] for _ in range(n + 1)]
    for e in edge:
        src = e[0]
        dist = e[1]
        adj[src].append(dist)
        adj[dist].append(src)
    
    visited = [-1] * (n + 1)
    
    bfs(1, visited, adj)
    for value in visited:
        if value == max(visited):
            answer += 1
    return answer


solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
```




    3



### 순위

**문제 설명**
- n명의 권투선수가 권투 대회에 참여했고 각각 1번부터 n번까지 번호를 받았습니다. 권투 경기는 1대1 방식으로 진행이 되고, 만약 A 선수가 B 선수보다 실력이 좋다면 A 선수는 B 선수를 항상 이깁니다. 심판은 주어진 경기 결과를 가지고 선수들의 순위를 매기려 합니다. 하지만 몇몇 경기 결과를 분실하여 정확하게 순위를 매길 수 없습니다.

- 선수의 수 n, 경기 결과를 담은 2차원 배열 results가 매개변수로 주어질 때 정확하게 순위를 매길 수 있는 선수의 수를 return 하도록 solution 함수를 작성해주세요.

**제한사항**
- 선수의 수는 1명 이상 100명 이하입니다.
- 경기 결과는 1개 이상 4,500개 이하입니다.
- results 배열 각 행 [A, B]는 A 선수가 B 선수를 이겼다는 의미입니다.
- 모든 경기 결과에는 모순이 없습니다.

**입출력 예**

|n|results|return|
|---|---|---|
|5|[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]|2|

**아이디어**
- 승패표 그리기 (행 : 이김, 열 : 짐)


```python
def solution(n, results):
    answer = 0
    
    chart = [[0] * n for _ in range(n)]

    for w,l in results:
        chart[w-1][l-1] = 1 # win
        chart[l-1][w-1] = -1 # lose
    
    for i in range(n):
        wins = [opp for opp, rst in enumerate(chart[i]) if rst == 1] # 이긴 결과
        
        while wins:
            loser = wins.pop() # i번째 선수가 이긴 선수
            for opp, rst in enumerate(chart[loser]): # loser 가 이긴 선수는 i 번째 선수가 다 이길 수 있음
                if rst == 1 and chart[i][opp] == 0:
                    chart[i][opp], chart[opp][i] = 1, -1 # 승패 표 작성
                    wins.append(opp)
                    
    for c in chart:
        if c.count(0) == 1:
            answer += 1
            
    
    return answer

solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])
```

    [[0, 1, 0, 0, 0], [-1, 0, -1, -1, 1], [0, 1, 0, -1, 0], [0, 1, 1, 0, 0], [0, -1, 0, 0, 0]]





    2


