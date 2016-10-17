class Solution(object):
    def __init__(self):
        self.mapping = {
            0: 'Zero',
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen', 
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety'}
            
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
            
        ans = self.numbers(num)
        return ' '.join(x.strip() for x in ans.split(' ') if x.strip())
        
    def numbers(self, num):
        if num >= 1000000000:
            return self.mapping[num/1000000000] + ' Billion ' + self.numbers(num % 1000000000)
        if num >= 1000000:
            return self.numbers(num / 1000000) + ' Million ' + self.numbers(num % 1000000)
        if num >= 1000:
            return self.numbers(num / 1000) + ' Thousand ' + self.numbers(num % 1000)
        if num >= 100:
            return self.numbers(num / 100) + ' Hundred ' + self.numbers(num % 100)
        if num >= 10:
            if num / 10 != 1:
                return self.mapping[(num / 10) * 10] + (' ' + self.mapping[num % 10] if num % 10 != 0 else '')
            else:
                return self.mapping[num]
        if num > 0:
            return self.mapping[num]
        
        return ''
