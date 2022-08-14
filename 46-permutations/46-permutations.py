class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        perm = []
        result = []
        
        def dfs(idx):
            
            if len(perm) == len(nums):
                result.append(perm[:])
                return
            
            for i in range(0, len(nums)):
                if nums[i] not in perm:
                    perm.append(nums[i])
                    dfs(idx + 1)
                    perm.pop()
                    
        
        dfs(0)
        return result