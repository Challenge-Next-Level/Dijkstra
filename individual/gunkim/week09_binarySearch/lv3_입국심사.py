# 이전에 프로그래머스 개발자 코테에서도 여러 화구에 음식을 하는 문제가 있었는데 그것이 이분 탐색으로 해결하는 것이었다는 걸...
# 이분 탐색을 드디어 조금 알 것 같다!!!
def solution(n, times):
    answer = 0
    times.sort()
    # left: 최소 시간, right: 최악 시간 설정
    left, right = 1, times[-1] * n
    while left <= right:
        mid = (left + right) // 2
        people = 0
        # mid 시간 동안 각 심사관들이 심사할 수 있는 수를 더한다
        for time in times:
            people += mid // time
            if people > n:
                break
        # 심사한 사람들의 수가 부족하면 left 증가, 충분하면 right 감소
        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer


print(solution(6, [7, 10]))