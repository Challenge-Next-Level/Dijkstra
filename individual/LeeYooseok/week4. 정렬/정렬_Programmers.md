### K번째 수

**문제 설명**
- 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

- 예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면
    1. array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
    2. 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
    3. 2에서 나온 배열의 3번째 숫자는 5입니다.
- 배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

**제한사항**
- array의 길이는 1 이상 100 이하입니다.
- array의 각 원소는 1 이상 100 이하입니다.
- commands의 길이는 1 이상 50 이하입니다.
- commands의 각 원소는 길이가 3입니다.

**입출력 예**

|array|commands|return|
|---|---|---|
|[1, 5, 2, 6, 3, 7, 4]|[[2, 5, 3], [4, 4, 1], [1, 7, 3]]|[5, 6, 3]|

**아이디어**
- 기본 배열을 복사본으로 해당 연산을 수행
- 정렬된 배열을 반환하여 원본 배열이 바뀌지 않도록 sorted 사용


```python
def solution(array, commands):
    answer = []
    for n in range(len(commands)):
        command = commands[n]
        i = command[0]
        j = command[1]
        k = command[2]
        sub_array = array[i-1:j]
        
        sorted_sub_array = sorted(sub_array)
        answer.append(sorted_sub_array[k-1])
    
    return answer
```


```python
solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]])
```




    [5, 6, 3]



### 가장 큰 수

**문제 설명**
- 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

- 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

- 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

**제한 사항**
- numbers의 길이는 1 이상 100,000 이하입니다.
- numbers의 원소는 0 이상 1,000 이하입니다.
- 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.

**입출력 예**

|numbers|return|
|---|---|
|[6, 10, 2]|"6210"|
|[3, 30, 34, 5, 9]|"9534330"|

**아이디어**
- 어떻게 할까?



```python
def solution(numbers):
    
```


```python
solution([6,10,2])
```


```python
solution([3,30,34,5,9])
```

### H-Index

**문제 설명**
- H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

- 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

- 어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

**제한사항**
- 과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
- 논문별 인용 횟수는 0회 이상 10,000회 이하입니다.

**입출력 예**

|citations|return|
|---|---|
|[3, 0, 6, 1, 5]|3|

**아이디어**
- citations를 오름차순으로 정렬
- h_index를 citiations의 길이부터 -1 하며 확인


```python
def solution(citiations):
    answer = 0
    
    citiations.sort()
    
    for i in range(len(citiations)):
        h_index = len(citiations) - i
        if citiations[i] >= h_index:
            answer = h_index
            break
            
    return answer
```


```python
solution([3,0,6,1,5])
```




    3


