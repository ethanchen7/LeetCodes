class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = [(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),(50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]
        
        result = ""
        remainder = num
        while remainder > 0:
            for digit, key in roman:
                if digit <= remainder:
                    result += key
                    remainder -= digit
                    break
        
        return result