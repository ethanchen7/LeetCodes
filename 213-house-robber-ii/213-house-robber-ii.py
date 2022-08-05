class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def houseRobberOne(arr):
            dp = [0] * len(arr)
            dp[0] = arr[0]

            for i in range(1, len(arr)):
                dp[i] = max(dp[i - 1], dp[i-2] + arr[i]) # rob one before, or rob two before plus this one

            return max(dp)
        
        if len(nums) < 2:
            return nums[0]
        
        include_first_house = houseRobberOne(nums[0:len(nums)-1])
        include_last_house = houseRobberOne(nums[1:])
        
        return max(include_first_house, include_last_house)
        