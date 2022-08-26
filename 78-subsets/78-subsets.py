class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def dfs(idx, sub):
            
            if idx >= len(nums):
                result.append(sub[:])
                return
            
            sub.append(nums[idx])
            dfs(idx + 1, sub)
            sub.pop()
            dfs(idx + 1, sub)
        
        result = []
        dfs(0, [])
        return result