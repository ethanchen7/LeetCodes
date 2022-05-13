class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        perm = []
        used = []
        self.dfs(nums, res, perm, used)
        return res
    
    def dfs(self, nums, res, perm, used):
        
        if len(perm) == len(nums):
            res.append(perm[:])
            return
        
        for i in range(len(nums)):
            
            if nums[i] not in used:
                perm.append(nums[i])
                used.append(nums[i])
                self.dfs(nums, res, perm, used)
                used.pop()
                perm.pop()
        
        