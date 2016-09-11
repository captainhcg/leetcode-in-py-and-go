class Solution(object):
    def generatePalindromes(self, s):
        from collections import Counter
        unique = ""
        per_str = ""
        for ch, cnt in Counter(s).iteritems():
            if cnt % 2 != 0:
                if unique:
                    return []
                else:
                    unique = ch
            per_str += ch * (cnt / 2)

        def permutations(s):
            if len(s) <= 1:
                return [s]
            ret = []
            for idx, ch in enumerate(s):
                if idx == 0 or ch != s[idx-1]:
                    for suffix in permutations(s[:idx] + s[idx+1:]):
                        ret.append(s[idx] + suffix)
            return ret
        
        return ["".join(s)+unique+"".join(s[::-1]) for s in permutations(per_str)]
