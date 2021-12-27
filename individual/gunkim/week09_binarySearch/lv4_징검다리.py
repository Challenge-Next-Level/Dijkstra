def solution(distance, rocks, n):
    answer = 0
    # 바위 정렬 및 마지막 도착 바위 추가(거리 계산 위함)
    rocks.sort()
    rocks.append(distance)
    # 이분 탐색
    left, right = 1, distance
    while left <= right:
        mid = (left + right) // 2 # mid 값은 징검다리에서 최소 거리
        min_dist = float('inf') # 바위 제거 한 징검다리의 최소 거리
        loc, remove = 0, 0 # 이전 바위 위치, 제거한 바위 수
        for r in rocks:
            dist = r - loc # 바위 사이 거리 계산
            if dist < mid: # mid보다 작은 거리는 있으면 안되니 제거
                remove += 1
            else: # 충족하는 거리, loc과 min_dist 업데이트
                loc = r
                min_dist = min(min_dist, dist)
        # left, right 설정
        if remove > n: # 너무 많이 제거했으니 right값 줄이기
            right = mid - 1
        else: # 덜 제거됐으니 left늘리기, 같은 경우도 포함이라 answer 업데이트
            left = mid + 1
            answer = min_dist
    return answer


print(solution(25, [2, 14, 11, 21, 17], 2))