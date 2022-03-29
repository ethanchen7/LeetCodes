class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        
        for i in range(len(nums)):
            direction = nums[i] >= 0 # boolean
            slow, fast = i, i
        
            while True:
                
                slow = self.find_next_index(nums, direction, slow)
                fast = self.find_next_index(nums, direction, fast)
                
                if fast != -1:
                    fast = self.find_next_index(nums, direction, fast)
                
                if slow == -1 or fast == -1 or slow == fast:
                    break
            
            if slow != -1 and slow == fast:
                return True
        
        return False
    
    def find_next_index(self, nums, direction, current_index):
        current_direction = nums[current_index] >= 0
        if direction != current_direction:
            return -1
        
        next_index = (current_index + nums[current_index]) % len(nums)
        
        if current_index == next_index:
            return -1
        
        return next_index