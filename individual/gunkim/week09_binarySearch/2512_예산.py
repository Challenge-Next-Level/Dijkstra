N = int(input())
budget = list(map(int, input().split()))
total = int(input())
# 요청된 예산 정렬
budget.sort()
if sum(budget) <= total: # 모든 요청이 배정될 수 있는 경우
    print(budget[-1])
else: # 그렇지 못한 경우, 이분탐색
    left, right = 1, budget[-1]
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        sum_budget = 0
        for b in budget: # 상한액 이하의 예산 요청은 그대로 배정
            if b < mid:
                sum_budget += b
            else: # 상한액 초과 요청은 상한액으로 배정
                sum_budget += mid
        # left, right 값 조절
        if sum_budget > total:
            right = mid - 1
        else:
            left = mid + 1
            answer = max(answer, mid)
    print(answer)