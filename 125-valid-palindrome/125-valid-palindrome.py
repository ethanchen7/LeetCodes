class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        chars = [c.lower() for c in s if c.isalnum()]
        left = 0
        right = len(chars) - 1
        
        while left <= right:
            
            if chars[left] != chars[right]:
                return False
            else:
                left += 1
                right -= 1
        
        return True