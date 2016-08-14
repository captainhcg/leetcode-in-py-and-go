class Solution(object):
    def groupStrings(self, strings):
        def get_offset(init, ch):
            offset = ord(ch) - init
            if offset < 0:
                offset += 26
            return offset
            
        def get_key(s):
            init = ord(s[0])
            return tuple(get_offset(init, ch) for ch in s)
        
        d = collections.defaultdict(list)
        for s in strings:
            d[get_key(s)].append(s)
        
        return [sorted(arr) for arr in d.values()]
