def parking_lot():
    N, M = input().split()
    fee = []
    weight = []
    ining = []
    answer = 0
    # 주차요금
    for i in range(int(N)):
        fee.append(int(input()))
    space = [-1 for i in range(int(N))]
    # 차의무게
    for i in range(int(M)):
        weight.append(int(input()))
    # 주차장을 오가는 차들의 순서
    # 요금은 시간이 아닌 주차요금*차의무게
    for i in range(2 * int(M)):
        num = int(input())
        # 음수값은 출차
        if num < 0:
            num *= -1
            num -= 1
            s_idx = 0
            for j in space:
                if j == num:
                    break
                s_idx += 1
            answer += fee[s_idx] * weight[num]
            space[s_idx] = -1
        # 양수값은 주차해야할 차량(대기차량)
        else:
            ining.append(num)
        # 주차장 공간이 있다면 주차
        while -1 in space and len(ining):
            idx = 0
            for j in space:
                if j == -1:
                    break
                idx += 1
            space[idx] = ining.pop(0) - 1
    print(answer)
    return


parking_lot()