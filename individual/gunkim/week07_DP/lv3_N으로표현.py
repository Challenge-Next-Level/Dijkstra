# 아이디어가 떠오르지 않아 답안을 찾아보았는 데 for문이 4개라 dp에 대한 의구심이 들었고 나름의 해결방안이 떠올라 도전을 했었다
# i개를 이용하여 수들을 만들 때 i - 1개를 이용하여 만들었던 수들에 N을 사칙연산을 통해 추가하는 식으로 풀이했다
# 하지만 66 - (6 / 6) 을 통해 65를 4개만에 만드는 풀이는 만들 수 없다는 것을 테스트 케이스 검색을 통해 알아냈다
def solution(N, number):
    if N == number:
        return 1
    # dp 리스트의 쓰임새
    # 1. dp[0]는 완성했던 숫자들을 모두 넣어둔 set 공간
    # 2. dp[x]은 x개의 숫자를 이용해 만들 수 있는 숫자를 넣어둔 공간
    # 예외 처리) dp[x]를 완성시킬 때 dp[0]에 있는 숫자 set을 차집합(dp[x] - dp[0])으로 빼준다. 아래 코드가 있을 것.
    dp = [set([]) for _ in range(9)]

    # 최소 8개를 사용한 경우 까지만 dp를 만든다
    for i in range(1, 9):
        # 1. N을 i개 연속으로 이어붙인 숫자 생성
        dp[i].add(int(str(N) * i))

        # i == 4일 때 4개의 N을 사용하여 수식을 생성해야 한다
        # 이때 i의 갯수가 (1 + 3), (2 + 2), (3 + 1) 일 때 경우를 생각해서 완성하면 된다
        # (1 + 3)이 정확히 무슨 의미냐 하면은 (1개를 사용했을 때 + 3개를 사용했을 때 경우를 서로 사칙연산)을 하면 되는 것이다
        # 하지만 (1 + 3) 과 (3 + 1)은 정확히 같은 결과 값을 도출하기에 (3 + 1)을 수행할 필요가 없다. 따라서 아래와 같이 operand의 범위를 조정해준다
        for operand in range(1, i // 2 + 1):
            # 2. operand와 i - operand 의 경우를 서로 사칙연산하여 숫자 생성
            for op1 in range(len(dp[operand])):
                for op2 in range(len(dp[i - operand])):
                    dp[i].add(dp[operand][op1] + dp[i - operand][op2]) # 덧셈
                    dp[i].add(dp[operand][op1] - dp[i - operand][op2]) # 뺄셈
                    dp[i].add(dp[i - operand][op2] - dp[operand][op1]) # 뺄셈
                    dp[i].add(dp[operand][op1] * dp[i - operand][op2]) # 곱셈
                    # 나눗셈
                    if dp[operand][op1] != 0:
                        dp[i].add(dp[i - operand][op2] // dp[operand][op1])
                    if dp[i - operand][op2] != 0:
                        dp[i].add(dp[operand][op1] // dp[i - operand][op2])
        # 3. 차집합을 이용하여 이전에 만들었던 수는 제거
        dp[i] -= dp[0]
        # 4. number가 있다면 i 반환
        if number in dp[i]:
            return i
        # 새로 생성한 수를 dp[0] set에 추가
        dp[0] |= dp[i]
        dp[i] = list(dp[i])
    # 5. 위 과정을 모두 진행한 후라면 답이 없다는 뜻이니 -1 리턴
    return -1


print(solution(6, 65)) # 4