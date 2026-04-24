class HashTable:
    def __init__(self):
        self.collection={}

    def validate_key(self, key):
        if not isinstance(key, str):
            raise TypeError('The key should be a string.')
        
        return key
    
    def hash(self, key):
        self.validate_key(key)
        
        ascii_codes=tuple(map(lambda x: ord(x), key))
        hashed_key=sum(ascii_codes)

        return hashed_key
        
    def add(self, key, value):
        hashed_key=self.hash(key)


        if self.collection.get(hashed_key, False):
            self.collection[hashed_key][key]=value
            return

        self.collection[hashed_key]={key: value}

    def remove(self, key):
        self.validate_key(key)

        hashed_key=self.hash(key)

        values=self.collection.get(hashed_key, None)

        if not values: return

        if values.get(key, None):
            del values[key]
        
        return

    def lookup(self, key):
        self.validate_key(key)

        hashed_key=self.hash(key)

        values=self.collection.get(hashed_key, None)

        if not values: return

        value=values.get(key, None)
        return value

def main():
    ht=HashTable()

    ht.add('Guilherme', 'Nininho')
    ht.add('Fábio', 'Pabio')

    ht.add('xxxxxddb ', 'success')
    print(ht.collection)

    print(ht.remove('xxxxxddb '))
    print(ht.remove('Guilherme'))
    print(ht.collection)

    print(ht.lookup('xxxxxddb '))


main()