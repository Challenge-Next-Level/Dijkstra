# heapq에 크기2의 리스트를 넣어주면 2개의 값을 기준으로 알아서 정렬을 해줄까?
# 나는 첫번째 값만 보고 정렬을 해줄거라 생각해서 일부로 pop전에 한 번더 정렬을 시켜줬는데
# 해주지 않아도 문제는 통과를 했다
import sys
import heapq
# from operator import itemgetter


def abs_heap():
    n = int(sys.stdin.readline())
    heap = []
    for i in range(n):
        num = int(sys.stdin.readline())
        if num == 0:
            if len(heap) == 0:
                print(0)
            else:
                # heap = sorted(heap, key=itemgetter(0, 1))
                answer = heapq.heappop(heap)
                if answer[1] == -1:
                    print(-answer[0])
                else:
                    print(answer[0])
        else:
            if num < 0:
                heapq.heappush(heap, [-num, -1])
            else:
                heapq.heappush(heap, [num, 1])
    return


abs_heap()