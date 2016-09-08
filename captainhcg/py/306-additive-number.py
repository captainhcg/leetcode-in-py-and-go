class Solution(object):
    def isAdditiveNumber(self, num):
        if len(num) < 3:
            return False

        stack = []
        for idx in xrange(1, len(num) / 3 + 1):
            first_number_str = num[:idx]
            if len(first_number_str) > 1 and first_number_str[0] == "0":
                continue
            stack.append((int(first_number_str), num[idx:]))

        while stack:
            last_number, cur_str = stack.pop()
            for jdx in xrange(1, len(cur_str) / 2 + 1):
                this_number_str, remaining_str = cur_str[:jdx], cur_str[jdx:]
                if len(this_number_str) > 1 and this_number_str[0] == "0":
                    continue
                this_number = int(this_number_str)
                result_str = str(last_number + this_number)
                if remaining_str.startswith(result_str):
                    if remaining_str == result_str:
                        return True
                    stack.append((this_number, remaining_str))

        return False
