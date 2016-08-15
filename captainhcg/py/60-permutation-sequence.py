class Solution(object):
    def getPermutation(self, n, k):
        arr, base = [],  [1, 1]
        for idx in xrange(2, n+1):
            base.append(idx * base[-1])
        
        idx, ele = k- 1, [str(number) for number in xrange(1, n + 1)] 
        while ele:
            offset, idx = divmod(idx, base[len(ele)-1])
            arr.append(ele[offset])
            ele = ele[:offset] + ele[offset+1:]
        return "".join(arr)
