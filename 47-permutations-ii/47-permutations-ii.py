class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = []
        used = set() # store the INDICES of the ones we've used
        
        def dfs(perm):
            if len(perm) == len(nums):
                result.append(perm[:])
                return 
            
            for i in range(0, len(nums)):
                
                if (i in used) or (i > 0 and nums[i] == nums[i - 1] and not (i-1) in used):
                    continue

                used.add(i)
                dfs(perm + [nums[i]])
                used.remove(i)
            
        dfs([])
        return result