## 수열 정렬

### 문제 설명
- 입력
    - 첫째 줄: 정수 1개(N) -> 배열 A의 크기 (N<=50)
    - 둘째 줄: 배열 A의 원소가 0번부터 차례대로 주어짐
- 출력
    - 비내림차순으로 만드는 수열 P를 출력

### 조건
- 비내림차순이란, 각각의 원소가 바로 앞에 있는 원소보다 크거나 같을 경우를 말한다. 
- 만약 그러한 수열이 여러개라면 사전순으로 앞서는 것을 출력한다.

### 아이디어
- A_asc : 배열 A를 오름차순으로 정렬한 배열
- index : A의 원소 하나가 A_asc에서 몇 번째 원소인지를 저장해두는 ㄹ리스트
- A 배열에 같은 수의 원소가 들어가 있을 수 있기 때문에
    - 먼저 빼낸 것은 -100으로 다시 사용안되게 재지정해줌

```
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A_asc = sorted(A)

index = []

for a in A:
    index.append(A_asc.index(a))
    A_asc[A_asc.index(a)] = -100
    
    
for i in index:
    print(i, end = " ")

```
