import math
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        dp = [99999 for i in range(amount + 1)]
        dp[0] = 0
        # [0, 1, 1, 2, 3, 1, 2, 2, 3, 3, 2, 3] # coin counts
        #  0  1  2  3  4  5  6  7  8  9  10  11   amounts
        for i in range(1,amount + 1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], dp[i - c] + 1)

        if dp[-1] == 99999:
            return -1
        else:
            return dp[-1]