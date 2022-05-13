class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        sub = []
        nums.sort()
        self.dfs(nums, res, sub, 0)
        return res
    
    def dfs(self, nums, res, sub, i):
        
        if i == len(nums):
            res.append(sub[:])
            return
        
        sub.append(nums[i])
        self.dfs(nums, res, sub, i + 1)
        sub.pop()
        
        while i + 1 < len(nums) and nums[i] == nums[i+1]: #skip duplicates
            i += 1
        
        self.dfs(nums, res, sub, i + 1)