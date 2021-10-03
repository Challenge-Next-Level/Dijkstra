# 시간초과 무덤 수준의 문제이다
# 기본적으로 아이디어를 생각하는 것도 어려움
# 구현을 했더라고 시간 때문에 애를 엄청 먹는다. python3 실행환경에서 100%찍고도 시간초과가 발생
# 결국에 pypy3로 돌려 성공했다
# 시간을 조금이라도 줄였던 방법들
# 1. len(list) == 0이 아닌 list로도 empty여부 확인 가능
# 2. enumerate로 i, v 값을 확인하려 했는데 이것도 시간을 잡아먹는 이유 같다
# 3. for문 마다 print 사용하는 것도 시간을 쓰는 것 같음
import sys
from collections import deque


N, L = map(int, sys.stdin.readline().split())
problem = list(map(int, sys.stdin.readline().split()))
save = deque()
answer = [0 for _ in range(N)]
for i in range(N):
    while save and save[0][0] <= i - L:
        save.popleft()
    while save and save[-1][1] > problem[i]:
        save.pop()
    save.append([i, problem[i]])
    answer[i] = save[0][1]
print(*answer)
