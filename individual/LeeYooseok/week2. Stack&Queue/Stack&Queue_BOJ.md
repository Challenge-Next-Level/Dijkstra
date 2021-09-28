### 21775, 가희와 자원 놀이

**문제**
- 가희와 친구들은 자원 놀이를 하고 있습니다.

- 이 놀이는 T개의 연산 카드와, 1 부터 2×109 이하의 자연수가 한 장에 하나씩 순서대로 적혀져 있는 2×109개의 자원 카드를 이용합니다.

- 자원 놀이에서 사용하는 연산 카드의 종류는 3가지입니다.
    - next
        - 아무 일도 일어나지 않고 이 카드를 버립니다.
    - acquire n
        - 자연수 n이 적혀진 자원 카드를 획득하려고 시도합니다.
        - 만약 자연수 n이 적혀진 자원 카드가 공용 공간에 있다면 자신의 공간으로 자원 카드를 가져온 다음에, acquire n 카드를 버립니다.
        - 그렇지 않고, 자원 카드가 다른 누군가의 공간에 있는 경우에는 이 카드를 버리지 않고 돌아오는 자신의 다음 차례에 재사용합니다.
    - release n
        - 자연수 n이 적혀진 자원 카드를 공용 공간에 반납하고, 이 카드를 버립니다.


- 자원 게임의 초기 상태
    - 모든 유저들은 자원 카드와 연산 카드를 들고 있지 않습니다.

- 게임의 규칙은 아래와 같습니다.
    - 처음에 모든 자원 카드들과 연산 카드들은 공용 공간에 놓여져 있습니다.
    - 각 턴을 수행하는 사람은 1명입니다.
    - 자신의 턴이 돌아오면 다음의 행동을 수행합니다.
        - 연산 카드를 들고 있지 않은 경우
            - 더미의 맨 위에 있는 연산 카드를 뽑고, 해당 카드에 있는 연산을 즉시 수행합니다.
        - 연산 카드를 들고 있는 경우
            - 들고 있는 연산 카드에 있는 연산을 즉시 수행합니다.
    - 처음 연산 카드 더미에 있던 연산 카드가 T개 주어지고, T 턴동안 각 턴을 수행한 사람의 번호가 주어집니다.

    - T 턴동안 수행된 연산 카드의 id를 알려주세요. 처음 더미에 있는 연산 카드의 갯수와 턴 수는 같습니다.

**입력**
- 첫 번째 줄에 자원 놀이에 참가하는 사람 수 N과 턴 수 T가 주어집니다.

- 두 번째 줄에 각 턴을 수행한 사람 번호가 T개 주어집니다.

- 세 번째 줄 부터 2+T번째 줄까지, 더미의 맨 위에 있는 카드부터, 더미에 있는 연산 카드의 id와 연산 카드에 적혀져 있는 연산이 공백으로 구분되어 주어집니다.

**출력**
- T턴에 걸쳐서, 각 턴에 수행된 연산 카드의 id를 한 줄에 하나씩 출력해 주세요.

**아이디어**
- 소유중인 연산 카드 딕셔너리 생성
    - key : 소유자 Id
    - value : {
        - key : card_num
        - value : 자원 수
    }
    
- 소유중인 자원 카드 리스트 생성
    - set()

- next
    - 연산 카드 소유 불가
    - 아무 일도 일어나지 않고 카드를 버립니다.
- acquire n
    - 연산 카드 소유 가능
    - 자연수 n이 적혀진 자원 카드를 획득하려고 시도합니다.
    - 소유중인 자원 카드 list 에 해당 수 가 있는지 확인
        - 있을 시
            - 다음 턴에 해당 연산 카드 수행
            - 해당 턴의 사용자 id -> 소유중인 연산 카드 딕셔너리[id][card_num] = num
        - 없을 시
            - 소유중인 자원 카드 리스트에 num 추가
- release n
    - 연산 카드 소유 불가
    - 자연수 n 이 적혀진 자원 카드를 공용 공간에 반납 후, 해당 연산 카드 버림
    - 획득하지 않은 자원 카드를 release 하는 경우는 주어지지 않습니다.
        - 소유중인 자원 카드 리스트에서 해당 값 제거


