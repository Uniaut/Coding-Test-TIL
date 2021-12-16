class LinkNode:
    def __init__(self, key, value):
        self.next_node = None
        self.key = key
        self.value = value
            

class HashTable:
    def __init__(self, hash_func=hash, bucket_size=10):
        self.hash_func = hash_func
        self.bucket_size = bucket_size
        self.table = [None] * bucket_size
    

    def __setitem__(self, key, value):
        bucket_index = hash(key) % self.bucket_size
        node = self.table[bucket_index]
        if node is None:
            self.table[bucket_index] = LinkNode(key, value)
            return None
        
        prev = node
        node = node.next_node
        while node is not None:
            if node.key == key:
                node.value = value
                break
            else:
                node = node.next_node
        else:
            prev.next_node = LinkNode(key, value)
            return None

    def __getitem__(self, key):
        bucket_index = hash(key) % self.bucket_size
        node = self.table[bucket_index]
        while node is not None:
            if node.key == key:
                return node.value
            else:
                node = node.next_node
        else:
            raise Exception('No item')

a = HashTable(bucket_size=10)
for i in range(100):
    a[i] = 100 - i

for i in range(10):
    print(a[i])

a['james'] = 'cash'
print(a['james'])