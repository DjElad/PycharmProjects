def check_id_valid(id_number):
    is_valid = [int(i) for i in str(id_number)]
    for x in range(9):
        if x % 2 != 0:
            is_valid[x] *= 2
            if len(str(is_valid[x])) == 2:
                is_valid[x] = int((is_valid[x] / 10) + (is_valid[x] % 10))

    if sum(is_valid) % 10 == 0:
        return True
    return False


print(check_id_valid(123456782))


class IDIterator:

    def __init__(self, _id):
        self._id = _id
        self.iterator = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.iterator >= 11:
            raise StopIteration()

        while self.iterator < 10:
            self._id += 1
            if check_id_valid(self._id):
                self.iterator += 1
                return self._id
        self.iterator = 11


def id_gen(id_number):
    for i in range(id_number, 999999999):
        if check_id_valid(i):
            yield i


def main():
    the_gen = id_gen(123456780)
    for x in range(10):
        print(next(the_gen))

        
main()


check = IDIterator(123456780)
for y in check:
    print(y)