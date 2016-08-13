class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        import collections
        self.cache = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key):
        """
        :rtype: int
        """
        ret = self.cache.pop(key, -1)
        if ret != -1:
            self.cache[key] = ret
        return ret

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        self.cache.pop(key, None)
        if len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value
