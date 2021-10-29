# set을 이용해서 합집합, 교집합을 구할 수 있다! '|' == 합집합, '&' == 교집합 을 의미한다!
# (1) 소수 판별시 제곱근 까지만 비교하는 이유 정리하기
# (2) 에라토스테네스의 체는 무엇이고 언제 사용하는지 정리하기
from itertools import permutations
from math import sqrt


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    num_list = set()
    # 만들 수 있는 숫자들의 경우를 순열로 뽑는다
    for i in range(len(numbers)):
        num = map(int, map(''.join, permutations(numbers, i + 1)))
        num_list |= set(num)
    num_list = list(num_list)
    # 뽑은 숫자들에 대해 소수 판별
    for i in range(len(num_list)):
        if is_prime(num_list[i]):
            answer += 1
    return answer


n = "011"
print(solution(n))

