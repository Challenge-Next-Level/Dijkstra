from collections import defaultdict


def solution(genres, plays):
    play_count_by_genre = defaultdict(int)
    songs_in_genre = defaultdict(list)

    for song_id, genre, play in zip(counter(), genres, plays):
        # 장르별로 플레이수를 계속 더해준다(장르별 플레이수 총합)
        play_count_by_genre[genre] += play
        # 나중에 오름차순 sort함수 사용을 위해 minus로 대입(노래마다 플레이수와 index를 기록)
        songs_in_genre[genre].append((-play, song_id))
    # 플레이수에 따라 장르를 정렬한다
    # print(play_count_by_genre['pop']) -> 해당 장르의 value값
    # 위와 같이 value값에 따라 정렬을 하고 key를 정렬하면된다
    genre_in_order = sorted(play_count_by_genre.keys(), key=lambda g: play_count_by_genre[g], reverse=True)

    answer = list()
    for genre in genre_in_order:
        # sorted(songs_in_genre[genre])[:2] 부분은 장르별로 플레이수에 따라 정렬을 하는데 minus값이어서 가장 큰수가 맨 앞으로 정렬됨
        # song_id for minus_play, song_id in 을 통해 song의 index를 받아온다. 앞에서 [:2]를 통해 2개씩만 튜플을 잘라서 2개의 id만 받아옴
        # answer리스트에 extend를 통해 리스트 값을 추가한다
        answer.extend([song_id for minus_play, song_id in sorted(songs_in_genre[genre])[:2]])

    return answer


# counter라는 이름의 제너레이터
def counter():
    i = 0
    while True:
        # yield를 사용하여 값을 바깥으로 전달해주고 대기상태로 들어갔다가 다음 제네러이터 실행시 다시 동작한다
        yield i
        i += 1