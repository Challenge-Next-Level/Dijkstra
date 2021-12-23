## 그래프 자료에서 데이터를 탐색하는 알고리즘

### DFS (Depth First Search)
- 그래프에서 특정 노드를 찾으려고 할때, 위에서 아래로 찾는 방식
- 기본 원칙
    - 데이터를 찾을떄 **"앞으로 찾아 가야할 노드"** 와 **"이미 방문한 노드"** 를 기준으로 데이터를 탐색합니다.
    - 특정 노드가 "앞으로 찾아 가야할 노드"라면 
        - 계속 검색을 하는 것이고, 
    - "이미 방문한 노드"면 
        - 무시하거나 따로 저장하면 됩니다. 



### DFS 구현 방법
- ### 스택/큐를 활용한 구현 방법
    - 리스트 활용 - pop 이용으로 인한 성능 하락


```python
def dfs(graph, start_node):
 
    ## 기본은 항상 두개의 리스트를 별도로 관리해주는 것
    need_visited, visited = list(), list()
 
    ## 시작 노드를 시정하기 
    need_visited.append(start_node)
    
    ## 만약 아직도 방문이 필요한 노드가 있다면,
    while need_visited:
 
        ## 그 중에서 가장 마지막 데이터를 추출 (스택 구조의 활용)
        node = need_visited.pop()
        
        ## 만약 그 노드가 방문한 목록에 없다면
        if node not in visited:
 
            ## 방문한 목록에 추가하기 
            visited.append(node)
 
            ## 그 노드에 연결된 노드를 
            need_visited.extend(graph[node])
            
    return visited
```

    - deque 활용


```python
def dfs2(graph, start_node):
    ## deque 패키지 불러오기
    from collections import deque
    visited = []
    need_visited = deque()
    
    ##시작 노드 설정해주기
    need_visited.append(start_node)
    
    ## 방문이 필요한 리스트가 아직 존재한다면
    while need_visited:
        ## 시작 노드를 지정하고
        node = need_visited.popleft()
 
        ##만약 방문한 리스트에 없다면
        if node not in visited:
 
            ## 방문 리스트에 노드를 추가
            visited.append(node)
            ## 인접 노드들을 방문 예정 리스트에 추가
            need_visited.extend(graph[node])
                
    return visited
```

- ### 재귀 함수를 통한 DFS 구현


```python
def dfs_recursive(graph, start, visited = []):
## 데이터를 추가하는 명령어 / 재귀가 이루어짐 
    visited.append(start)
 
    for node in graph[start]:
        if node not in visited:
            dfs_recursive(graph, node, visited)
    return visited
```

### BFS (Breadth First Search)
- 그래프에서 특정 노드를 찾으려고 할때, 수평방향으로 찾는 방식
- 기본 원칙
    - 1단계. 시작 노드를 방문했던 노드에 삽입한다. 

    - 2단계. 방문할 노드에 시작노드의 Child Node를 삽입한다. 
    
    - 3단계. Child노드를 중심으로 다시 1~2단계를 거쳐 탐색한다. 
    
### 구현
- **DFS 와의 차이점 : While문 다음에 어떤 자료를 우선적으로 추출**
    - DFS 같은 경우 리스트의 가장 끝에 있는 데이터를 기준으로 추출하지만, 
    - BFS는 리스트의 가장 처음에 있는 인자를 받습니다. 


```python
def bfs(graph, start_node):
    need_visited, visited = [], []
    need_visited.append(start_node)
    
    
    while need_visited:
        node = need_visited[0]
        del need_visited[0]
        
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    return visited
```
