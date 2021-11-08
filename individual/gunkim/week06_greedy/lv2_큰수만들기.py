# 처음 풀이는 조합을 사용했다.
# 하지만 입력값은 백만 이하의 수이기 때문에 수가 클 때 조합의 경우가 너무 많이 발생하여 시간초과가 발생했다.
def solution(number, k):
    # stack 용도로 생성
    answer = []
    # stack에 숫자를 넣으면서 stack의 top값이 넣어야하는 숫자보다 작다면 pop
    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
    # 예외 처리
    # 위 조건에서 k가 0이 되지 않고 끝이 날 수 있다. 따라서 맨 뒤에서 부터 k개의 숫자를 없앤다.
    return ''.join(answer[:len(answer) - k])


n = "4177252841"
K = 4
print(solution(n, K))