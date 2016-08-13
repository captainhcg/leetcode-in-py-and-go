class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1list = version1.split(".")
        v2list = version2.split(".")
        
        if len(v1list) < len(v2list):
            v1list.extend(["0"] * (len(v2list) - len(v1list)))
        elif len(v1list) > len(v2list):
            v2list.extend(["0"] * (len(v1list) - len(v2list)))
        
        for idx in xrange(min(len(v1list), len(v2list))):
            v1 = int(v1list[idx])
            v2 = int(v2list[idx])
            if v1 > v2:
                return 1
            if v1 < v2:
                return -1
        return 0
