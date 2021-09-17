# https://docs.python.org/ko/3/library/collections.html
import collections


def solution(participant, completion):

    p = collections.Counter(participant)
    c = collections.Counter(completion)
    # wrapper = collections.UserDict(p)
    # print(wrapper)
    res = p - c
    answer = list(res)[0]
    return answer


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

print(solution(participant, completion))