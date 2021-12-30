### 등굣길

**문제 설명**
- 계속되는 폭우로 일부 지역이 물에 잠겼습니다. 물에 잠기지 않은 지역을 통해 학교를 가려고 합니다. 집에서 학교까지 가는 길은 m x n 크기의 격자모양으로 나타낼 수 있습니다.

- 가장 왼쪽 위, 즉 집이 있는 곳의 좌표는 (1, 1)로 나타내고 가장 오른쪽 아래, 즉 학교가 있는 곳의 좌표는 (m, n)으로 나타냅니다.

- 격자의 크기 m, n과 물이 잠긴 지역의 좌표를 담은 2차원 배열 puddles이 매개변수로 주어집니다. 오른쪽과 아래쪽으로만 움직여 집에서 학교까지 갈 수 있는 최단경로의 개수를 1,000,000,007로 나눈 나머지를 return 하도록 solution 함수를 작성해주세요.

**제한사항**
- 격자의 크기 m, n은 1 이상 100 이하인 자연수입니다.
    - m과 n이 모두 1인 경우는 입력으로 주어지지 않습니다.
- 물에 잠긴 지역은 0개 이상 10개 이하입니다.
- 집과 학교가 물에 잠긴 경우는 입력으로 주어지지 않습니다.


**입출력 예**

|m|n|puddles|return|
|---|---|---|---|
|4|3|[[2, 2]]|4|

**아이디어**
- 오른쪽 or 아래로만 이동
- 길이 갈라질 수 있으면, 경우의수 갈래길 만큼 증가
- 점화식
    - dp[i][j] = dp[i-1][j] + dp[i][j-1]
    - 새로 값을 넣을 칸 = 바로 위 칸 까지의 경로수 + 바로 왼쪽 칸 까지의 경로수


```python
def solution(m, n, puddles):
    puddles = [[q,p] for [p,q] in puddles] # puddles 좌표가 거꾸로 주어짐
    
    dp = [[0] * (m+1) for i in range(n+1)] # dp 초기화
    dp[1][1] = 1 # 집의 위치 (시작 위치)
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if i==1 and j==1: continue
            if [i,j] in puddles : # 웅더이 위치의 경우 값을 0
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
    return dp[n][m]
```


```python
solution(4,3,[[2,2]])
```




    4

