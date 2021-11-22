# 코드를 수정하며 최적화를 진행했다. 조금의 깨달음을 얻은 문제
# 1. 처음 틀렸던 이유: cost 최악의 경우 값이 천만이었는데 백만으로 놓고 제출했었음
# 2. 최적화 첫 번째: dfs함수 내에서 visit을 deep copy를 통해 따로 공간 생성 후 넣었었는데 그냥 dfs함수 사용 전 후로 append, pop을 진행하면 되었다
# 3. 최적화 두 번째: backtracking이용. 현재 cost가 이미 answer값 보다 크다면 return을 하면 되었다
# 4. 번외: 이 TSP 문제는 비트마스킹 해결법으로 푸는게 최고라고 한다
import sys


def dfs(idx, cost, visit):
    global answer
    # 모두 방문했다면 순회 종료
    if len(visit) == len(arr[0]):
        if arr[idx][0] != 0:
            cost += arr[idx][0]
            answer = min(answer, cost)
        return
    # backtracking: 이미 cost가 answer보다 크다면 리턴
    if cost >= answer:
        return
    # 방문하지 않은 곳에 대해 순회
    for i in range(len(arr[0])):
        if i not in visit and arr[idx][i] != 0:
            visit.append(i)
            dfs(i, cost + arr[idx][i], visit)
            visit.pop()
    return


def solution():
    N = int(input())
    for i in range(N):
        cost = list(map(int, sys.stdin.readline().split()))
        arr.append(cost)
    # index(0에서 시작), cost, visit
    dfs(0, 0, [0])
    return answer


answer = 10000000
arr = []
print(solution())