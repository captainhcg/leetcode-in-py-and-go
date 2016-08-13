class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dict = {}
        for c in magazine:
            if c not in dict:
                dict[c] = 1
            else:
                dict[c] += 1
        
        for c in ransomNote:
            if c not in dict or dict[c] == 0:
                return False
            else:
                dict[c] -= 1
                
        return True
