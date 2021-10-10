# 문제 이해가 정말 어려웠던 지금도 어려운 문제
# B -> 1 2 0
# A -> 2 3 1
# 입력, 출력값을 보면서 이해하는게 제일 중요했음
# B수열은 A수열의 비내림차순 수열이라는 것을 이해하는게 중요
import sys


def sequence_sort():
    N = int(input())
    number = list(map(int, sys.stdin.readline().split()))
    # A리스트에 값과 값의 위치를 같이 넣어준다
    A = []
    for i in range(len(number)):
        A.append([number[i], i])
    # 값을 기준으로 정렬을 한다
    sort_A = sorted(A, key=lambda x: x[0])
    num = 0
    B = [0 for i in range(N)]
    # 정렬한 A를 순서대로 보며 위치를 B[위치]에 다가 활용하여 그곳에 0부터 차례대로 저장한다
    for i in range(N):
        B[sort_A[i][1]] = num
        num += 1
    print(' '.join(map(str, B)))
    return


sequence_sort()