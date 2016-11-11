import collections
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        ret = []
        mapping = collections.defaultdict(list)
        for string in strings:
            cvt = '0'
            for i in xrange(1, len(string)):
                cvt += str((ord(string[i]) - ord(string[i - 1])) % 26)
            mapping[cvt].append(string)
        return mapping.values()
