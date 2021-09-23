def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0 for i in range(bridge_length)]
    while len(truck_weights) != 0:
        # 다리에서 pop
        bridge.pop(0)
        # 트럭 or 0 추가
        if sum(bridge) + truck_weights[0] <= weight:
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)
        time += 1
    time += len(bridge)
    return time


bl = 2
w = 10
tw = [7,4,5,6]
print(solution(bl, w, tw))