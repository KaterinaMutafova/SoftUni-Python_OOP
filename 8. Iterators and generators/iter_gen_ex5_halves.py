def solution():
    def integers():
        current = 1
        while True:
            yield current
            current += 1

    # TODO: Implement

    def halves():
        for i in integers():
            yield i / 2

    # TODO: Implement

    def take(n, seq):
        nums = []
        for i in seq:
            if len(nums) == n:
                return nums
            nums.append(i)


    # TODO: Implement

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))

