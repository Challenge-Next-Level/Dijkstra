def girl_group():
    N, M = input().split()
    N = int(N)
    M = int(M)

    kpop_dict = {}

    for n in range(N):
        members=[]
        singer = input()
        number = int(input())
        for num in range(number):
            members.append(input())
        kpop_dict[singer]=sorted(members)

    for m in range(M):
        m1 = input()
        m2 = int(input())
        if m2 == 0:
            print(*kpop_dict[m1], sep = "\n")
        else:
            for s in kpop_dict.keys():
                if m1 in kpop_dict[s]:
                    print(s);

girl_group()
