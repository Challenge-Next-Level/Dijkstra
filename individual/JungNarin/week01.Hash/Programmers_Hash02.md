## 2. 전화번호 목록

### 문제설명
- 파라미터: 리스트 1개
  - phone_book = ["119", "97674223", "1195524421"]
  
- 반환값: phone_book의 임의의 번호가 다른 번호의 접두어인 경우 <b>false</b>, 그렇지 않다면 <b>true</b> 반환

### 조건
- 같은 번호가 들어있지 않다.

### 아이디어
- 최소한으로 for문이 돌아가도록 해야 한다.
  - 리스트를 정렬한자. 최대한 비슷한 숫자끼리 인접하도록. ex) 119, 21, 11952 -> 119, 11952, 21
    - <b>바로 다음 문자열의 접두어가 아니라면 더이상 for문을 돌 필요 없다.</b>
    - <b>다음 문자열의 접두어인 문자열이 하나라도 발견되면 False를 리턴하므로 바로 뒤의 원소랑만 비교하면 된다!</b>
  
- 한 문자열이 다른 문자열의 시작 부분과 정확하게 일치한다.
  - startswith() 함수를 사용하자.
  
- for문을 돌면서 한 원소와 바로 뒤에 있는 원소를 비교한다.
  - zip함수를 사용해서 두 원소를 담은 tuple를 만든다. 
  - tuple의 원소를 변수 2개에 담고 비교한다.
    

```
def solution(phone_book):
    phone_book = sorted(phone_book);
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False;
    return True;
```
