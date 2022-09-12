class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def houseRobberOne(arr):
            
            if not arr:
                return 0
            
            dp = [0] * len(arr)
            dp[0] = arr[0]
            
            for i in range(1,len(arr)):
                dp[i] = max(dp[i-1], dp[i-2] + arr[i])
            
            return dp[-1]
        
        if len(nums) == 1:
            return nums[0]
        
        return max(houseRobberOne(nums[1:]), houseRobberOne(nums[:-1]))