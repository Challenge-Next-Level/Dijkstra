# 문자에 해당하는 값이 A, B, C...에 대해 순서대로 나오는게 아닌 줄 알았는데 순서대로 입력이 되는 거였음
# 순서대로 입력이 되는거니 ord()를 쓰는게 신선한 아이디어 었음
# 반복문 한 번으로 해결을 하던데... 문자를 만나면 숫자를 stack에 push, 연산자를 만나면 stack에서 값 2개를 pop하여 계산
# 정말 좋은 아이디어인 것 같음. stack 문제가 생각보다 아이디어가 번뜩여야 하는 듯
from collections import deque


def postfix_notation():
    N = int(input())
    str = input()

    value = deque()
    for i in range(N):
        value.append(int(input()))

    stack = []
    for ch in str:
        # 문자이면
        if ch.isupper():
            # A라면 value의 65 - 65 = 0 번째 index값을 append
            stack.append(value[ord(ch) - ord('A')])
        # 연산자이면
        else:
            # 바로 이전에 추가되었던 숫자 2개를 pop
            # 계산결과는 다시 append
            num2 = stack.pop()
            num1 = stack.pop()
            if ch == '+':
                stack.append(num1 + num2)
            elif ch == '-':
                stack.append(num1 - num2)
            elif ch == '/':
                stack.append(num1 / num2)
            elif ch == '*':
                stack.append(num1 * num2)
    print(format(stack[0], '.2f'))
    return


postfix_notation()