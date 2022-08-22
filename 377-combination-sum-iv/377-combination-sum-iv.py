class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        #    [1, 2, 3] nums
        # [1, 1, 2, 4, 7] # dp
        # pattern is that dp[i] is just a sum of all the previous combinations
        
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            
            for n in nums:
                if i>=n:
                    dp[i] += dp[i - n] # add all the other possible combinations up until this point
        
        return dp[target]