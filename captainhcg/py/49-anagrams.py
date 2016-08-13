class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in d:
                d[key] = [s]
            else:
                d[key].append(s)
        return list(d.values())
