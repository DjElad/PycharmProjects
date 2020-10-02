numbers = iter(list(range(1, 101)))
# print every 3rd num
for i in numbers:
    next(numbers)
    next(numbers)
    print(i)