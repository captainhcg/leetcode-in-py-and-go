class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        arr = []
        prints = []
        m = {"A": 0, "C": 1, "G": 2,"T": 3}
        res = set()
        l = set()
        
        mask = 0  # 0b11111111111111111111
        for idx in xrange(0, 20):
            mask |= (1 << idx)
            
        for ch in s:
            arr.append(m[ch])
        for idx, v in enumerate(arr):
            fp = 0
            if idx == 0:
                fp = arr[idx]
            else:
                fp = (prints[idx-1] << 2) & mask | arr[idx]
            
            prints.append(fp)
            if idx >= 9:
                if fp not in res:
                    res.add(fp)
                else:
                    l.add(s[idx-9:idx+1])
        return [s for s in l]
