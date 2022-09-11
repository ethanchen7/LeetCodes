class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        dp = [[1,1] for _ in range(n)] # max_length, count
        
        global_max = 1

        for i in range(1, n):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    if dp[i][0] < dp[j][0] + 1:
                        dp[i][0] = dp[j][0] + 1
                        dp[i][1] = dp[j][1]
                    
                    elif dp[j][0] + 1 == dp[i][0]:
                        dp[i][1] += dp[j][1]
            global_max = max(global_max, dp[i][0])
        
        result = 0
        for mx_len, count in dp:
            if mx_len == global_max:
                result += count
        
        return result
        
        
        