from numpy import ndarray
class HashTable:
    pass

    def __init__(self, size=53):
        self.keymap = []
        for val in range(0, size):
            self.keymap.append([])

    

    def hash(self, key):
        total = 0
        weird_prime = 31
        for val in range(0, min(len(key), 100)):
            char = key[val]
            value = ord(char) - 96
            total = (total*weird_prime + value) % len(self.keymap)
        return total
    
    def set(self, key, val):
        new_key = self.hash(key)
        self.keymap[new_key].append([key, val])
    
    def get(self, key):
        new_key = self.hash(key)
        values = self.keymap[new_key]
        for val in values:
            if val[0] == key:
                return val[1]
        return None
    
    def keys(self):
        arr = []
        for array in self.keymap:
            for val in array:
                arr.append(val[0])
        return arr
    
    def values(self):
        arr = []
        for array in self.keymap:
            for val in array:
                arr.append(val[1])
        arr = set(arr)
        return arr
    
    def print(self):
        print(self.keymap)




this = HashTable()
this.set('pink', 55)
this.set('red', 32)
this.set('yellow', 12)
this.set('blue', 45)
this.set('orange', 235)
this.set('green', 345)
this.set('black', 345)
this.set('maroon', 62)
this.set('lavender', 67)
print(this.get('pink'))
this.print()
this.set('are we done', 'yes')
print(this.get('are we done'))
print(this.keys())
print(this.values())