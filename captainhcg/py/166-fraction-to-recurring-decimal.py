class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        if numerator % denominator == 0:
            return str(numerator / denominator)
        neg = (numerator / denominator) < 0
        numerator, denominator = abs(numerator), abs(denominator)
        integer_part, reminder = divmod(numerator, denominator)
        ret = str(integer_part) + "."
        reminder *= 10

        current = ""
        offset = -1
        cache = {}
        while True:
            integer_part, reminder = divmod(reminder, denominator)
            current += str(integer_part)
            offset += 1
            if reminder == 0:
                ret += current
                break
            elif (integer_part, reminder) in cache:
                last_offset = cache[(integer_part, reminder)]
                ret += current[:last_offset] + "(%s)" % (current[last_offset:-1])
                break
            else:
                cache[(integer_part, reminder)] = offset
            reminder *= 10
        if neg:
            ret = "-" + ret
        return ret
