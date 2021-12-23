### 1388, 바닥장식

**문제**
- 형택이는 건축가이다. 지금 막 형택이는 형택이의 남자 친구 기훈이의 집을 막 완성시켰다. 형택이는 기훈이 방의 바닥 장식을 디자인했고, 이제 몇 개의 나무 판자가 필요한지 궁금해졌다. 나무 판자는 크기 1의 너비를 가졌고, 양수의 길이를 가지고 있다. 기훈이 방은 직사각형 모양이고, 방 안에는 벽과 평행한 모양의 정사각형으로 나누어져 있다.

- 이제 ‘-’와 ‘|’로 이루어진 바닥 장식 모양이 주어진다. 만약 두 개의 ‘-’가 인접해 있고, 같은 행에 있다면, 두 개는 같은 나무 판자이고, 두 개의 ‘|’가 인접해 있고, 같은 열에 있다면, 두 개는 같은 나무 판자이다.

- 기훈이의 방 바닥을 장식하는데 필요한 나무 판자의 개수를 출력하는 프로그램을 작성하시오.

**입력**
- 첫째 줄에 방 바닥의 세로 크기N과 가로 크기 M이 주어진다. 둘째 줄부터 N개의 줄에 M개의 문자가 주어진다. 이것은 바닥 장식 모양이고, '-‘와 ’|‘로만 이루어져 있다. N과 M은 50 이하인 자연수이다.

**출력**
- 첫째 줄에 문제의 정답을 출력한다.

**아이디어**
- 두개씩 확인
- "-" 확인 - 너비 우선 검색
- "|" 확인 - 깊이 우선 검색


```python
N, M = map(int, input().split()) # N : 행 개수, M : 열 개수

board = list()

for _ in range(N):
    board.append(list(input()))
    
result = 0

# - 확인
for i in range(N):
    pre = "/"
    for j in range(M):
        if board[i][j] == "-":
            if board[i][j] != pre:
                result += 1
        pre = board[i][j]
        
# | 확인
for j in range(M):
    pre = "/"
    for i in range(N):
        if board[i][j] == "|":
            if board[i][j] != pre:
                result += 1
        pre = board[i][j]
        
print(result)
```

    4 4
    ----
    ----
    ----
    ----
    4


### 14716, 현수막

**문제**
- ANT가 처음 알고리즘 대회를 개최하게 되면서 현수막을 내걸었다.

- 저번 학기 영상처리 수업을 듣고 배웠던 지식을 최대한 응용 해보고 싶은 혁진이는 이 현수막에서 글자가 몇 개인지 알아보는 프로그램을 만들려 한다.

- 혁진이는 우선 현수막에서 글자인 부분은 1, 글자가 아닌 부분은 0으로 바꾸는 필터를 적용하여 값을 만드는데 성공했다.

- 그런데 혁진이는 이 값을 바탕으로 글자인 부분 1이 상, 하, 좌, 우, 대각선으로 인접하여 서로 연결되어 있다면 한 개의 글자라고 생각만 하였다.

- 혁진이가 필터를 적용하여 만든 값이 입력으로 주어졌을 때, 혁진이의 생각대로 프로그램을 구현하면 글자의 개수가 몇 개인지 출력하여라.

**입력**
- 첫 번째 줄에는 현수막의 크기인 M와 N가 주어진다. (1 ≤ M, N ≤ 250)

- 두 번째 줄부터 M+1 번째 줄까지 현수막의 정보가 1과 0으로 주어지며, 1과 0을 제외한 입력은 주어지지 않는다.

**출력**
- 혁진이의 생각대로 프로그램을 구현했을 때, 현수막에서 글자의 개수가 몇 개인지 출력하여라.

**아이디어**
- 현수막의 부분을 탐색하다가, 방문하지 않은 1를 발견하면, 글자의 수를 하나 증가시키고 BFS를 실시한다.


```python
import sys
from collections import deque

r, c = map(int, sys.stdin.readline().rstrip().split())
d = [[-1,0], [1,0], [0,1], [0,-1], [-1,-1], [-1,1], [1,-1], [1,1]] # 이동 방향
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(r)] # 입력 현수막
visited = [[False for _ in range(c)] for _ in range(r)] # 현수막 크기의 False 배열

def isin(y,x): # 현수막 안에 있으면 return True
    if -1<y<r:
        if -1<x<c: 
            return True
    return False

def bfs(sy, sx):
    q = deque() # 한개의 글자를 위한 deque
    q.append([sy, sx])
    visited[sy][sx] = True # 방문 체크

    while q: #글자가 끝날 때 까지
        y, x = q.popleft()

        for i in range(8): # 8방향 각각 확인
            ny = y + d[i][0]
            nx = x + d[i][1]

            if isin(ny, nx):
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    if arr[ny][nx] == 1: # 해당 위치가 글자에 포함되어있을 시 추가 
                        q.append([ny,nx])

cnt = 0

for i in range(r):
    for j in range(c):
        if not visited[i][j] and arr[i][j] == 1: # 방문하지 않았고, 해당 숫자가 1 일 때,
            cnt += 1
            bfs(i, j)

print(cnt)

```
