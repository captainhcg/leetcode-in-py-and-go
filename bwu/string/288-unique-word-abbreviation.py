class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.abbv_dict = {}
        for word in dictionary:
            abbv_word = self.abbv(word)
            if abbv_word not in self.abbv_dict:
                self.abbv_dict[abbv_word] = word
            elif word != self.abbv_dict[abbv_word]:
                self.abbv_dict[abbv_word] = ''

    def abbv(self, word):
        if len(word) > 2:
            return word[0] + str(len(word) - 2) + word[-1]
        return word
        
    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abbv_word = self.abbv(word)
        return abbv_word not in self.abbv_dict or self.abbv_dict[abbv_word] == word


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")
