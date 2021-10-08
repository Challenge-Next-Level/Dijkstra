# 처음에 permutation을 이용해서 모든 경우에 대한 숫자를 비교하여 max값을 찾으려 했다.
# 그러나 그 경우를 다 비교한다는 것은 시간초과를 도래했다.
# 입력되는 숫자의 값은 1000이하라는 것을 착안하여 모든 숫자를 3자리수 이상으로 만든 후 비교를 하면 된다는 아이디어를 찾았다
# 너무 훌륭한 아이디어인 것 같다...
def solution(numbers):
    answer = ''
    # 뒤에서 정렬할 때, join할 때 모두 문자열 비교가 편하여 형변환
    to_str = list(map(str, numbers))
    # 인자로 있는 문자열을 3번 반복하여 만든 문자열로 비교
    to_str.sort(key=lambda x: x * 3, reverse=True)
    # 숫자 앞이 0으로 시작하면 안되니 int로 한 번 형변환
    answer = int(''.join(to_str))
    return str(answer)


n = [6, 10, 2]
solution(n)