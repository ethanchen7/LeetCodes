class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        perm = []
        self.dfs(nums, res, perm)
        return res
    
    def dfs(self, nums, res, perm):
        
        if (len(perm) == len(nums)):
            res.append(perm[:])
            return
        
        for i in range(len(nums)):
            
            if nums[i] not in perm:
                perm.append(nums[i])
                self.dfs(nums, res, perm)
                perm.pop()
                