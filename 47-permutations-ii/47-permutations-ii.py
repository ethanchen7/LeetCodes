class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        perm = nums[:]
        result = []
        
        def dfs(idx):
            
            if idx == len(nums):
                result.append(perm[:])
                return
            
            lookup = set()
            
            for i in range(idx, len(nums)):
                
                if perm[i] not in lookup:
                    perm[idx], perm[i] = perm[i], perm[idx]        
                    dfs(idx + 1)
                    perm[idx], perm[i] = perm[i], perm[idx]
                    lookup.add(perm[i])

        dfs(0)
        return result