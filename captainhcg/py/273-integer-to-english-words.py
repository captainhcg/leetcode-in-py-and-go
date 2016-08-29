class Solution(object):
    def numberToWords(self, num):
        if num == 0:
            return "Zero"
            
        numstr = str(num)
        less_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        def helper(nstr, level):
            n = int(nstr)
            if n == 0:
                return ""
            _arr = []
            hundth, tenth = divmod(n, 100)
            if hundth:
                _arr.append("%s Hundred" % less_20[hundth])
            if tenth >= 20:
                _arr.append(tens[tenth / 10])
                tenth = tenth % 10
            _arr.append(less_20[tenth])
            if level:
                _arr.append(thousands[level])
            return " ".join(s for s in _arr if s)

        ret = []
        level = 0
        while len(numstr) > 3:
            ret.append(helper(numstr[-3:], level))
            level += 1
            numstr = numstr[:-3]
        ret.append(helper(numstr, level))

        return " ".join(s for s in ret[::-1] if s)
