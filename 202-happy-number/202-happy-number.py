class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow, fast = n, n
        
        while True:
            slow = self.find_squares(slow)
            fast = self.find_squares(self.find_squares(fast))
            
            if slow == fast:
                break
        
        return slow == 1
            
    
    def find_squares(self, num):
        _sum = 0
        while num > 0:
            digit = num % 10
            _sum += digit * digit
            num //= 10
        
        return _sum