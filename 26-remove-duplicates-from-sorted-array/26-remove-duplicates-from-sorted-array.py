class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pointer, curr = 0, 1
        
        while curr < len(nums):
            
            if nums[curr] != nums[pointer]:
                pointer += 1
                nums[pointer] = nums[curr]
            
            curr += 1
       
        return pointer+1
                
            
            