class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        max_length = 1
        longest_start = 0
        
        for i in range(n):
            dp[i][i] = True
        
        for end in range(n):
            for start in range(end - 1, -1, -1):
                if s[start] == s[end]:
                    if (end - start == 1) or dp[start + 1][end - 1]:
                        dp[start][end] = True
                        if end - start + 1 > max_length:
                            max_length = end - start + 1
                            longest_start = start
        
        return s[longest_start:longest_start + max_length]