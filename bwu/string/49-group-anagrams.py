class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mapping = {}
        for word in strs:
            s_word = ''.join(sorted(word))
            if s_word not in mapping:
                mapping[s_word] = [word]
            else:
                mapping[s_word] += [word]
                
        return mapping.values()
