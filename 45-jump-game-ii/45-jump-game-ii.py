class Solution:
    def jump(self, nums: List[int]) -> int:
        
        dp = [math.inf for i in range(len(nums))]
        dp[0] = 0
        
        for start in range(len(nums) - 1):
            end = start + 1
            max_idx = start + nums[start]
            # get to every reachable target index and check how much it costs to get there
            while end <= max_idx and end < len(nums): 
                dp[end] = min(dp[end], dp[start] + 1) # the cost of getting to that starting index + 1 extra step
                end += 1

        return dp[len(nums) - 1]