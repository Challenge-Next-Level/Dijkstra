def idol():
    N, M = input().split()
    N = int(N)
    M = int(M)
    group = {}
    department = {}
    for i in range(int(N)):
        # 걸그룹 이름에 걸그룹 멤버이름을 dict로 생성, 자신의 이름에 자신의 소속을 dict로 생성
        name = input()
        count = input()
        group[name] = []
        for j in range(int(count)):
            girl_name = input()
            group[name].append(girl_name)
            department[girl_name] = name

    for i in range(int(M)):
        answer = input()
        bit = input()
        if int(bit) == 0:
            group[answer].sort()
            for ans in group[answer]:
                print(ans)
        else:
            print(department[answer])

    return


idol()