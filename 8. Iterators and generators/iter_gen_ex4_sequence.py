class sequence_repeat:
    def __init__(self, seq, number):
        self.seq = seq
        self.number = number
        self.index = 0
        self.length = len(seq)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == self.number:
            raise  StopIteration
        if self.index == self.length:
            self.index = 0
        temp = self.seq[self.index]
        self.index += 1
        self.count += 1
        return temp







result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

