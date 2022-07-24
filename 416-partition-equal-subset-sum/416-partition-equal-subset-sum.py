class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # the subset can be made if any numbers add up to 1/2 of the total sum
        
        if sum(nums) % 2 != 0: # we can't find equal subsets with an odd half
            return False
        
        n = len(nums)
        target = sum(nums) // 2
        
        dp = [[False for i in range(target + 1)] for j in range(len(nums))] # initialize 2D dp array
        
        # populate the first column
        for i in range(n): # base case, 0 numbers can add up to sum of 0
            dp[i][0] = True
        
        # populate the first row
        for j in range(1, target + 1): # ex: 1 can only be the sum of itself
            dp[0][j] = nums[0] == j # can only be True if it's equal to the first number
        
        # process the rest of the subsets
        for i in range(1, n):
            for j in range(1, target + 1):
                if dp[i - 1][j]: # if we solved the row above it, then it's the same answer
                    dp[i][j] = dp[i - 1][j]
                elif j >= nums[i]:
                    dp[i][j] = dp[i - 1][j - nums[i]] # check if there's a subset with the remaining sum
        
        return dp[n-1][target] #check the bottom - right corner of the dp