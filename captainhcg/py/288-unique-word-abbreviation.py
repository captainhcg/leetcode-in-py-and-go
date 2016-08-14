class ValidWordAbbr(object):
    def __init__(self, dictionary):
        self.cache = {}
        for word in dictionary:
            key = self.get_key(word)
            if key not in self.cache:
                self.cache[key] = word
            elif self.cache[key] != word:
                self.cache[key] = ""

    def isUnique(self, word):
        return self.cache.get(self.get_key(word), word) == word
    
    def get_key(self, s):
        return s if len(s) <= 2 else s[0] + str(len(s) - 2) + s[-1]
