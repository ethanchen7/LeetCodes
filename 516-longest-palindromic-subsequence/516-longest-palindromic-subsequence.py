class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        n = len(s)
        
        dp = [[0 for i in range(n)] for j in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
        
        for startIndex in range(n - 1, -1, -1):
            for endIndex in range(startIndex + 1, n):
                if s[startIndex] == s[endIndex]:
                    dp[startIndex][endIndex] = 2 + dp[startIndex + 1][endIndex - 1]
                else:
                    dp[startIndex][endIndex] = max(dp[startIndex + 1][endIndex], dp[startIndex][endIndex - 1])
        
        return dp[0][n-1] # start to end (0 to n - 1)