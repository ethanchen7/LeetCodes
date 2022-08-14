class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        sub = []
        result = []
        nums.sort() # sort so we can ignore duplicates right next to each other
        
        def dfs(idx):
            
            if idx >= len(nums):
                result.append(sub[:])
                return
            
            sub.append(nums[idx])
            dfs(idx + 1)
            sub.pop()
            
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]: # skip the duplicate numbers
                idx += 1
                
            dfs(idx + 1)
        
        dfs(0)
        return result