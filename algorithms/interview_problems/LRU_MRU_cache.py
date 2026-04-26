from collections import OrderedDict

# popitem(last=...) quick reference:
#
# | last=      | Pops from | Order     | Use case        |
# |------------|-----------|-----------|-----------------|
# | False      | Front     | LRU first | Cache eviction  |
# | True (def) | Back      | MRU first | History / undo  |
#
# Memory aid: last=True → pops the *last* inserted/accessed → MRU

class Cache:
    def __init__(self, cache_size, mru=False):
        self.cache = OrderedDict()
        self.cache_size = cache_size
        self.mru = mru  # True = evict MRU, False = evict LRU

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
            return
        self.cache[key] = value
        if len(self.cache) > self.cache_size:
            evicted = self.evict()
            print("Cache size exceeded. Removing item: {0} as per {1}".format(evicted, self.evict_policy()))

    def evict_policy(self):
        return "MRU eviction policy" if self.mru else "LRU eviction policy"

    def evict(self):
        # mru=True  → evict from back  (most recently used)
        # mru=False → evict from front (least recently used)
        return self.cache.popitem(last=self.mru)

    def print_cache(self, indent=0):
        print(" " * indent + str(self.cache))
    
    def get_cache_size(self):
        return self.cache_size


def LRUCache(cache_size): return Cache(cache_size, mru=False)
def MRUCache(cache_size): return Cache(cache_size, mru=True)


# Test code
if __name__ == "__main__":
    process_list = ["curl", "rpcbind", "wget", "netstat", "tcpdump", "wireshark"]
    cache_size = 5

    def common_put_func(cache):
        for i in range(cache_size):
            cache.put(i+1, process_list[i])
        print("Cache after adding {} items:".format(cache_size))
        cache.print_cache(2)
        cache.put(cache_size+1, process_list[cache_size])  # This should trigger eviction of the LRU item
        print("Cache after adding {} items:".format(cache_size + 1))
        cache.print_cache(2)

    def lru_get_func(cache):
        for i in range(cache_size):
            cache.get(i+1)
        print("Cache after getting {} items:".format(cache_size))
        cache.print_cache(2)
        cache.get(cache_size+1)  # Access the most recently added item
        print("Cache after getting {} items:".format(cache_size + 1))
        cache.print_cache(2)
    
    def mru_get_func(cache):
        for i in range(cache_size):
            cache.get(i+1)
        print("Cache after getting {} items:".format(cache_size))
        cache.print_cache(2)
        for i in range(cache_size, 0, -1):  # Access items in reverse order to make the most recently used item the one that was added first
            cache.get(i)
        print("Cache after getting {} items in reverse order:".format(cache_size + 1))
        cache.print_cache(2)

    def common_evict_func(cache):
        print("Evicting items until cache is empty as per {}:".format(cache.evict_policy()))
        for i in range(cache_size):
            print("  evicted {0}".format(cache.evict()))

    print("--- LRU Cache ---")
    lru_cache = LRUCache(cache_size)
    common_put_func(lru_cache)
    lru_get_func(lru_cache)
    common_evict_func(lru_cache)

    print("\n--- MRU Cache ---")
    mru_cache = MRUCache(cache_size)
    common_put_func(mru_cache)
    mru_get_func(mru_cache)
    common_evict_func(mru_cache)