def solution(phone_book):
    phone_book.sort()
    # for p1, p2 in zip(phone_book, phone_book[1:]):
    #     print(p1, p2)
        # if p2.startswith(p1):
        #     return False

    for i in range(0, len(phone_book) - 1):
        length = len(phone_book[i])
        if len(phone_book[i + 1]) >= length:
            word = phone_book[i + 1][0:length]
            if phone_book[i] == word:
                return False
    return True

pb = ["12","123","1235","567","88"]
print(solution(pb))