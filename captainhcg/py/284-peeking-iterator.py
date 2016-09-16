class PeekingIterator(object):
    def __init__(self, iterator):
        self.iter = iterator
        self.set_cache()
        
    def set_cache(self):
        if self.iter.hasNext():
            self.cache = next(self.iter)
        else:
            self.cache = None
            
    def peek(self):
        return self.cache
        
    def next(self):
        to_ret = self.cache
        self.set_cache()
        return to_ret
        
    def hasNext(self):
        return self.cache is not None
