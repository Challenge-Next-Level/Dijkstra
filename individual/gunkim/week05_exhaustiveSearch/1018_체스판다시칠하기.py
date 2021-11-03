# 맨 처음 8*8사이즈 체스판에 대한 모든 경우를 비교하며 따져야 하나? 라는 생각에 아닐것!이라 판단을 했다
# 하지만 다른 분들이 4중 for문으로 풀이한 것을 보고 맞구나 라는걸 알게 되었다.
# 체스판의 W,B를 판별하는 것이 어렵다고 판단하여 처음에 W,B로 시작하는 케이스를 하드코딩으로 만들어 비교를 했다.(통과는 함)
# 하지만 역시 행,렬의 합을 통해 판별하는 좋은 방법이 있었고 그것으로 수정을 했다.
import sys


def chess():
    # 보드 만들기
    N , M = map(int, input().split())
    ex = [[0] * M for _ in range(N)]
    for i in range(N):
        ex[i] = sys.stdin.readline().split()
        ex[i] = list(ex[i][0])

    answer = 64
    # 시작 지점 경우의 수
    for i in range(N - 7):
        for j in range(M - 7):
            min1, min2 = 0, 0
            # 시작 지점에서 8 * 8 크기의 체스판 판별 시작
            for c1 in range(8):
                for c2 in range(8):
                    # 행렬의 합을 통해 W,B를 판단
                    # 첫 시작이 W인 경우 (W:짝수,B:홀수)
                    if (c1 + c2) % 2 == 0 and ex[i + c1][j + c2] == 'B':
                        min1 += 1
                    elif (c1 + c2) % 2 == 1 and ex[i + c1][j + c2] == 'W':
                        min1 += 1
                    # 첫 시작이 B인 경우 (B:짝수,W:홀수)
                    if (c1 + c2) % 2 == 0 and ex[i + c1][j + c2] == 'W':
                        min2 += 1
                    elif (c1 + c2) % 2 == 1 and ex[i + c1][j + c2] == 'B':
                        min2 += 1
            # 색을 칠하는 최솟값을 판단
            answer = min(answer, min(min1, min2))

    return answer


print(chess())