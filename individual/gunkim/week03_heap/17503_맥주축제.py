# 알코올이 낮은 것부터 먹어야 되는 것부터 몰랐음...
# 맥주들을 sorted로 정렬을 하는데 무슨 의미인지 찾아봐야 할듯
import sys
import heapq


def beer():
    N, M, K = map(int, sys.stdin.readline().split())
    heap_beer = []
    # 맥주 K개 입력. 이때 알코올 기준으로 최소힙 정렬
    beer = []
    for i in range(K):
        beer.append(list(map(int, sys.stdin.readline().split())))
    beers = sorted(beer, key=lambda x: (x[1], x[0]))

    favorite = 0
    drink_fav = []
    liver = 0
    # 알코올이 낮은 맥주부터 마신다
    for b in beers:
        favorite += b[0]
        heapq.heappush(drink_fav, b[0])
        if len(drink_fav) == N:
            if favorite >= M:
                liver = b[1]
                break
            else:
                favorite -= heapq.heappop(drink_fav)
    if favorite < M:
        return -1
    return liver


print(beer())