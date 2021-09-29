from collections import Counter
N = 0;

while True:
    try:
        N = int(input());
        result = 0;
        std_list = [];
        for n in range(N):
            std = sorted(Counter(input()).keys());
            print(std)
            if std not in std_list:
                std_list.append((std));
        print(len(std_list));
    except:
        break
