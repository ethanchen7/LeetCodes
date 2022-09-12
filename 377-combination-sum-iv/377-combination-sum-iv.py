class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo = {}
        
        def backtrack(remain):
            
            if remain in memo:
                return memo[remain]
            
            if remain == 0:
                return 1
            
            if remain < 0:
                return 0
            
            memo[remain] = 0
            for j in range(0, len(nums)):
                memo[remain] += backtrack(remain - nums[j])
            
            return memo[remain]
        
        return backtrack(target)
                
            