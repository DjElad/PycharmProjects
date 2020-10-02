def persistence(n):
    count = 0
    pers = 1
    length = len(str(n))
    while length > 1:
        last = int(n % 10)
        pers *= last
        for i in range(1, length):
            next_d = int((n / 10) % 10)
            pers *= next_d
            count += 1
            n = int(n / 10)
    return count


print(persistence(999))