class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        result = []
        sub = []
        
        def dfs(sub, i):
            
            if i >= len(nums):
                result.append(sub[:])
                return
            
            sub.append(nums[i])
            dfs(sub, i + 1)
            
            sub.pop()
            dfs(sub, i + 1)
        
        dfs(sub, 0)
        return result