class Solution:
    def longestPalindrome(self, s: str) -> str:
        # expand around the center solution
        res = ""
        max_len = 0
        
        for i in range(len(s)):
            left, right = i, i
            
            # odd length
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                if (right - left + 1) > max_len:
                    res = s[left:right + 1]
                    max_len = right - left + 1
                
                left -= 1
                right += 1
            
            # even length
            left, right = i, i + 1
            
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                if (right - left + 1) > max_len:
                    res = s[left:right + 1]
                    max_len = right - left + 1
                
                left -= 1
                right += 1
        
        return res