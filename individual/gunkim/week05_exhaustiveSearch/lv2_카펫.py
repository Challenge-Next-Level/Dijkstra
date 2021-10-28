def solution(brown, yellow):
    answer = []
    for i in range(yellow, 0, -1):
        if yellow % i == 0:
            width = i + 2
            height = int((yellow / i)) + 2
            if width * height - yellow == brown:
                answer = [width, height]
                break
    return answer


b = 24
y = 24
print(solution(b, y))