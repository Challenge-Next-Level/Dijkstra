# 나의 첫 풀이는 6이 정말 연속으로 3개가 있는 지 판별하는 것을 구현했다
# 하지만 역시 더 쉽고 간편한 풀이가 있었고 그걸로 대체했다
# 그래도 미천한 나의 풀이도 백준에서 통과는 시켜줬었다...ㅎ
def movie_director():
    answer = 666
    number = 1
    num = int(input())
    while number < num:
        answer += 1
        if '666' in str(answer):
            number += 1
    return answer


print(movie_director())