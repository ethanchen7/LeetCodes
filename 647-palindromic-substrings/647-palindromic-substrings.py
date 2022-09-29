class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        count = 0
        for i in range(n):
            dp[i][i] = True
            count += 1
        
        for end in range(n):
            for start in range(end - 1, -1, -1):
                if s[start] == s[end]:
                    if end - start == 1 or dp[start + 1][end - 1]:
                        dp[start][end] = True
                        count += 1
        
        return count