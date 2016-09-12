class Solution(object):
    def addOperators(self, num, target):
        ret = []
        def dfs(cur, res, last, nums_remaining):
            if not nums_remaining:
                if res + last == target:
                    ret.append("".join(cur))
                return

            for idx in xrange(1, len(nums_remaining) + 1):
                val_str, next_str = nums_remaining[:idx], nums_remaining[idx:]
                if len(val_str) >= 2 and val_str[0] == "0":
                    continue
                val = int(val_str)
                cur.extend(["+", val_str])
                dfs(cur, res + last, val, next_str)
                cur[-2] = "-"
                dfs(cur, res + last, -val, next_str)
                cur[-2] = "*"
                dfs(cur, res, last * val, next_str)
                del cur[-2:]

        for idx in xrange(1, len(num) + 1):
            val_str, next_str = num[:idx], num[idx:]
            if len(val_str) >= 2 and val_str[0] == "0":
                continue
            val = int(val_str)
            dfs([val_str], 0, val, next_str)

        return ret
