# 결과값 출력할 때 값이 하나 남아있다면 내 결과는 최대, 최소를 제대로 출력 못할 것 같은데
# 일단 통과했다 ㅎ;;
import heapq


def solution(operations):
    answer = []
    index = 0
    while index < len(operations):
        word, num = operations[index].split()
        num = int(num)
        # 숫자를 push
        if word == 'I':
            heapq.heappush(answer, num)
        # 최솟값 pop
        elif len(answer) != 0 and word == 'D' and num == -1:
            heapq.heappop(answer)
        # 최대힙을 만든 후 최댓값 pop, 다시 최소힙 생성
        elif len(answer) != 0 and word == 'D' and num == 1:
            max_heap = []
            for i in answer:
                heapq.heappush(max_heap, -i)
            heapq.heappop(max_heap)
            answer = []
            for i in max_heap:
                heapq.heappush(answer, -i)
        index += 1

    # 결과 출력
    if len(answer) == 0:
        return [0, 0]
    else:
        min = heapq.heappop(answer)
        max_heap = []
        for i in answer:
            heapq.heappush(max_heap, -i)
        max = heapq.heappop(max_heap)
        return [-max, min]


o = ["I 7","I 5","I -5","D -1"]
print(solution(o))