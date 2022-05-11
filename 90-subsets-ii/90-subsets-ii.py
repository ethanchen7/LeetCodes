class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        subsets = []
        subsets.append([])
        start, end = 0, 0
        
        for i in range(len(nums)):
            
            start = 0
            
            if i > 0 and nums[i] == nums[i-1]:
                start = end + 1
            
            end = len(subsets) - 1
            for j in range(start, end + 1):
                set1 = list(subsets[j])
                set1.append(nums[i])
                subsets.append(set1)
        
        return subsets