N, K = list(map(int, input().split()))
bottle = []
for i in range(N):
    bottle.append(int(input()))
# 이분 탐색 시작
left, right = 0, max(bottle)
answer = 0
while left <= right:
    mid = (left + right) // 2
    people = 0
    for b in bottle: # 병 마다 따를 수 있는 잔의 수 추가
        people += b // mid
    # left, right 값 조절
    if people < K:
        right = mid - 1
    else:
        left = mid + 1
        answer = max(answer, mid)
print(answer)