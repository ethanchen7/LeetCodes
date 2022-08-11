class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        
        dp = [[False for _ in range(n)] for _ in range(n)] # startIndex, endIndex
        count = 0

        # every string with one character is a palindrome
        for i in range(n):
            dp[i][i] = True
            count += 1
        
        for startIndex in range(n - 1, -1, -1):
            for endIndex in range(startIndex + 1, n):
                if s[startIndex] == s[endIndex]:
                    # if it's a two character string or if the remaining string is a palindrome
                    if endIndex - startIndex == 1 or dp[startIndex + 1][endIndex - 1]:
                        dp[startIndex][endIndex] = True
                        count += 1
        
        return count
                        
        