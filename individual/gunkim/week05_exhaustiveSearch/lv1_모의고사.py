def solution(answers):
    # 1번 : 12345
    # 2번 : 21232425
    # 3번 : 3311224455
    answer = [0, 0, 0]
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if answers[i] == one[i % 5]:
            answer[0] += 1
        if answers[i] == two[i % 8]:
            answer[1] += 1
        if answers[i] == three[i % 10]:
            answer[2] += 1

    name = []
    max_answer = max(answer)
    for i in range(len(answer)):
        if answer[i] == max_answer:
            name.append(i + 1)
    return name


a = [1,3,2,4,2]
solution(a)


