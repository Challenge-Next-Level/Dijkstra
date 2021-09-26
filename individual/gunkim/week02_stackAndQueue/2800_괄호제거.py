# 콤비네이션을 활용하는 거겠지 생각은 했지만 구현 아이디어는 아예 떠오르지 않음
# enumerate를 이용하여 괄호의 쌍 위치를 저장하는 법이 신선했음
# 쌍위치를 저장한 배열에서 combination을 이용해서 경우의 수를 뽑는 것이 핵심
from itertools import combinations


def del_bracket():
    problem = [*input()]  # 문자열 하나씩 리스트화
    save = []
    pair_index = []
    for i, v in enumerate(problem):
        if v == '(':
            problem[i] = ''
            save.append(i)
        elif v == ')':
            problem[i] = ''
            pair_index.append([save.pop(), i])
    out = set()
    # 위에서 괄호들은 공백처리를 했음
    # 괄호쌍을 선택하는 경우를 콤비네이션으로 생각한다
    for i in range(len(pair_index)):
        for j in combinations(pair_index, i):
            answer = problem[:]
            # 괄호를 넣어준다
            for left, right in j:
                answer[left] = '('
                answer[right] = ')'
            # join은 리스트화 되어있는 문자들을 모두 합쳐 문자열로 만듦
            out.add(''.join(answer))
    for i in sorted(out):
        print(i)
    return


del_bracket()