```python
import sys

# 참여자 id, 턴 수 입력
N, T = map(int, input().split())

# 각 턴을 수행한 참여자의 id 입력
turns = [int(x) for x in input().split()]

# 소유중인 자원 카드 딕셔너리 생성
cards = dict()

# cards 딕셔너리 자료구조 초기화
for i in range(1, N+1):
    cards[i] = dict()

have = set()

i = 0
cardinput = 0

while True:
    if(i >= len(turns)):
        for _ in range(len(turns) - cardinput):
            input()
        break
    else:      
        Id = turns[i]
        # 자신의 턴인 참여자의 딕셔너리에 카드 있을 시 acquire 카드 수행 아닐 시 계속 수행
        if(cards[Id]) :
            # cards[Id] - 숫자 : 카드 넘버 쌍
            num = list(cards[Id].values())[0]
            card_num = list(cards[Id].keys())[0]
            sys.stdout.write(card_num + '\n')
            # 해당 자원 카드가 누군가가 소유 중인지 확인
            if (num not in have):
                have.add(num)
                # 소유중이던 acquire 카드 버리기
                del cards[Id][card_num]
        else :
            card = input()
            #card = sys.stdin.readline()
            cardinput += 1
            card_num = card.split()[0]
            sys.stdout.write(card_num + '\n')
            if("release" in card):
                have.remove(num)
            elif("acquire" in card):
                num = card.split()[2]
                # 해당 자원 카드가 누군가가 소유 중인지 확인
                if( num in have):
                    cards[Id][card_num] = num
                else :
                    have.add(num)

    i += 1
```

    2 10
    1 1 2 2 1 1 2 2 2 2 
    1 next
    1
    2 acquire 1
    2
    3 acquire 1
    3
    3
    4 next
    4
    5 release 1
    5
    3
    6 release 1
    6
    7 next
    7
    8 acquire 1
    8
    

### 5464, 주차장

**문제**
- 시내 주차장은 1부터 N까지 번호가 매겨진 N개의 주차 공간을 가지고 있다. 이 주차장은 매일 아침 모든 주차 공간이 비어 있는 상태에서 영업을 시작하며, 하룻동안 다음과 같은 방식으로 운영된다. 차가 주차장에 도착하면, 주차장 관리인이 비어있는 주차 공간이 있는지를 검사한다. 만일 비어있는 공간이 없으면, 차량을 빈 공간이 생길 때까지 입구에서 기다리게 한다. 만일 빈 주차 공간이 하나만 있거나 또는 빈 주차 공간이 없다가 한 대의 차량이 주차장을 떠나면 곧바로 그 장소에 주차를 하게 한다. 만일 빈 주차 공간이 여러 곳이 있으면, 그 중 **번호가 가장 작은 주차 공간에 주차하도록 한다.** 만일 주차장에 여러 대의 차량이 도착하면, **일단 도착한 순서대로 입구의 대기장소에서 줄을 서서** 기다려야 한다. 대기장소는 큐(queue)와 같이, 먼저 대기한 차량부터 주차한다.

- 주차료 = 차량의 무게 * 주차 공간마다 따로 책정된 단위 무게당 요금

- 주차장 관리원은 **오늘 M대의 차량이 주차장을 이용**할 것이라는 것을 알고 있다. 또한, 차량들이 들어오고 나가는 순서도 알고 있다.

- 입력 : 주차 공간별 요금과 차량들의 무게와 출입 순서 
- 결과 : **하룻동안 주차장이 벌어들일 총 수입을 계산**

**입력**
- 반드시 표준 입력으로부터 다음의 데이터를 읽어야 한다.

