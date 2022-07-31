class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # the queue will always be in decreasing order
        # the maximum of the window will always be at the front of the queue
        output = []
              
        queue = deque()
        
        # starts both pointers at 0
        
        # incrememts the right pointer
        
        # at any point, if the last element of the queue is less than the current number,
        # pop it off the element
        
        # append the current pointer index onto the queue
        
        # check that our first queue element is still in the range (less than left)
        
        # check that the window size is valid
        # append the first element of the queue to our output if the window size is valid
        # shift left up
        
        left, right = 0, 0
        
        while right < len(nums):
            
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            
            queue.append(right)
            
            if left > queue[0]:
                queue.popleft()
            
            if (right - left + 1) >= k:
                output.append(nums[queue[0]])
                left += 1
            
            right += 1
    
        return output
            