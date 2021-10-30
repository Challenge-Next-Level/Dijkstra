### 모의고사

**문제 설명**
- 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

- 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, ...
- 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5,  ...
- 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5,  ...

- 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

**제한 조건**
- 시험은 최대 10,000 문제로 구성되어있습니다.
- 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
- 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

**입출력 예**

|answers|return|
|---|---|
|[1,2,3,4,5]|[1]|
|[1,3,2,4,2]|[1,2,3]|

**아이디어**
- 사람 : 맞힌 문제 수 형식으로 딕셔너리 만듦
- answer의 길이만큼 반복
    - if answer[i] == sol1[i % 5]:
         - 딕셔너리[1] += 1
    - if answer[i] == sol2[i % 8]:
         - 딕셔너리[2] += 1
    - if answer[i] == sol3[i % 10]:
        - 딕셔너리[3] += 1


```python
def solution(answers):
    sol1 = [1,2,3,4,5]
    sol2 = [2,1,2,3,2,4,2,5]
    sol3 = [3,3,1,1,2,2,4,4,5,5]
    
    score = dict()
    score[1] = 0
    score[2] = 0
    score[3] = 0
    
    for i in range(len(answers)):
        if answers[i] == sol1[i % 5]:
            score[1] += 1
        if answers[i] == sol2[i % 8]:
            score[2] += 1
        if answers[i] == sol3[i%10]:
            score[3] += 1
    
    score_list = list(score.values())
    max_score = max(score_list)
    answer = []
    
    for i in range(len(score_list)):
        if score_list[i] == max_score:
            answer.append(i+1)
    
    return answer
```


```python
solution([1,3,2,4,2])
```




    [1, 2, 3]



### 소수 찾기

**문제 설명**
- 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

- 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

**제한사항**
- numbers는 길이 1 이상 7 이하인 문자열입니다.
- numbers는 0~9까지 숫자만으로 이루어져 있습니다.
- "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

**입출력 예**

|numbers|return|
|---|---|
|"17"|3|
|"011"|2|

**아이디어**
- 입력 숫자들로 만들 수 있는 모든 수 리스트 생성
- 만들 수 있는 가장 큰 숫자까지의 소수 리스트 생성
- 소수 개수 확인


```python
from itertools import permutations

def solution(numbers):
    nums = list(numbers)
    # 만들 수 있는 모든 수 리스트 생성
    all_nums = list()
    for i in range(1,len(nums)+1):
        all_nums += list(map(''.join, permutations(nums, i)))
        
    # 중복 제거 및 문자열 숫자로 변경
    all_nums = list(set(list(map(int, all_nums))))
    
    # 만들 수 있는 가장 큰 숫자까지의 소수 리스트 생성 - 에리토스테네스의 체 사용
    max_num = max(all_nums)
    prime_nums = list()
    a = [False, False] + [True] * (max_num-1)
    for i in range(2,max_num+1):
        if a[i]:
            prime_nums.append(i)
            for j in range(2*i, max_num+1, i):
                a[j] = False
                
    answer = 0
    
    for num in all_nums:
        if num in prime_nums:
            answer += 1
    
    return answer
```


```python
solution("011")
```




    2



### 카펫

**문제 설명**
- Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.
- Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.

- Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

**제한사항**
- 갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
- 노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
- **카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.**

**입출력 예**

|brown|yellow|return|
|---|---|---|
|10|2|[4, 3]|
|8|1|[3, 3]|
|24|24|[8, 6]|


**아이디어**
- m >= n
- 노랑 카펫 개수 -> m * n 으로 표현
- 갈색 카펫 개수 + 노랑 카펫 개수 -> m+2 * n+2 로 표현


```python
def solution(brown, yellow):
    norans = list()
    for i in range(yellow,0, -1):
        if yellow % i == 0:
            # m >= n 제한조건 만족
            norans.append(sorted([i, yellow//i], reverse = True))
           
    answer = []
    
    for i in norans:
        if brown+yellow == (i[0] + 2)*(i[1] + 2):
            answer = [i[0]+2, i[1]+2]
    
    return answer
```


```python
solution(8,1)
```




    [3, 3]


