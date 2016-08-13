class Solution(object):
    def partition(self, s):
        if not s:
        	return [[]]
        	
        m = [[False] * len(s) for _ in xrange(len(s))]
        for idx, ch in enumerate(s):
            m[idx][idx] = True
            offset = 0
            while True:
                if idx-offset >= 0 and idx+offset < len(s) and s[idx-offset] == s[idx+offset]:
                    m[idx-offset][idx+offset] = True
                    offset += 1
                else:
                    break
            if idx+1 < len(s) and ch == s[idx+1]:
                m[idx][idx+1] = True
                offset = 0
                while True:
                    if idx-offset >= 0 and idx+offset+1 < len(s) and s[idx-offset] == s[idx+offset+1]:
                        m[idx-offset][idx+offset+1] = True
                        offset += 1
                    else:
                        break
        ret = []
        arr = []
        def dfs(st):
        	for ed in xrange(st, len(s)):
        		if m[st][ed]:
        			if ed == len(s) - 1:
        				ret.append(arr + [s[st:ed+1]])
        			else:
        				arr.append(s[st:ed+1])
        				dfs(ed+1)
        				arr.pop()
        dfs(0)
        return ret 
