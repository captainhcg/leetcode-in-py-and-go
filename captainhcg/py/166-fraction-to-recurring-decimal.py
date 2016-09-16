class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        if numerator % denominator == 0:
            return str(numerator / denominator)
        neg = (numerator / denominator) < 0
        numerator, denominator = abs(numerator), abs(denominator)
        integer_part, reminder = divmod(numerator, denominator)
        ret = str(integer_part) + "."
        reminder *= 10
        offset = len(ret)
        cache = {}
        while reminder:
            integer_part, reminder = divmod(reminder, denominator)
            if reminder:
                if (integer_part, reminder) in cache:
                    last_offset = cache[(integer_part, reminder)]
                    ret = ret[:last_offset] + "(%s)" % (ret[last_offset:])
                    break
                else:
                    cache[(integer_part, reminder)] = offset
            ret += str(integer_part)
            offset += 1
            reminder *= 10
        if neg:
            ret = "-" + ret
        return ret
