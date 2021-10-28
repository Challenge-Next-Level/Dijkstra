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

