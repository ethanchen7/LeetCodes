class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        max_palindrome_length = 1
        max_start = 0
        
        for r in range(n):
            dp[r][r] = True
        
        for end in range(n):
            for start in range(end - 1, -1, -1):
                if s[start] == s[end]:
                    if (end - start == 1) or dp[start + 1][end - 1]:
                        dp[start][end] = True
                        if (end - start + 1) > max_palindrome_length:
                            max_palindrome_length = end - start + 1
                            max_start = start
        
        return s[max_start:max_start + max_palindrome_length]