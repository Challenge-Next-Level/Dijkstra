def dfs(idx, now, name, cnt):
    # 문자 최소 횟수 변경
    if now[idx] != name[idx]:
        count = ord(name[idx]) - ord(now[idx])
        if count > 13:
            count = 91 - ord(name[idx])
        cnt += count
        now = now[:idx] + name[idx] + now[idx + 1:]
    # 문자열이 완성되었다면 리턴
    if now == name:
        global result
        result = min(result, cnt)
        return

    # 왼쪽 or 오른쪽 진행
    left, right = 0, 0
    left_idx, right_idx = idx, idx
    while True:
        left_idx -= 1
        left += 1
        if left_idx < 0:
            left_idx = len(now) - 1
        if now[left_idx] != name[left_idx]:
            break
    while True:
        right_idx += 1
        right += 1
        if right_idx >= len(now):
            right_idx = 0
        if now[right_idx] != name[right_idx]:
            break
    if left == right:
        dfs(left_idx, now, name, cnt + left)
        dfs(right_idx, now, name, cnt + right)
    elif left < right:
        dfs(left_idx, now, name, cnt + left)
    else:
        dfs(right_idx, now, name, cnt + right)
    return


def solution(name):
    # A로 이루어진 첫 문자열 생성
    start = ''.join(['A' for _ in range(len(name))])
    dfs(0, start, name, 0)
    return result


n = "JEROEN"
result = 99999
print(solution(n))