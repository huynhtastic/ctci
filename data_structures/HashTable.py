class HashTable():
    def __init__(self):
        self.keys = []
        # TODO: make values a linked list
        self.values = [0] * 10

    def put(self, key, value):
        hkey = hash(key)  # compute hash
        idx = hkey % 10  # compute index to map key to value
        self.keys.append(key)  # TODO: find beter way to store keys
        if self.values[idx] == 0:
            self.values[idx] = [[key, value]]
        else:
            found = False
            for i in range(len(self.values[idx])):
                if (self.values[idx][i][0] == key):
                    self.values[idx][i][1] = value
                    found = True
                    break
            if not found:
                self.values[idx].append((key, value))  # add key/value to map

    def get(self, key):
        hkey = hash(key)
        idx = hkey % 10

        if self.values[idx] != 0:
            for val in self.values[idx]:
                if key == val[0]:  # if the key matches the key stored in this 
                    return val[1]
        raise KeyError('{} is not a valid key in this mapping'.format(key))
