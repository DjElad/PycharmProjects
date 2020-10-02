def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
            else:
                return True
    else:
        return False


def first_prime_over(n):
    if n == 1:
        return 3
    result = (i for i in range(n+1, n**10) if is_prime(i))
    return next(result)


print(first_prime_over(1))


