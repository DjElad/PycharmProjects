def find_outlier(integers):
    count_even = 0
    count_odd = 0
    for i in integers:
        if i % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    print(count_odd)
    print(count_even)

    if count_odd > count_even:
        for x in integers:
            if x % 2 == 0:
                return x
    elif count_odd < count_even:
        for x in integers:
            if x % 2 != 0:
                return x
    else:
        return "how"


print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))


