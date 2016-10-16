class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode(c)
            curr = curr.children[c]
        curr.isWord = True
        return
        
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.searchHelper(self.root, word)
        
    def searchHelper(self, root, word):
        curr = root
        for idx, c in enumerate(word):
            if len(curr.children) == 0:
                return False
                
            if c == '.':
                for node in curr.children.values():
                    if self.searchHelper(node, word[idx + 1:]):
                        return True
                return False
            elif c not in curr.children:
                return False
            else:
                curr = curr.children[c]
        return curr.isWord
        
class TrieNode(object):
    def __init__(self, val=None, isWord=False):
        self.val = val
        self.isWord = isWord
        self.children = {}
