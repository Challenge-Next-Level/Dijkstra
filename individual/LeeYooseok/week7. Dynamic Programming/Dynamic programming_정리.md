## Dynamic Programming

### - 큰 문제를 작은 문제로 나눌 수 있다.
### - 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.

- ### 방식
    - Top Down 방식
        - 재귀함수를 이용하여 순환하는 방식
        
    - Bottom Up 방식
        - 작은 문제로부터 큰 문제의 답 도출
        
    - 공통점
        - 다음 상태를 구하기 위해, 이전 상태를 저장하고 재 사용합니다.
- ### 적용 방식
    - 상태 정의 : DP배열의 index가 의미하는 것과 문제의 초기상태 정의
    - 점화식 구하기 : 다음 상태를 나타내기 위한 표현식
    - 시간 복잡도 계산
