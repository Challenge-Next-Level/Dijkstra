def solution(array, commands):
    answer = []
    for i in commands:
        slice = array[i[0] - 1:i[1]]
        s = sorted(slice)
        answer.append(s[i[2] - 1])
    print(answer)
    return answer


a = [1, 5, 2, 6, 3, 7, 4]
c= [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
solution(a, c)