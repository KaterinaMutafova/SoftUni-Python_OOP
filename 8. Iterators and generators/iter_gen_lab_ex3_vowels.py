class vowels:
    def __init__(self, string_word):
        self.string_word = string_word
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.i < len(self.string_word):
            current_char = self.string_word[self.i]
            self.i += 1
            if self.is_vowel(current_char):
                return current_char
        raise StopIteration

    @staticmethod
    def is_vowel(c):
        vowels = "aeiuyo"

        return c.lower() in vowels




my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
