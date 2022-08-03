class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        perm = []
        
        def dfs(i):
            
            if len(perm) == len(nums):
                result.append(perm[:])
                return
            
            for j in range(0, len(nums)):
                if nums[j] not in perm:
                    perm.append(nums[j])
                    
                    dfs(j + 1)
                    
                    perm.pop()
        
        dfs(0)
        return result