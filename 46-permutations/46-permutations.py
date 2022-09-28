class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        result = []
        def dfs(idx):
            
            if idx == len(nums):
                result.append(nums[:])
                return
            
            for j in range(idx, len(nums)):
                nums[idx], nums[j] = nums[j], nums[idx]
                dfs(idx + 1)
                nums[idx], nums[j] = nums[j], nums[idx]
        
        dfs(0)
        return result