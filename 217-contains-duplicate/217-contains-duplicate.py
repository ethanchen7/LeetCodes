class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        seen = {}
        
        for n in nums:
            if n not in seen:
                seen[n] = 1
            else:
                return True
        
        return False