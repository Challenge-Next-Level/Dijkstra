# ICN부터 무조건 시작: 이 조건을 몰랐다. 코드를 수정하여 제출했는데 1번 테스트만 통과하지 못함
# 이유: 같은 경로의 티켓이 존재할 수 있다는 점
# 다른 분의 풀이: 티켓을 delete하며 진행 -> 삭제가 맘에 들지 않음
# 또 다른 분의 풀이: 다시 이렇게 해결하라하면 풀지 못할 것 같음 -> 개어려움
def solution(tickets):
    answer = []
    routes = {}
    # 1. 티켓을 딕셔너리로 정리한다
    for ticket in tickets:
        if ticket[0] not in routes:
            routes[ticket[0]] = []
        routes[ticket[0]].append(ticket[1])
    # 2. 알파벳이 빠른 것이 뒤로가게 정렬
    for key in routes.keys():
        routes[key].sort(reverse=True)
    # 3. 무조건 ICN 부터 시작
    stack = ['ICN']
    while stack:
        tmp = stack[-1]
        # 4. 스택 마지막 값에서 갈 수 있는 루트가 있다면 스택에 추가한다
        if tmp in routes and len(routes[tmp]) != 0:
            stack.append(routes[tmp].pop())
        # 5. 없다면 pop 진행을 하며 이를 경로(answer)로 저장한다
        else:
            answer.append(stack.pop())
    # 6. 경로가 역순으로 저장되어 있으므로 재정렬
    answer.reverse()
    return answer


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
