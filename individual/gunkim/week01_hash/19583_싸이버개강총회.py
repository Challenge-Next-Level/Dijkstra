# https://developeryuseon.tistory.com/90
# input()의 실행시간이 느려 시간초과가 발생했던 문제
import sys

def cyber():
    start, end, stream = input().split()
    start = start.replace(":", "")
    end = end.replace(":", "")
    stream = stream.replace(":", "")

    check_all = {}

    while True:
        try:
            # 아래 입력 부분이 input이 되면 '시간초과'가 발생한다
            time, name = sys.stdin.readline().split()
            time = time.replace(":", "")
            if time <= start:
                check_all[name] = 1
            elif end <= time <= stream and name in check_all:
                check_all[name] += 1
        except:
            break
    cnt = 0
    for i in check_all:
        if check_all[i] >= 2:
            cnt += 1
    print(cnt)
    return


cyber()