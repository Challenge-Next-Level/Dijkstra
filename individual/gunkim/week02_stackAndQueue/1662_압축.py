def zip(length, stack):
    # 스택을 모두 pop할 때까지
    while stack:
        top = stack.pop()
        # )일 때는 재귀
        if top == ')':
            length += zip(0, stack)
        # (일 때는 앞 숫자와 length를 곱
        elif top == '(':
            length *= int(stack.pop())
            return length
        # 그냥 숫자일 때는 length++
        else:
            length += 1
    return length


str = input()
stack = list(str)
print(zip(0, stack))