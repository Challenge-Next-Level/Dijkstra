from collections import deque


def snake():
    N = int(input())
    K = int(input())
    board = [[0 for col in range(N)] for row in range(N)]
    dir = deque()
    # 먹이를 board에 입력
    for i in range(K):
        x, y = map(int, input().split())
        board[x - 1][y - 1] = 1
    L = int(input())
    # 방향전환정보 저장
    for i in range(L):
        dir.append(input().split())

    time = 0
    # 방향전환을 위한 변수
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    d = 0
    # 머리위치, 몸통의위치
    head = [0, 0]
    body = deque()
    body.append([0, 0])
    # 이전에 먹이를 먹었는지 여부
    eat = 0
    while True:
        time += 1
        # 머리 이동
        head[0] += dx[d]
        head[1] += dy[d]
        # 게임이 끝나는 조건
        if head[0] < 0 or head[0] >= N or head[1] < 0 or head[1] >= N or head in body:
            break
        # 꼬리 이동, 몸통위치 이동
        if eat == 0:
            idx = body.popleft()
            board[idx[0]][idx[1]] = 0
        a = head[0]
        b = head[1]
        body.append([a, b])

        # 사과가 있을 때
        if board[head[0]][head[1]] == 1:
            eat = 1
        else:
            eat = 0

        # 방향전환
        if len(dir) != 0 and int(dir[0][0]) == time:
            if dir[0][1] == 'D':
                d += 1
                if d == 4:
                    d = 0
            elif dir[0][1] == 'L':
                d -= 1
                if d == -1:
                    d = 3
            dir.popleft()

    print(time)
    return


snake()