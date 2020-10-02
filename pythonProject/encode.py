def duplicate_encode(word):
    word = word.lower()
    lst = [str(i) for i in word]
    res = []
    for x in range(0, len(lst)):
        if word.count(lst[x]) > 1:
            res.append(")")
        else:
            res.append("(")
    print("".join(res))


duplicate_encode("(( @")

