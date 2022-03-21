class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = 0, 0
        
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                nums[slow + 1] = nums[fast]
                slow += 1
            
            fast += 1
    
        return slow + 1
            
            