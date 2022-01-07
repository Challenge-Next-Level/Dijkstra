N, D = map(int, input().split())
shortcut = [[] for _ in range(10001)] # 지름길 있는 곳 세팅
for i in range(N):
    start, end, weight = map(int, input().split())
    shortcut[start].append([end, weight])
distance = [d for d in range(D + 1)] # 초기 거리값 설정, d위치는 d만큼의 거리
# 최소 거리를 다익스트라로 갱신
for i in range(D + 1):
    if i != 0: # 현재위치와 이전위치+1 중 최소값을 현재위치로 설정
        distance[i] = min(distance[i], distance[i - 1] + 1)
    for end, weight in shortcut[i]: # 지름길을 보며 최소거리 갱신
        if end <= D and distance[end] > distance[i] + weight:
            distance[end] = distance[i] + weight
print(distance[D])