class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        for i in range(len(nums)):
            slow, fast = i, i
            direction = nums[i] > 0
            
            while True:
                slow = self.new_index(nums, slow, direction)
                fast = self.new_index(nums, fast, direction)
                
                if fast != -1:
                    fast = self.new_index(nums, fast, direction)
                
                if slow == -1 or fast == -1 or slow == fast:
                    break
            
            if slow != -1 and fast != -1:
                return True
        
        return False
                    
                
        
    
    def new_index(self, nums, curr_index, direction):
        
        current_direction = nums[curr_index] > 0
        if current_direction != direction:
            return -1
        
        new_index = (curr_index + nums[curr_index]) % len(nums)
        new_direction = nums[new_index] > 0
        if curr_index == new_index: # there is a loop
            return -1
        
        return new_index