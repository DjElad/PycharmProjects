
def array_diff(a, b):
    a = [y for y in a if y not in b]
    return a


print(array_diff([2, 1, 2, 3, 3, 2, 3], [2, 3]))
