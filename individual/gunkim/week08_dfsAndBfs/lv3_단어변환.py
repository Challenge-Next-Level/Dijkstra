# 처음 조건에 대한 생각이 필요했음. 무턱대고 탐색을 진행하면 분명 무한 루프에 빠질 것이기 때문
# 1. break문에 대한 조건이 필요: words에 있는 단어를 모두 탐색하는 경우는 불가한 경우가 되기 때문에 이때를 리턴
# 2. 불필요한 탐색 줄이기: 탐색을 했던 word는 visit에 저장
def solution(begin, target, words):
    answer = 100
    # 한 번 거쳐간 단어는 다시 탐색할 필요가 없기 때문에 visit 배열 생성
    visit = []
    length = len(words)
    # target이 words안에 없다면 완성 불가
    if target not in words:
        return 0

    def dfs(cur_word, depth):
        # words에 있는 모든 단어를 탐색했는데 완성하지 못했다면 리턴
        if depth >= length:
            return
        # target을 만들었다면 answer 값 계산
        if cur_word == target:
            nonlocal answer
            answer = min(answer, depth)
            return
        # 1. words에 있는 단어에서 탐색
        # 2. 탐색하는 단어는 이전에 visit한 적이 없어야 함
        # 3. 탐색하는 단어는 현재 단어와 한 글자만 달라야 함
        # 4. 조건을 만족하면 dfs 진행
        for i in range(length):
            if words[i] not in visit:
                count = 0
                for j in range(len(words[i])):
                    if cur_word[j] != words[i][j]:
                        count += 1
                if count == 1:
                    visit.append(words[i])
                    dfs(words[i], depth + 1)
                    visit.pop()
        return

    dfs(begin, 0)
    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))