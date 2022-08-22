class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo = {}
        def dfs(remain):
            
            if remain == 0:
                return 1
            
            if remain in memo:
                return memo[remain]
            
            count = 0
            for n in nums:
                if n <= remain:
                    count += dfs(remain - n)
            
            memo[remain] = count
            return memo[remain]
        
        return dfs(target)