def solution(numbers, target):
    answer = 0
    length = len(numbers)

    # numbers의 idx값과 현재까지 계산된 val값을 인자로 넣어준다
    def dfs(idx, val):
        if idx >= length:
            if val == target:
                nonlocal answer
                answer += 1
            return
        dfs(idx + 1, val + numbers[idx])
        dfs(idx + 1, val - numbers[idx])
        return

    dfs(0, 0)
    return answer


n = [1, 1, 1, 1, 1]
t = 3
print(solution(n, t))