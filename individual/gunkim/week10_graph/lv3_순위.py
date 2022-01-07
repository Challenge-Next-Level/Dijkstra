def dfs(person, chart):
    win = []  # person이 이기는 사람들 세팅
    for idx, result in enumerate(chart[person]):
        if result == 1:
            win.append(idx)
    while win:  # person이 이긴 사람(a)이 이기는 사람(b)은 결국 person도 b를 이길 수 있다
        loser = win.pop()
        for idx, result in enumerate(chart[loser]):
            if result == 1 and chart[person][idx] == 0:
                chart[person][idx], chart[idx][person] = 1, -1  # 승패표 추가 수정
                win.append(idx)  # person이 이기는 사람들 세팅에 추가


def solution(n, results):
    answer = 0
    # 승, 패 결과표 세팅
    chart = [[0] * n for _ in range(n)]
    for i in results:
        a, b = i
        chart[a - 1][b - 1], chart[b - 1][a - 1] = 1, -1
    # 각각의 사람이 이길 수 있는 사람을 dfs탐색으로 모두 알아내기
    for me in range(n):
        dfs(me, chart)
    # 승패표가 모두 채워져있는 사람(0이 하나인 person)은 순위를 알 수 있음
    for i in chart:
        if i.count(0) == 1:
            answer += 1
    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))