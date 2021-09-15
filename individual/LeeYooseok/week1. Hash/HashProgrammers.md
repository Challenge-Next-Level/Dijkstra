### 1. 완주하지 못한 선수
**문제 설명**
- 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

- 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

**제한사항**
- 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
- completion의 길이는 participant의 길이보다 1 작습니다.
- 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
- 참가자 중에는 동명이인이 있을 수 있습니다.

**입출력 예**

|participant|completion|return|
|---|---|---|
|["leo", "kiki", "eden"]|["eden", "kiki"]|"leo"|
|["marina", "josipa", "nikola", "vinko", "filipa"]|["josipa", "filipa", "marina", "nikola"]|"vinko"|
|["mislav", "stanko", "mislav", "ana"]|["stanko", "ana", "mislav"]|"mislav"|

**아이디어**
- participant 와 completion 의 리스트 길이가 1이 차이난다.
- 각 리스트를 오름차순으로 정렬 후 다른것이 있는지 확인


```python
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(participant)-1):
        if participant[i] != completion[i]:
            answer = participant[i]
            return answer
    answer = participant[-1]
    return answer
```


```python
solution(["leo", "kiki", "eden"],["eden", "kiki"])
```




    'leo'



### 2. 전화번호 목록
**문제 설명**
- 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
- 전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.
    - 구조대 : 119
    - 박준영 : 97 674 223
    - 지영석 : 11 9552 4421
- 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

**제한 사항**
- phone_book의 길이는 1 이상 1,000,000 이하입니다.
- 각 전화번호의 길이는 1 이상 20 이하입니다.
- 같은 전화번호가 중복해서 들어있지 않습니다.

**입출력 예**

|phone_book|return|
|---|---|
|["119", "97674223", "1195524421"]|false|
|["123","456","789"]|true|
|["12","123","1235","567","88"]|false|

**아이디어**
- phone_book을 길이 순으로 정렬한다.
- 맨 앞부터 해당 번호가 리스트내의 다른 번호에 포함되어 있는지 확인
- 있을 시 false 반환


```python
def solution(phone_book):
    phone_book.sort() # list sort 시 앞에 수에 따라 정렬된다.
    for i in range(1,len(phone_book)):
        head = phone_book[i-1]
        next_head = phone_book[i]
        if head == next_head[:len(head)]:
            answer = False
            return answer
    answer = True
    return answer
```


```python
solution(["119", "97674223", "1195524421"])
```

    ['119', '1195524421', '97674223']
    




    False



### 3. 위장
**문제 설명**
- 스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장합니다.

- 예를 들어 스파이가 가진 옷이 아래와 같고 오늘 스파이가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야 합니다.

|종류|이름|
|---|---|
|얼굴|동그란 안경, 검정 선글라스|
|상의|파란색 티셔츠|
|하의|청바지|
|겉옷|긴 코트|

- 스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

**제한사항**
- clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
- 스파이가 가진 의상의 수는 1개 이상 30개 이하입니다.
- 같은 이름을 가진 의상은 존재하지 않습니다.
- clothes의 모든 원소는 문자열로 이루어져 있습니다.
- 모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
- 스파이는 하루에 최소 한 개의 의상은 입습니다.

입출력 예

|clothes|return|
|---|---|
|[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]|5|
|[["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]|3|

**아이디어**
- 각 옷의 종류를 key 로 갇는 딕셔너리 생성
- clothes 를 반복하여 옷의 종류 개수를 확인
- 조합 계산
    - 각 옷의 종류 개수 + 1 한 수를 모두 곱한 값에서 1을 뺀다.
        - 해당 옷의 종류를 안입는 경우의 수 고려
        - 최소 한 개의 의상은 입어야 하므로 1을 뺀다.


```python
def solution(clothes):
    wear = dict()
    for cloth in clothes:
        if cloth[1] in wear.keys():
            wear[cloth[1]] += 1
        else :
            wear[cloth[1]] = 1
    answer = 1
    for i in wear.values():
        answer = answer * (i+1)
    return answer-1
```


```python
solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])
```




    3



### 4. 베스트 앨범
**문제 설명**
- 스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

- 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
- 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
- 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
- 노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 - 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

**제한사항**
- genres[i]는 고유번호가 i인 노래의 장르입니다.
- plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
- genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
- 장르 종류는 100개 미만입니다.
- 장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
- 모든 장르는 재생된 횟수가 다릅니다.

**입출력 예**

|genres|plays|return|
|---|---|---
|["classic", "pop", "classic", "classic", "pop"]|[500, 600, 150, 800, 2500]|[4, 1, 3, 0]|

**아이디어**
- 장르별 재생 횟수를 딕셔너리로 확인한다.
    - key : values = 장르 : {고유번호 : 재생 횟수}
- 재생횟수가 많은 순 대로 dict 를 정렬한다.
- 결과 리스트에 결과값 추가


```python
def solution(genres, plays):
    # 장르별 딕셔너리로 정리
    songs = dict()
    for i in range(len(genres)):
        genre = genres[i]
        if genre not in songs.keys():
            songs[genre] = dict()
        songs[genre][i] = plays[i]
    print(songs)
    
    # 재생 횟수 기준으로 정렬된 장르 리스트
    plays = dict()
    for i in songs.keys():
        plays[i] = sum(songs[i].values())
    plays = sorted(plays.items(), key= lambda x : x[1], reverse = True)
    print(plays)
    
    # 재생 횟수가 높은 장르 부터 반복
    # 재생 횟수가 높은 노래의 고유 번호 부터 answer 에 추가
    answer = []
    for i in plays:
        songs[i[0]] = sorted(songs[i[0]].items(), key= lambda x : x[1], reverse = True)
        for j in songs[i[0]][:2]:
            answer.append(j[0])
    return answer
```


```python
solution(["classic", "pop", "classic", "classic", "pop"], [500,600,150,800,2500])
```

    {'classic': {0: 500, 2: 150, 3: 800}, 'pop': {1: 600, 4: 2500}}
    [('pop', 3100), ('classic', 1450)]
    




    [4, 1, 3, 0]


