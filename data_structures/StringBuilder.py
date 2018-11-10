class StringBuilder():
    def __init__(self):
        # Python doesn't have a fixed-length array, so we just use list
        self.strings = []

    def append(self, word):
        self.strings.append(word)

    def to_string(self):
        return ''.join(self.strings)

    def __str__(self):
        return self.to_string()
