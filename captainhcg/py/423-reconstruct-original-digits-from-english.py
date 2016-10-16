class Solution(object):
    def originalDigits(self, s):
        from collections import Counter
        ret = []
        m = [('0', 'zero', 'z'), ('4', 'four', 'u'), ('5', 'five', 'f'), ('7', 'seven', 'v'), ('8', 'eight', 'g'), ('6', 'six', 's'), ('3', 'three', 'h'), ('9', 'nine', 'i'), ('2', 'two', 't'), ('1', 'one', 'o')]
        total = Counter(s)
        for char, word, sign in m:
            times = total.get(sign)
            if times:
                ret.extend([char] * times)
                for ch in word:
                    total[ch] = total[ch] - times
        return "".join(sorted(ret))
