VOWELS = {"a", "i", "u", "e", "o"}

def vowel_filter(function):

    def wrapper():
        res = function()
        return [char for char in res if char in VOWELS]


    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
