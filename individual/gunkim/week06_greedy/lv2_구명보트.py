# 내가 처음 해결하려한 방법
# 1.처음 사람부터 나머지 사람들과 무게 합을 비교한다
# 2.무게 합이 limit보다 작으면서 제일 큰 것을 골라내 보트에 탑승시킨다
# 하지만 문제는 이 방법이 딱봐도 최적의 효율이 아니라는 것...하;;
# 결국 해결법은 너무 간단했다. 사람들을 정렬 후 무게가 가장 무거운 사람들을 작은 사람들과 비교를 통해 태우면 되는 것
from collections import deque


def solution(people, limit):
    answer = 0
    # 몸무게를 정렬 후 dequeue로 생성한다
    people.sort()
    dq = deque(people)
    while dq:
        # 최고 몸무게 + 최저 몸무게 < 제한 을 만족하면 최저 몸무게도 pop
        # dequeue의 크기가 2이상일 때만 비교 가능
        if len(dq) > 1 and dq[0] + dq[-1] <= limit:
            dq.popleft()
        dq.pop()
        answer += 1
    return answer


p = [70, 80, 50]
l = 100
print(solution(p, l))