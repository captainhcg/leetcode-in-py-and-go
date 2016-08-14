class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        str = list(s)
        head, tail = 0, len(s) - 1
        while head < tail:
            if str[head].lower() not in vowels:
                head += 1
                continue
            if str[tail].lower() not in vowels:
                tail -= 1
                continue
            
            str[head], str[tail] = str[tail], str[head]
            head += 1
            tail -= 1
            
        return ''.join(str)
