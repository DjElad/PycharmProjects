class MusicNotes:

    def __init__(self):
        self.notes = [55, 61.74, 65.41, 73.42, 82.41, 87.31, 98]
        self.notes_index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.notes_index >= len(self.notes) - 1:
            raise StopIteration()
        mult = 1
        for i in range(0, 5):
            for x in range(0, 7):
                self.notes_index += 1
                print(self.notes[self.notes_index] * mult)
            self.notes_index = -1
            mult *= 2
        self.notes_index = 7
        return "fuuuuuck"


notes_iter = MusicNotes()

for freq in notes_iter:
    print(freq)
