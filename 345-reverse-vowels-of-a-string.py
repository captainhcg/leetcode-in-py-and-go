class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = []
        for ch in s:
            if ch.lower() in "aeiou":
               vowels.append(ch)
        chs = []
        for ch in s:
            if ch.lower() in "aeiou":
                chs.append(vowels.pop())
            else:
                chs.append(ch)
        return "".join(chs)
