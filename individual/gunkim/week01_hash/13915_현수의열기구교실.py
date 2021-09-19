def research():
    while True:
        try:
            N = input()
            ans = []
            for i in range(int(N)):
                num = input()
                num_list = []
                for j in num:
                    if j not in num_list:
                        num_list.append(j)
                num_list.sort()
                if num_list not in ans:
                    ans.append(num_list)
            print(len(ans))
        except:
            break

research()