- 첫 번째 줄에는 정수 N과 M이 빈칸을 사이에 두고 주어진다.
- 그 다음 N개의 줄에는 주차 공간들의 단위 무게당 요금을 나타내는 정수들이 주어진다. 그 중 s번째 줄에는 주차 공간 s의 단위 무게당 요금 Rs가 들어있다.
- 그 다음 M개의 줄에는 차량들의 무게를 나타내는 정수들이 주어진다. 차량들은 1 부터 M 까지 번호로 구분되고, 이 번호는 출입 순서와는 상관없다. 이 M개의 줄 중 k번째 줄에는 차량 k의 무게를 나타내는 정수 Wk가 들어있다.
- 그 다음 2*M 개의 줄에는 차량들의 주차장 출입 순서를 나타내는 정수들이 한 줄에 하나씩 주어진다. 양의 정수 i는 차량 i가 주차장에 들어오는 것을 의미하고, 음의 정수 -i는 차량 i가 주차장에서 나가는 것을 의미한다. 주차장에 들어오지 않은 차량이 주차장에서 나가는 경우는 없다. 1 번부터 M 번까지 모든 차량은 정확하게 한 번씩 주차장에 들어오고, 한 번씩 주차장에서 나간다. 또한 입구에서 대기 중인 차량이 주차를 하지 못하고 나가는 경우는 없다.
- 1 ≤ N ≤ 100 주차 공간의 수
- 1 ≤ M ≤ 2,000 차량의 수
- 1 ≤ Rs ≤ 100 주차 공간 s의 단위 무게당 요금
- 1 ≤ Wk ≤ 10,000 차량 k의 무게

**출력**
- 출력은 반드시 표준 출력으로 하여야 하며, 하나의 줄에 한 개의 정수를 출력한다. 이 정수는 오늘 하룻동안 주차장이 벌어들인 총 수입이다.

**아이디어**
- 필요한 데이터
    - 주차 공간 번호, 차량 번호, 차량 무게


```python
# 주차 공간 수, 오늘 이용할 자동차 수
N, M = map(int, input().split())

# 주차 공간들의 단위 무게당 요금
prices = list()
for _ in range(N):
    prices.append(int(input()))
    
# 차량들의 무게
cars_weight = [0]
for _ in range(M):
    cars_weight.append(int(input()))
    
# 차량 대기 공간 - queue
wait = list()

# 차량 주차장
parking = [0]*N


# 전체 요금 - 결과
result = 0

# 차량 입/퇴 장 순서
for _ in range(2 * M):
    io = int(input())
    if io > 0 :
        # 만차 확인
        if(0 not in parking):
            wait.append(io)
        else:
            ith = parking.index(0)
            parking[ith] = io
    else:
        io = -io
        ith = parking.index(io)
        # 출차 처리
        parking[ith] = 0
        result += cars_weight[io] * prices[ith]
        # 대기 차량 입장
        if(len(wait) != 0):
            parking[ith] = wait.pop(0)
    
print(result)
```

    3 4
    2
    3
    5
    200
    100
    300
    800
    3
    2
    -3
    1
    4
    -4
    -2
    -1
    5300
    

### 2800, 괄호 제거
**문제**
- 어떤 수식이 주어졌을 때, 괄호를 제거해서 나올 수 있는 서로 다른 식의 개수를 계산하는 프로그램을 작성하시오.

- 이 수식은 괄호가 올바르게 쳐져 있다. 예를 들면, 1+2, (3+4), (3+4*(5+6))와 같은 식은 괄호가 서로 쌍이 맞으므로 올바른 식이다.

