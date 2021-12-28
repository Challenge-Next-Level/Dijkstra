N = int(input())
have = list(map(int, input().split()))
M = int(input())
question = list(map(int, input().split()))
# 이분 탐색을 위해 정렬
have.sort()
answer = [0] * len(question) # 답을 저장하는 리스트
length = len(have) - 1
# 각 숫자를 갖고 있는지 검사
for i in range(len(question)):
    left, right = 0, length # have 리스트의 index 값을 저장
    # 이분 탐색
    while left <= right:
        mid = (left + right) // 2
        if question[i] < have[mid]:
            right = mid - 1
        elif question[i] > have[mid]:
            left = mid + 1
        else: # 갖고 있다면 answer 수정 및 break
            answer[i] = 1
            break
print(' '.join(map(str, answer)))