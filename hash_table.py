class HashTable:
    def __init__(self, size=101):
        self.size = size
        self.table = [None]* size


    def _hash(self, key):
        return key % self.size


    def put(self, key, value):
        index = self._hash(key)

        if self.table[index] is None:
            self.table[index] = []

        for i, (k,v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key,value))


    def get(self, key):
        index = self._hash(key)

        if self.table[index] is None:
            return None

        for k,v in self.table[index]:
            if k == key:
                return v

        return None


    def delete(self, key):
        index = self._hash(key)

        if self.table[index] is None:
            return False
        
        for i, (k,v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
            
        return False
    