- 하지만, 1+(2*3, ((2+3)*4 와 같은 식은 쌍이 맞지 않는 괄호가 있으므로 올바른 식이 아니다.

- 괄호를 제거할 때는, 항상 쌍이 되는 괄호끼리 제거해야 한다.

- 예를들어 (2+(2*2)+2)에서 괄호를 제거하면, (2+2*2+2), 2+(2*2)+2, 2+2*2+2를 만들 수 있다. 하지만, (2+2*2)+2와 2+(2*2+2)는 만들 수 없다. 그 이유는 쌍이 되지 않는 괄호를 제거했기 때문이다.

- 어떤 식을 여러 쌍의 괄호가 감쌀 수 있다.

**입력**
- 첫째 줄에 음이 아닌 정수로 이루어진 수식이 주어진다. 이 수식은 괄호가 올바르게 쳐져있다. 숫자, '+', '*', '-', '/', '(', ')'로만 이루어져 있다. 수식의 길이는 최대 200이고, 괄호 쌍은 적어도 1개, 많아야 10개이다. 

**출력**
- 올바른 괄호 쌍을 제거해서 나올 수 있는 서로 다른 식을 사전 순으로 출력한다.

**아이디어**
- 결과 경우의 수
    - 2 ^ 괄호 개수 - 1
- 입력 받은 문자열 - index 가능
- 괄호 위치 딕셔너리 생성
    - key : 열린 괄호 index
    - value : 닫힌 괄호 index
    - 괄호 개수 : len(딕셔너리)
- 경우의 수 계산 하여 빼도 되는 괄호의 쌍 index 를 찾는다.
    - 해당 index 의 문자열을 공백으로 치환 후 출력
    
### 왜 result 자료구조가 set 이 되어야 하는지 의문?


```python
import itertools

expression = list(input())

pairs = dict()

i = 0
for e in range(len(expression)):
    if expression[e] == "(":
        pairs[e] = i
        i += 1
    elif expression[e] == ")":
        i -= 1
        key_list = list(pairs.keys())
        key = key_list[list(pairs.values()).index(i)]
        pairs[key] = e

result = set()

for i in range(1, len(pairs)+1):
    comb = itertools.combinations(pairs.keys(), i)
    for j in comb:
        sub_expression = expression[:]
        for k in list(j):
            sub_expression[k] = ''
            sub_expression[pairs[k]] = ''
        result.add(''.join(map(str,sub_expression)))
        
for i in sorted(result):
    print(i)
```

    (0/(0))
    (0/0)
    0/(0)
    0/0
    


```python
import itertools

expression = list(input())

opens = list()
pairs = list()

i = 0
for e in range(len(expression)):
    if expression[e] == "(":
        opens.append(e)
    elif expression[e] == ")":
        open_ = opens.pop()
        pairs.append([open_, e])

result = set()

for i in range(1, len(pairs)+1):
    comb = itertools.combinations(pairs, i)
    for j in comb:
        sub_expression = expression[:]
        for k in list(j):
            sub_expression[k[0]] = ''
            sub_expression[k[1]] = ''
        result.add(''.join(map(str,sub_expression)))
        
for i in sorted(result):
    print(i)
```

    (0/(0))
    (0/0)
    0/(0)
    0/0
    

### 3190, 뱀

**문제**
- 'Dummy' 라는 도스게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다. 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.

- 게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에 벽이 있다. 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.

- 뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.
    - 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
    - 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
    - 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
    - 사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.

**입력**
- 첫째 줄에 보드의 크기 N이 주어진다. (2 ≤ N ≤ 100) 다음 줄에 사과의 개수 K가 주어진다. (0 ≤ K ≤ 100)

- 다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다. 사과의 위치는 모두 다르며, 맨 위 맨 좌측 (1행 1열) 에는 사과가 없다.

- 다음 줄에는 뱀의 방향 변환 횟수 L 이 주어진다. (1 ≤ L ≤ 100)

- 다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데,  정수 X와 문자 C로 이루어져 있으며. 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다. X는 10,000 이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.

**출력**
- 첫째 줄에 게임이 몇 초에 끝나는지 출력한다.

**아이디어**
- 보드의 가장자리 벗어 낫는지 확인
    - 최소값 <= 0 || 최대값 > N 확인
- 사과의 위치 표시
    - - [[x,y]] → [a1, a2],...
- 뱀의 위치를 [[x,y]] 로 표시 → deque
    - 이동 + 사과를 안 먹을 시
        - deque에 append(머리의 위치) → pop()
        - 머리의 위치 방향에 따라
            - deque[0]의 위치에 방향 맞춰서 해당 값 + / -
    - 이동 + 사과를 먹을 시
        - deque에 append(머리의 위치)


```python
from collections import deque
import copy

# 보드의 크기 N * N
N = int(input())

# 사과의 개수 K 개
K = int(input())
apple = []

for k in range(K):
    l, c = map(int, input().split())
    apple.append([c,-l]) #[x,y]
    
# 뱀의 방향 변환 횟수 L
L = int(input())
lotation = dict()
for l in range(L):
    t, c = input().split()
    t = int(t)
    lotation[t] =  c
    
# 뱀의 위치 표시 deque
snake = deque()
snake.append([1,-1])

time = 1 # 시간
way = 0 # 방향 [→,↓,←,↑]
while True:
    # 이동
    head = copy.deepcopy(snake[0]) # 머리 위치 확인
    if way == 0 :
        head[0] += 1 #오른쪽으로 한칸
    elif way == 1:
        head[1] -= 1 # 아래로 한칸
    elif way == 2:
        head[0] -= 1 # 왼쪽으로 한칸
    else :
        head[1] += 1 #위쪽으로 한칸
    
    # 자기 몸에 부딪혔는지 확인
    if head in snake:
        print(time)
        break
    else:
        snake.appendleft(head) # 머리 이동
    
    # 사과 먹었는지 확인
    new_head = snake[0]
    if new_head not in apple:
        snake.pop() # 꼬리 이동
    else:
        apple.remove(new_head) # 사과 먹은거 처리
        
    # board 벗어났는지 확인
    for s in snake:
        s[1] = - s[1]
    if max(max(snake)) > N or min(min(snake)) <= 0:
        print(time)
        break
    for s in snake:
        s[1] = - s[1]
        
    # 방향 전환
    if time in lotation.keys():
        if lotation[time] == 'D':
            way += 1
            if way == 4:
                way = 0
        else :
            way -= 1
            if way == -1:
                way = 3
        
    # 시간 + 1
    time += 1
```

    10
    5
    1 5
    1 3
    1 2
    1 6
    1 7
    4
    8 D
    10 D
    11 D
    13 L
    13
    

### 1935, 후위표기식 2

**문제**
- 후위 표기식과 각 피연산자에 대응하는 값들이 주어져 있을 때, 그 식을 계산하는 프로그램을 작성하시오.

**입력**
- 첫째 줄에 피연산자의 개수(1 ≤ N ≤ 26) 가 주어진다. 그리고 둘째 줄에는 후위 표기식이 주어진다. (여기서 피연산자는 A~Z의 영대문자이며, A부터 순서대로 N개의 영대문자만이 사용되며, 길이는 100을 넘지 않는다) 그리고 셋째 줄부터 N+2번째 줄까지는 각 피연산자에 대응하는 값이 주어진다. 3번째 줄에는 A에 해당하는 값, 4번째 줄에는 B에 해당하는값 , 5번째 줄에는 C ...이 주어진다, 그리고 피연산자에 대응 하는 값은 100보다 작거나 같은 자연수이다.

- 후위 표기식을 앞에서부터 계산했을 때, 식의 결과와 중간 결과가 -20억보다 크거나 같고, 20억보다 작거나 같은 입력만 주어진다.

**출력**
- 계산 결과를 소숫점 둘째 자리까지 출력한다.


```python
from collections import deque
import string

N = int(input())

expression = list(input())

nums = list()
for _ in range(N):
    nums.append(input())
    
alphas = string.ascii_uppercase[:N]
for i in range(len(alphas)):
    while alphas[i] in expression:
        expression[expression.index(alphas[i])] = nums[i]

nums = deque()

for e in expression:
    if e not in ['+','*','/','-']:
        nums.append(e)
    else:
        a = nums.pop()
        b = nums.pop()
        c = str(eval(b + e + a))
        nums.append(c)
        
print("{:.2f}".format(float(nums[0])))
```

    1
    AA+A+
    1
    3.00
    

### 1662, 압축

**문제**
- 압축되지 않은 문자열 S가 주어졌을 때, 이 문자열중 어떤 부분 문자열은 K(Q)와 같이 압축 할 수 있다. K는 한자리 정수이고, Q는 0자리 이상의 문자열이다. 이 Q라는 문자열이 K번 반복된다는 뜻이다. 압축된 문자열이 주어졌을 때, 이 문자열을 다시 압축을 푸는 프로그램을 작성하시오.

**입력**
- 첫째 줄에 압축된 문자열 S가 들어온다. S의 길이는 최대 50이다. 문자열은 (, ), 0-9사이의 숫자로만 들어온다.

**출력**
- 첫째 줄에 압축되지 않은 문자열의 길이를 출력한다. 이 값은 int범위다.

**아이디어**
- S → K(Q) 로 압축
    - Q 라는 문자열이 K 번 반복 된다.
- '(' 로 split 하여 리스트에 추가 한다.


```python
S = input().split("(")
S[-1] = S[-1].split(")")
sub_S = S.pop()

result = 0

for i in range(len(S)):
    result = result + len(sub_S[i])
    result = int(S[-1-i][-1]) * result
    result = result + len(S[-1-i]) - 1

print(result)
```

    33(56(3)2(71(9)))
    112
    
