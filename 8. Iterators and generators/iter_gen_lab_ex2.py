class reverse_iter:
    def __init__(self, iterator):
        self.iterator = iterator
        self.i = len(iterator)

    def __iter__(self):
        return self

    def __next__(self):
        self.i -= 1
        if self.i >= 0:
            return self.iterator[self.i]
        raise StopIteration





reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)


