### 1010, 다리놓기

**문제**
- 재원이는 한 도시의 시장이 되었다. 이 도시에는 도시를 동쪽과 서쪽으로 나누는 큰 일직선 모양의 강이 흐르고 있다. 하지만 재원이는 다리가 없어서 시민들이 강을 건너는데 큰 불편을 겪고 있음을 알고 다리를 짓기로 결심하였다. 강 주변에서 다리를 짓기에 적합한 곳을 사이트라고 한다. 재원이는 강 주변을 면밀히 조사해 본 결과 강의 서쪽에는 N개의 사이트가 있고 동쪽에는 M개의 사이트가 있다는 것을 알았다. (N ≤ M)

- 재원이는 서쪽의 사이트와 동쪽의 사이트를 다리로 연결하려고 한다. (이때 한 사이트에는 최대 한 개의 다리만 연결될 수 있다.) 재원이는 다리를 최대한 많이 지으려고 하기 때문에 서쪽의 사이트 개수만큼 (N개) 다리를 지으려고 한다. 다리끼리는 서로 겹쳐질 수 없다고 할 때 다리를 지을 수 있는 경우의 수를 구하는 프로그램을 작성하라.

**입력**
- 입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다. 그 다음 줄부터 각각의 테스트케이스에 대해 강의 서쪽과 동쪽에 있는 사이트의 개수 정수 N, M (0 < N ≤ M < 30)이 주어진다.

**출력**
- 각 테스트 케이스에 대해 주어진 조건하에 다리를 지을 수 있는 경우의 수를 출력한다.

**아이디어**
- 중복 없이 순열


```python
import math


def solution(n,m):
    result = math.factorial(m) / (math.factorial(m-n) * math.factorial(n))
    print(int(result))
    

n = int(input())
for _ in range(n):
    nums = list(map(int, input().split()))
    solution(nums[0],nums[1])
```

    3
    2 2
    1
    1 5
    5
    13 29
    67863915


### 11727, 2xn 타일링 2

**문제**
- 2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

**입력**
- 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

**출력**
- 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

**아이디어**
- 2 x 1
    - 1
- 2 x 2
    - 3
- 2 x 3
    - 5
- 2 x 4
    - 11
- 2 x n
    - s[n-1] + s[n-2] * 2


```python
s = [0, 1, 3]

n = int(input())

for i in range(3, n+1):
    s.append(s[i - 1] + (s[i - 1] * 2))

print(s[n] % 10007)
```

    4
    11


### 2293, 동전 1

**문제**
- n가지 종류의 동전이 있다. 각각의 동전이 나타내는 가치는 다르다. 이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그 경우의 수를 구하시오. 각각의 동전은 몇 개라도 사용할 수 있다.

- 사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.

**입력**
- 첫째 줄에 n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000) 다음 n개의 줄에는 각각의 동전의 가치가 주어진다. 동전의 가치는 100,000보다 작거나 같은 자연수이다.

**출력**
- 첫째 줄에 경우의 수를 출력한다. 경우의 수는 231보다 작다.

**아이디어**
- 1원으로 k 원 만드는 경우의 수
    - 1
- 1,2 원으로 k 원 만드는 경우의 수
    - 1
    - if k-2 >=0
        - dp[k-2]
- 1,2,5 원으로 k 원 만드는 경우의 수
    - 1 원으로 k 원 만드는 경우의 수
    - 1,2 원으로 k 원 만드는 경우의 수
    - if k-5 >=0
        - dp[k-5]


```python
n, k = map(int, input().split())

coins = list()
for _ in range(n):
    coins.append(int(input()))

dp = [0] * (k+1)
dp[0] = 1
    
for c in coins:
    for j in range(c, k+1):
        if j-c >= 0:
            dp[j] += dp[j-c]
            
print(dp[k])
```

    3 10
    1
    2
    5
    10

