# 사실 다른 풀이(for문 2개 사용)로 통과는 했었다
# 그런데 for문 하나라도 풀 수 있다는 것을 보게 되어 수정하게 되었다.
# 하나의 for문 안에 문제의 조건문을 하나 걸어 만족시 반환을 하면 되었다.
# 너무 단순하지만 내겐 너무 어려웠던 센스 있는 조건문이었다
def solution(citations):
    length = len(citations)
    s = sorted(citations)
    # 적게 인용된 논문 부터 올라가면서 '인용된 횟수 값'이 '그 횟수만큼 인용된 논문 갯수 이상'이 되었을 때 return
    for i in range(length):
        if s[i] >= length - i:
            return length - i
    return 0


c = [3, 0, 6, 1, 5]
print(solution(c))