# 사실 스터디에서 유석님의 풀이를 먼저 보고 해결한 문제이다.
# 그때 진출 시점으로 정렬한 것에서 포인트를 얻어 풀이를 진행했다.
def solution(routes):
    # 진출 시점으로 route 정렬
    routes.sort(key=lambda x: x[1])
    # 첫 번째 카메라 위치를 첫 route의 진출 지점으로 설정
    idx, camera = 1, routes[0][1]
    answer = 1
    length = len(routes)
    while idx < length:
        # 카메라의 위치가 다음 route의 범위 안에 들어가지 않는 다면 새로 카메라를 생성
        if routes[idx][0] > camera or camera > routes[idx][1]:
            camera = routes[idx][1]
            answer += 1
        idx += 1
    return answer


r = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(r))