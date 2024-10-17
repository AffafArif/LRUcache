class DoubleLinkedListNode:
    def __init__(self, key=None, value=None, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

class LRUCache:
    def __init__(self, capacity):
        self.capacity = min(capacity, 50)  # Ensure capacity does not exceed 50
        self.cache = {}
        self.head = None
        self.tail = None

    def add_node_to_head(self, node):
        if self.head:
            node.next = self.head
            self.head.prev = node
            self.head = node
        else:
            self.head = self.tail = node

    def remove_node(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_node_to_head(node)

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.move_to_head(node)
            return node.value
        else:
            return -1

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)
        else:
            if len(self.cache) >= self.capacity:
                del self.cache[self.tail.key]
                self.remove_node(self.tail)

            new_node = DoubleLinkedListNode(key, value)
            self.cache[key] = new_node
            self.add_node_to_head(new_node)

    def display(self):
        current = self.head
        while current:
            print(f"({current.key}: {current.value})", end=" -> ")
            current = current.next
        print("None")

def fill_cache_with_primes(cache):
    for num in range(101):  # Range up to 100
        if is_prime(num):
            cache.put(num, num)

def MissRate(cache, keys):
    misses = 0
    total_requests = len(keys)

    for key in keys:
        if cache.get(key) == -1:
            misses += 1

    miss_rate = misses / total_requests
    return miss_rate


if __name__ == '__main__':
    MAX_CAPACITY = 50
    MAX_KEY = 100
    MAX_VALUE = 100

    lru_cache = LRUCache(MAX_CAPACITY)

    # Fill the cache with keys 0-49
    for key in range(MAX_CAPACITY):
        lru_cache.put(key, key)
    print("Cache after filling with keys 0-49:")
    lru_cache.display()

    # Retrieve the odd number key values
    odd_keys = [key for key in range(1, MAX_CAPACITY * 2, 2)]
    miss_rate_odd_keys = MissRate(lru_cache, odd_keys)
    print(f"Miss Rate after retrieving odd number key values: {miss_rate_odd_keys:.2%}")
    print("Cache after retrieving odd number key values:")
    lru_cache.display()

    # Fill the cache with prime number keys 0-100
    fill_cache_with_primes(lru_cache)
    print("Cache after filling with prime number keys 0-100:")
    lru_cache.display()

    # Compute the final miss rate
    final_miss_rate = MissRate(lru_cache, range(MAX_KEY + 1))
    print(f"Final Miss Rate: {final_miss_rate:.2%}")
    print("Cache after all operations:")
    lru_cache.display()