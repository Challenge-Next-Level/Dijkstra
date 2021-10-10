# sort와 sorted는 stable한 정렬이다
import sys


def age_sort():
    N = int(input())
    answer = []
    for i in range(N):
        person = sys.stdin.readline().split()
        person[0] = int(person[0])
        answer.append(person)
    ans = sorted(answer, key=lambda x: x[0])
    for i in ans:
        i[0] = str(i[0])
        print(' '.join(i))
    return


age_sort()