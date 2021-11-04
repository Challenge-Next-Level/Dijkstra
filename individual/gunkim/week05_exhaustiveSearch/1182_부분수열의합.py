def dfs(idx, num):
    global N, S, seq
    if idx >= N:
        return
    num += seq[idx]
    if num == S:
        global answer
        answer += 1
    dfs(idx + 1, num - seq[idx])
    dfs(idx + 1, num)


N, S = map(int, input().split())
seq = list(map(int, input().split()))
answer = 0
dfs(0, 0)
print(answer)