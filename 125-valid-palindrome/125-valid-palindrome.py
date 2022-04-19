class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        res = [char.lower() for char in s if char.isalnum()]
        
        left, right = 0, len(res) - 1
        while left <= right:
            if res[left] != res[right]:
                return False
            left += 1
            right -= 1
        
        return True