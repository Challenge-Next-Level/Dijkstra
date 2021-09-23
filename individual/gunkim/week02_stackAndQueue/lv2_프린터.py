def solution(priorities, location):
    answer = 0
    while len(priorities) != 0:
        # 런타임 에러가 발생해서 pop을 앞이 아닌 뒤로 옮겼다.
        num = priorities[0]
        if num >= max(priorities):
            answer += 1
            if location == 0:
                break
        else:
            priorities.append(num)
        priorities.pop(0)
        if location == 0:
            location = len(priorities) - 1
        else:
            location -= 1
    return answer


pri = [1, 1, 9, 1, 1, 1]
loc = 0
print(solution(pri, loc))