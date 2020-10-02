def descending_order(num):
    lst = sorted(str(num), reverse=True)
    res = int("".join(lst))
    print(res)


def main():
    descending_order(123456789)


main()