class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        isNegative = x < 0
        
        result = 0
        x = abs(x)
        while x:
            digit = x % 10
            result *= 10
            result += digit
            x /= 10
            
            if result > (2**31 - 1):
                return 0
        
        if isNegative:
            return -result
        return result