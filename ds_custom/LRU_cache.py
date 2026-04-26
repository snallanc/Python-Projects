from collections import OrderedDict

# popitem(last=...) quick reference:
#
# | last=      | Pops from | Order     | Use case        |
# |------------|-----------|-----------|-----------------|
# | False      | Front     | LRU first | Cache eviction  |
# | True (def) | Back      | MRU first | History / undo  |
#
# Memory aid: last=True → pops the *last* inserted/accessed → MRU

class LRUCache:
    def __init__(self, cache_size):
        self.cache = OrderedDict()
        self.cache_size = cache_size
    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    def put(self,key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.cache_size:
            # Pops the LRU item from the cache
            print("Cache size exceeded. Removing least recently used item: {0}".format(self.cache.popitem(last=False)))
    def print_cache(self):
        print(self.cache)
    def pop_cache(self):
        return self.cache.popitem(last=False)


# Test code
process_list = ["curl", "rpcbind", "wget", "netstat", "tcpdump", "wireshark"]
cache_size = 3
lru_cache = LRUCache(cache_size)
for i in range(cache_size):
    lru_cache.put(i+1, process_list[i])
    lru_cache.print_cache()
for i in range(cache_size):
    lru_cache.get(i+1)
for i in range(cache_size):
    print("popped {0}".format(lru_cache.pop_cache()))
