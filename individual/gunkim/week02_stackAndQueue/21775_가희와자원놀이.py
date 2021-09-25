# 입력 데이터의 크기가 매우 커서 시간초과가 계속 발생했음
# 논리적으로는 맞게 구현했기에 "필요없는 구현을 덜어내야 했음"
# release는 유저가 해당 숫자를 가지고 있지 않다면 발생하지 않는 상황임
# 따라서 "유저가 어떤 숫자를 갖고있는지에 대한 데이터는 필요가 없음"
# 그저 공용 공간에 숫자가 있는지 없는지만 알면됨
import sys
from collections import deque
input = sys.stdin.readline


def play():
    N, T = map(int, input().split())
    turn = list(map(int, input().split()))
    dummy = deque()
    player_hand = [[] for i in range(N)]

    # 누군가가 카드를 가져갔다면 used_card에 추가
    used_card = set()

    for i in range(T):
        dummy.append(input().split())
    for i in turn:
        num = i - 1
        # 카드가 없다면 드로우
        if len(player_hand[num]) == 0:
            player_hand[num] = dummy.popleft()
            if player_hand[num][1] == 'next':
                sys.stdout.write(player_hand[num][0]+'\n')
                player_hand[num] = []
            elif player_hand[num][1] == 'release':
                sys.stdout.write(player_hand[num][0]+'\n')
                used_card.remove(int(player_hand[num][2]))
                player_hand[num] = []
        # 카드가 있다면 사용(있다면 acquire임 무조건)
        if len(player_hand[num]):
            sys.stdout.write(player_hand[num][0] + '\n')
            target_num = int(player_hand[num][2])
            if target_num not in used_card:
                used_card.add(target_num)
                player_hand[num] = []


play()