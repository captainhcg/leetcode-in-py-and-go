class TrieNode(object):
    def __init__(self):
        self.hasword = False
        self.ptrs = {}

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.ptrs:
                node.ptrs[ch] = TrieNode()
            node = node.ptrs[ch]
        node.hasword = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.ptrs:
                return False
            node = node.ptrs[ch]
        return node.hasword
        

    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.ptrs:
                return False
            node = node.ptrs[ch]
        return True
