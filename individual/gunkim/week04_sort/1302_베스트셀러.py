import sys


def best_seller():
    N = int(input())
    dict = {}
    for i in range(N):
        book = sys.stdin.readline().split()[0]
        if book in dict:
            dict[book] += 1
        else:
            dict[book] = 1
    answer = []
    max = 0
    for i in dict:
        if dict[i] > max:
            max = dict[i]
    for i in dict:
        if dict[i] == max:
            answer.append(i)
    answer.sort()
    print(answer[0])
    return


best_seller()