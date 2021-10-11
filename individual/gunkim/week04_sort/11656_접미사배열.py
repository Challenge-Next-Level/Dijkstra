def suffix_arr():
    suf = input()
    length = len(suf)
    answer = []
    for i in range(length):
        answer.append(suf[i:length])
    answer.sort()
    for i in answer:
        print(i)
    return


suffix_arr()