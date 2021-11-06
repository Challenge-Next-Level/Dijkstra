# 입력값이 항상 오름차순으로 입력된다는 고정관념을 깨자!
def solution(n, lost, reserve):
    answer = 0
    # 내가 18, 20 test case를 틀렸던 이유
    # 학생들의 번호가 담긴 lost, reserve를 정렬하고 제출했더니 통과했다 ㅎㅎ;;
    lost.sort()
    reserve.sort()

    # 처음에 틀리고 수정을 했던 곳
    # 체육복을 잃어버리고 여유분이 있는 학생은 애초에 본인 체육복으로 지급 받아야 하기에
    # 체육복 소유 여부 list를 만드는 과정에서 유의하여 만든다.
    have = [1 for _ in range(n)]
    for i in range(len(lost)):
        if lost[i] not in reserve:
            have[lost[i] - 1] = 0
    # 체육복 여분을 앞 친구 or 뒤 친구에게 준다
    for i in range(len(reserve)):
        if reserve[i] not in lost:
            if reserve[i] - 2 >= 0 and have[reserve[i] - 2] == 0:
                have[reserve[i] - 2] = 1
            elif reserve[i] < n and have[reserve[i]] == 0:
                have[reserve[i]] = 1
    # have리스트에서 체육복이 있는 친구들을 count
    for i in range(n):
        if have[i] == 1:
            answer += 1
    return answer


N = 5
l = [2,5,6]
r = [2,4,6]
print(solution(N, l, r))