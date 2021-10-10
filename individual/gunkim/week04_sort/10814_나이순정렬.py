# sort와 sorted는 stable한 정렬이다
import sys


def age_sort():
    N = int(input())
    answer = []
    for i in range(N):
        person = sys.stdin.readline().split()
        # 뒤에서 나이를 기준으로 정렬을 해야하기 때문에 int로 형변환
        person[0] = int(person[0])
        answer.append(person)
    ans = sorted(answer, key=lambda x: x[0])
    for i in ans:
        # join을 위해 int를 str로 형변환
        i[0] = str(i[0])
        print(' '.join(i))
    return


age_sort()