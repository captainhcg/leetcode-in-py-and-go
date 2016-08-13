class Solution(object):
    def cal(self, l, r, op):
        if op == "+":
            return l + r
        elif op == "-":
            return l - r
        else:
            return l * r
            
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        self.numbers = re.split(r'(\+|\-|\*)', input)
        if len(self.numbers) == 1:
            return [int(self.numbers[0])]
        self.ret = self.helper(0, len(self.numbers)-1)
        return self.ret
    
    def helper(self, lidx, ridx):
        if lidx == ridx:
            return [int(self.numbers[lidx])]
        ret = []
        for idx in xrange(lidx + 1, ridx, 2):
            op = self.numbers[idx]
            left = self.helper(lidx, idx-1)
            right = self.helper(idx+1, ridx)
            for l in left:
                for r in right:
                    ret.append(self.cal(l, r, op))
        return ret
