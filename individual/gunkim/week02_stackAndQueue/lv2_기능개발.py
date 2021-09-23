def solution(progresses, speeds):
    answer = []
    time = 0
    cnt = 0
    while len(progresses) != 0:
        if progresses[0] + speeds[0] * time >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            time += 1
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
    answer.append(cnt)
    return answer


pro = [95, 90, 99, 99, 80, 99]
spe = [1, 1, 1, 1, 1, 1]
print(solution(pro, spe))