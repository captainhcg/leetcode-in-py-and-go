class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        self.ret = []
        if numRows:
            self.generateHelper(1, numRows)
        return self.ret
    
    def generateHelper(self, level, numRows):
        if level == 1:
            self.ret.append([1])
        else:
            new_row = []
            last_number = 0
            for n in self.ret[-1]:
                new_row.append(last_number + n)
                last_number = n
            new_row.append(1)
            self.ret.append(new_row)
        if level + 1 <= numRows:
            self.generateHelper(level + 1, numRows)
