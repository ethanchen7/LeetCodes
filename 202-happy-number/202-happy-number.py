class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow, fast = n, n
        
        while True:
            slow = self.find_square(slow)
            fast = self.find_square(self.find_square(fast))
        
            if slow == fast:
                break
            
        return slow == 1
        
    
    def find_square(self, num):
        square = 0
        
        while num > 0:
            digit = num % 10
            square += (digit * digit)
            num //= 10
        
        return square