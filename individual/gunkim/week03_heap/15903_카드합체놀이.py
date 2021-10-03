import sys
import heapq


def card_comb_play():
    n, m = map(int, sys.stdin.readline().split())
    card = list(map(int, sys.stdin.readline().split()))
    cards = []
    for i in card:
        heapq.heappush(cards, i)

    for i in range(m):
        a = heapq.heappop(cards)
        b = heapq.heappop(cards)
        c = a + b
        heapq.heappush(cards, c)
        heapq.heappush(cards, c)
    answer = 0
    for i in cards:
        answer += i

    return answer


print(card_comb_play())