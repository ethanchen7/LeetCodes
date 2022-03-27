class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n
        
        while True:
            slow = self.find_square_sum(slow)
            fast = self.find_square_sum(self.find_square_sum(fast))
            
            if slow == fast:
                break
        
        return slow == 1
    
    
    def find_square_sum(self, num):
        _sum = 0
        
        while num > 0:
            digit = num % 10
            _sum += digit * digit
            num //= 10
        
        return _sum