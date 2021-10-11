# 수학적인 생각이 좋아야 하는 문제. 나에겐 너무 어려웠다
# 양의 정수는 1부터 시작을 하니 num = 1 시작
# 오른차순 순으로 '추들의 무게'를 'num'과 비교한다
# num은 추의 무게 이상의 값을 갖고 있으면 'num + 비교한 추 - 1'의 무게 까지 측정을 할 수 있다
import sys


def scale():
    N = int(input())
    weight = list(map(int, sys.stdin.readline().split()))
    weight = sorted(weight)
    num = 1
    for i in range(N):
        if num < weight[i]:
            break
        num += weight[i]
    print(num)
    return


scale()