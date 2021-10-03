# 알코올이 낮은 것부터 먹어야 되는 것부터 몰랐음... 먹은 맥주는 선호도 기준으로 최소힙에 저장
# 맥주들을 sorted의 key함수로 정렬. 이때 당연히 1.알코올 2.선호도 기준으로 정렬
# lambda는 제일 잘 알려진 기초 정렬. operator모듈 함수의 itemgetter이란 것들을 이용시 간단, 빠르게 작성 가능
import sys
import heapq
# from operator import itemgetter


def beer():
    N, M, K = map(int, sys.stdin.readline().split())
    # 맥주 K개 입력. 이때 알코올 기준으로 최소힙 정렬
    beer = []
    for i in range(K):
        beer.append(list(map(int, sys.stdin.readline().split())))
    beers = sorted(beer, key=lambda x: (x[1], x[0]))
    # 아래는 itemgetter를 이용한 것. 위 결과와 같은 결과로 정렬을 한다
    # item = sorted(beer, key=itemgetter(1, 0))

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