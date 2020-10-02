import itertools

wallet = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

count = 0
for i in range(1, len(wallet)):
    #money_set = {itertools.combinations(wallet, i)}
    money_set = set(itertools.combinations(wallet, i))
    for option in money_set:
        
        if sum(option) == 100:
            print(option)
            count += 1


print(count)
