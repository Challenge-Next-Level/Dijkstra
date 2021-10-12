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
    # 우선 팔린 책 갯수에 대해 내림차순 정렬
    dict_sort = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    # 가장 많이 팔린 책들만 따로 뽑아서 사전순 정렬
    max = dict_sort[0][1]
    answer = []
    for i in dict_sort:
        if i[1] == max:
            answer.append(i)
    answer.sort()
    # 출력
    print(answer[0][0])
    return


best_seller()