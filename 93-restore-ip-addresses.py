class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.ret = []
        self.helper([], s)
        return [".".join(ip) for ip in self.ret]
        
    def helper(self, arr, remain):
        if len(arr) == 4 and not remain:
            self.ret.append(tuple(arr))
            return
        if len(arr) >= 4 or not remain:
            return
        
        if len(remain) >= 1:
            arr.append(remain[:1])
            self.helper(arr, remain[1:])
            arr.pop()
        if len(remain) >= 2 and remain[0] != "0":
            arr.append(remain[:2])
            self.helper(arr, remain[2:])
            arr.pop()
        if len(remain) >= 3 and remain[0] != "0":
            ip = remain[:3]
            if int(ip) <= 255:
                arr.append(remain[:3])
                self.helper(arr, remain[3:])
                arr.pop()
